<template>
  <div class="center">
    <img src="../assets/logo.png" class="hover-scale" />
    <h1>
      Welcome to {{ $store.state.serverName }}'s nginx reverse proxy setter
    </h1>
    <br />
    <Login v-if="!$store.state.loggedIn" />
    <Proxy v-else />
  </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from "vue-property-decorator";
import Login from "./Login.vue";
import Proxy from "./Proxy.vue";

@Component({
  components: {
    Login,
    Proxy,
  },
})
export default class HelloWorld extends Vue {
  @Prop() private server!: string;
}
</script>

<style scoped lang="scss">
.hover-scale {
  transition: 0.2s;
  &:hover {
    transform: scale(1.1);
  }
}
.center {
  text-align: center;
}
h1 {
  font-size: 2.1rem;
  line-height: 1.1;
  letter-spacing: 0.068em;
  font-weight: 400;
}
</style>
