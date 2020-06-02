<template>
  <div class="container">
    <div class="center">
      <h1>Welcome to {{ $store.state.userName }}'s nginx reverse proxy setter</h1>
      <br />
        <Login v-if="!$store.state.loggedIn" />
        <Proxy v-else />
    </div>
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
.center {
  text-align: center;
}
h1 {
  font-size: 2rem;
  line-height: 0.9;
  letter-spacing: 0.064em;
  font-weight: 500;
  font-style: normal;
}
</style>
