<template>
  <div>
    <div class="row heading">
      <div class="col-2">
        Type
      </div>
      <div class="col-4">
        Nameserver
      </div>
      <div class="col-2">
        path
      </div>
      <div class="col-3">
        Address
      </div>
    </div>

    <div class="row" v-for="proxy in proxies" :key="proxy.id">
      <div class="col-2">
        <span class="dropdown">
          <select required v-model="proxy.type">
            <option value="">--select--</option>
            <option value="static">Static</option>
            <option value="proxy">Proxy</option>
          </select>
        </span>
      </div>
      <div class="col-4">
        <input
          required
          v-model="proxy.nameserver"
          placeholder="example.com www.example.com"
          style="max-width: 500px;"
        />
      </div>
      <div class="col-2">
        <input
          required
          v-model="proxy.location"
          placeholder="/"
        />
      </div>
      <div class="col-3">
        <input
          required
          v-model="proxy.address"
          placeholder="http://localhost:8000"
        />
      </div>
      <div class="col-1">
        <button class="remove hover-red" @click="removeProxy(proxy)">
          -
        </button>
      </div>
    </div>
    <br />

    <button class="add" @click="addProxy()">
      +
    </button>
    <br />
    <button class="apply" @click="applyProxies()">
      Apply
    </button>
    <button class="reset" @click="fetchProxies()">
      Reset
    </button>
    <br />
    <button class="restart" @click="restartServer()">
      Restart server
    </button>
    <button class="logout" @click="clearSecrets()">
      Logout
    </button>
  </div>
</template>

<script lang="ts">
  import {Component, Prop, Vue} from 'vue-property-decorator';
  import axios from 'axios';

  @Component
  export default class Proxy extends Vue {
    proxies: {
      id: number;
      nameserver: string;
      location: string;
      address: string;
      type: string;
    }[] = [];

    addProxy() {
      this.proxies = this.proxies.concat({
        id: this.proxies.length + 1,
        location: '/',
        nameserver: '',
        address: '',
        type: '',
      });
    }
    removeProxy(proxy: {id: number; nameserver: string; address: string}) {
      this.proxies = this.proxies.filter(prox => prox.id != proxy.id);
    }
    async fetchProxies() {
      const response = await axios.get(
        'https://' + this.$store.state.rootURL + '/api/get_proxies',
      );
      this.proxies = response.data;
      console.log(response.data);
    }
    async applyProxies() {
      const response = await axios.post(
        'https://' + this.$store.state.rootURL + '/api/set_proxies',
        {proxies: this.proxies, securityKey: this.$store.state.securityKey},
      );
      console.log(response.data);
    }
    created() {
      this.fetchProxies();
    }
    async restartServer() {
      const response = await axios.post(
        'https://' + this.$store.state.rootURL + '/api/restart_server',
        {securityKey: this.$store.state.securityKey},
      );
      console.log(response.data);
    }
    async clearSecrets() {
      this.$store.state.loggedIn = false;
      const response = await axios.post(
        'https://' + this.$store.state.rootURL + '/api/clean_secrets',
        {securityKey: this.$store.state.securityKey},
      );
      console.log(response.data);
    }
  }
</script>
<style scope lang="scss">
.remove {
  color: #8a4f3e;
  border: 1px solid #8a4f3e;
}
.add {
  color: #e98215;
  border: 1px solid #e98215;
  margin-bottom: 5px;
  transition: 0.2s;
  &:hover {
    background: #e98215;
    color: white;
  }
}
.apply {
  color: green;
  border: 1px solid green;
  &:hover {
    background: green;
    color: white;
  }
}
.reset {
  color: red;
  border: 1px solid red;
  transition: 0.2s;
  &:hover {
    background: red;
    color: white;
  }
}
.logout {
  color: red;
  border: 1px solid red;
  &:hover {
    background: red;
    color: white;
  }
}
.restart {
  color: #39445d;
  border: 1px solid #39445d;
  transition: 0.2s;
  &:hover {
    background:  #39445d;
    color: white;
  }
}
</style>
