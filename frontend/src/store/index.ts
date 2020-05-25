import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    loggedIn: false,
    rootIP: "xxx.xxx.xxx.xxx",
    securityKey: "",
  },
  mutations: {},
  actions: {},
  modules: {},
});
