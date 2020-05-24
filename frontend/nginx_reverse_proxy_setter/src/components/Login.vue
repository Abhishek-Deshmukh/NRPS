<template>
  <div class="container-fluid">
    <p v-if="error" class="error">Authentication Error</p>
    <b-form @submit="onSubmit" @reset="onReset">
      <b-form-group label="Your Username:" label-for="input-1">
        <b-form-input
          id="input-1"
          v-model="form.username"
          required
          placeholder="Enter user-name"
        ></b-form-input>
      </b-form-group>
      <b-form-group label="Password:" label-for="input-2">
        <b-form-input
          id="input-2"
          type="password"
          v-model="form.password"
          required
          placeholder="Enter password"
        ></b-form-input>
      </b-form-group>
      <b-button type="submit" variant="primary">Submit</b-button>
      <b-button type="reset" variant="danger" class="ml-3">Reset</b-button>
    </b-form>
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
    password: "",
  };
  async onSubmit(event: any) {
    event.preventDefault();
    const response = await axios.post("http://localhost:8081/login", this.form)
    console.log(response);
    if (response.data) {
      this.error = false;
      this.$store.state.loggedIn = true;
    } else {
      this.error = true;
    }
  }
  onReset() {
    this.form = {
      username: "",
      password: "",
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
</style>
