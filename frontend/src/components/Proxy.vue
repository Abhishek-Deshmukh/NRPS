<template>
  <div class="container">
    <div class="row heading">
      <div class="col-1 number">#</div>
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

    <div class="row mt-1" v-for="proxy in proxies" :key="proxy.id">
      <div class="col-1 number">
        {{ proxy.id }}
      </div>
      <div class="col-2">
        <b-form-select required v-model="proxy.type">
          <b-form-select-option value="">--select--</b-form-select-option>
          <b-form-select-option value="static">Static</b-form-select-option>
          <b-form-select-option value="proxy">Proxy</b-form-select-option>
        </b-form-select>
      </div>
      <div class="col-4">
        <b-form-input
          required
          v-model="proxy.nameserver"
          placeholder="example.com www.example.com"
        />
      </div>
      <div class="col-4">
        <b-form-input
          required
          v-model="proxy.address"
          placeholder="localhost:8000"
        />
      </div>
      <div class="col-1">
        <b-button variant="outline-danger" @click="removeProxy(proxy)"
          >-</b-button
        >
      </div>
    </div>

    <b-button variant="outline-success" class="mt-2" @click="addProxy()"
      >+</b-button
    >
    <br />
    <b-button variant="outline-success" class="mt-2" @click="applyProxies()"
      >Apply</b-button
    >
    <b-button variant="outline-info" class="mt-2 ml-2" @click="fetchProxies()"
      >Reset</b-button
    >
    <b-button
      variant="outline-warning"
      class="mt-2 ml-2"
      @click="restartServer()"
      >Restart server</b-button
    >
    <b-button variant="outline-danger" class="mt-2 ml-2" @click="clearSecrets()"
      >Clear secrets</b-button
    >
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
      type: "",
    });
  }
  removeProxy(proxy: { id: number; nameserver: string; address: string }) {
    this.proxies = this.proxies.filter((prox) => prox.id != proxy.id);
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
    console.log(response.data)
  }
}
</script>

<style lang="scss">
.heading {
  font-size: 19px;
  line-height: 30px;
  letter-spacing: 0.064em;
  font-weight: 800;
}
.number {
  padding-top: 8px;
}
</style>
