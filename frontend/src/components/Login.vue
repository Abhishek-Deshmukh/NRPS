<template>
  <div class="container">
    <p v-if="error" class="error">Authentication Error</p>
    <form>
      <span label="Your Username:" for="input-1">Your Username:</span>
      <br />
      <input v-model="form.username" required placeholder="Enter user-name" />
      <br />
      <span for="input-2">Password:</span>
      <br />
      <input
        type="password"
        v-model="form.password"
        required
        placeholder="Enter password"
      />
      <br />
      <button type="submit" @click="onSubmit()" class="hover-green">Submit</button>
      <button type="reset" @click="onReset()" class="hover-red">Reset</button>
    </form>
  </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from "vue-property-decorator";
import axios from "axios";

@Component
export default class Login extends Vue {
  error: boolean = false;
  form = {
    username: "",
    password: ""
  };
  async onSubmit(event: any) {
    const response = await axios.post(
      "https://" + this.$store.state.rootURL + "/api/login",
      this.form
    );
    console.log(response);
    if (response.data) {
      this.error = false;
      this.$store.state.loggedIn = true;
      this.$store.state.securityKey = response.data;
    } else {
      this.error = true;
    }
  }
  onReset() {
    this.form = {
      username: "",
      password: ""
    };
  }
}
</script>
<style scoped lang="scss">
.error {
  color: red;
  font-size: 11px;
  line-height: 30px;
  letter-spacing: 0.064em;
  font-weight: 900;
  font-style: italic;
}
input {
  margin-bottom: 30px;
  margin-top: 5px;
  transition: 0.2s;
}
button {
  margin: 10px;
  border: 1px solid brown;
}
</style>
