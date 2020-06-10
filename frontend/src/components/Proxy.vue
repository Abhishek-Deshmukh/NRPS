<template>
  <div>
    <div class="container">
      <div class="row heading">
        <div class="col-1">#</div>
        <div class="col-2">
          Type
        </div>
        <div class="col-4">
          Nameserver
        </div>
        <div class="col-4">
          Address
        </div>
      </div>

      <div class="row" v-for="proxy in proxies" :key="proxy.id">
        <div class="col-1">
          {{ proxy.id }}
        </div>
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
          />
        </div>
        <div class="col-4">
          <input
            required
            v-model="proxy.address"
            placeholder="http://localhost:8000"
          />
        </div>
        <div class="col-1">
          <button class="remove" @click="removeProxy(proxy)">
            -
          </button>
        </div>
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
import { Component, Prop, Vue } from "vue-property-decorator";
import axios from "axios";

@Component
export default class Proxy extends Vue {
  proxies: {
    id: number;
    nameserver: string;
    address: string;
    type: string;
  }[] = [];

  addProxy() {
    this.proxies = this.proxies.concat({
      id: this.proxies.length + 1,
      nameserver: "",
      address: "",
      type: ""
    });
  }
  removeProxy(proxy: { id: number; nameserver: string; address: string }) {
    this.proxies = this.proxies.filter(prox => prox.id != proxy.id);
  }
  async fetchProxies() {
    const response = await axios.get(
      "http://" + this.$store.state.rootIP + ":8081/"
    );
    this.proxies = response.data;
    console.log(response.data);
  }
  async applyProxies() {
    const response = await axios.post(
      "http://" + this.$store.state.rootIP + ":8081/set_proxies",
      { proxies: this.proxies, securityKey: this.$store.state.securityKey }
    );
    console.log(response.data);
  }
  created() {
    this.fetchProxies();
  }
  async restartServer() {
    const response = await axios.post(
      "http://" + this.$store.state.rootIP + ":8081/restart_server",
      { securityKey: this.$store.state.securityKey }
    );
    console.log(response.data);
  }
  async clearSecrets() {
    this.$store.state.loggedIn = false;
    const response = await axios.post(
      "http://" + this.$store.state.rootIP + ":8081/clean_secrets",
      { securityKey: this.$store.state.securityKey }
    );
    console.log(response.data);
  }
}
</script>
