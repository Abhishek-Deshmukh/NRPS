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

<style lang="scss">
div {
  display: inline-block;
  margin: auto;
}
.heading {
  font-size: 19px;
  line-height: 30px;
  letter-spacing: 0.064em;
  font-weight: 800;
}
.container {
  display: grid !important;
  margin-left: 20px;
  margin-right: 20px;
}
input {
  font-family: "Fira Code";
  width: 300px;
  border-radius: 5px;
  box-shadow: none;
  padding: 8px;
  border: 1px solid #8a4f3e;
}
.row {
  margin-bottom: 10px;
}
.col-1 {
  width: 8vw;
}
.col-2 {
  width: 16vw;
}
.col-4 {
  width: 30vw;
}
.dropdown {
  position: relative;
  display: inline-block;
  vertical-align: middle;
}
.dropdown select {
  font-family: "Fira Code";
  background-color: #8a4f3e;
  color: #fff;
  font-size: inherit;
  padding: 0.5em;
  padding-right: 2.5em;
  border: 0;
  margin: 0;
  border-radius: 3px;
  text-indent: 0.01px;
  text-overflow: "";
  -webkit-appearance: button; /* hide default arrow in chrome OSX */
}
.dropdown::before {
  /*  Custom dropdown arrow cover */
  width: 2em;
  right: 0;
  top: 0;
  bottom: 0;
  border-radius: 0 3px 3px 0;
}
.dropdown::after {
  content: "";
  position: absolute;
  pointer-events: none;
}
.dropdown::after {
  content: "\25BC";
  height: 1em;
  font-size: 0.625em;
  line-height: 1;
  right: 1.2em;
  top: 50%;
  margin-top: -0.5em;
}
button {
  font-family: "Fira Code";
  background-color: transparent;
  color: black;
  padding: 8px 20px 8px 20px;
  border-radius: 5px;
  margin: 3px;
}
.remove {
  color: #8a4f3e;
  border: 1px solid #8a4f3e;
}
.add {
  color: #e98215;
  border: 1px solid #e98215;
  margin-bottom: 5px;
}
.apply {
  color: green;
  border: 1px solid green;
}
.reset {
  color: red;
  border: 1px solid red;
}
.logout {
  color: red;
  border: 1px solid red;
}
.restart {
  color: #39445d;
  border: 1px solid #39445d;
}
</style>
