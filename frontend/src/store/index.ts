import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {

    rootURL: "",
    // rootURL: "nrps.dunce.ml"

    serverName: "",
    // serverName: "dunce"

    securityKey: "",
    loggedIn: false,
  },
  mutations: {},
  actions: {},
  modules: {},
});
