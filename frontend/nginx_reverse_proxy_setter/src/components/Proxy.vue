<template>
  <div class="container">
    <div class="row heading">
      <div class="col-1 number">#</div>
      <div class="col-5">
        Nameserver
      </div>
      <div class="col-5">
        Address
      </div>
    </div>

    <div class="row mt-1" v-for="proxy in proxies" :key="proxy.id">
      <div class="col-1 number">
        {{ proxy.id }}
      </div>
      <div class="col-5">
        <b-form-input required v-model="proxy.nameserver" />
      </div>
      <div class="col-5">
        <b-form-input required v-model="proxy.address" />
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
  </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from "vue-property-decorator";
import axios from "axios";

@Component
export default class Proxy extends Vue {
  proxies: { id: number; nameserver: string; address: string }[] = [
    {
      id: 1,
      nameserver: "www.dunce.com",
      address: "80",
    },
    {
      id: 2,
      nameserver: "other.dunce.com",
      address: "localhost:8005",
    },
  ];

  addProxy() {
    this.proxies = this.proxies.concat({
      id: this.proxies.length + 1,
      nameserver: "",
      address: "",
    });
  }
  removeProxy(proxy: { id: number; nameserver: string; address: string }) {
    this.proxies = this.proxies.filter((prox) => prox.id != proxy.id);
  }
  async fetchProxies() {
    const response = await axios.get("http:\/\/localhost:8081/");
    this.proxies = response.data;
  }
  async applyProxies() {
    const response = await axios.post(
      "http:\/\/localhost:8081/set_proxies",
      this.proxies
    );
    console.log(response);
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
