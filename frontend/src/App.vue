<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<style lang="scss">
@import url(https://cdn.jsdelivr.net/gh/tonsky/FiraCode@4/distr/fira_code.css);
@import './assets/bootstrap-grid.min.css';
body {
  padding-top: 40px;
  font-family: 'Fira Code';
}
.heading {
  font-size: 19px;
  line-height: 30px;
  letter-spacing: 0.064em;
  font-weight: 800;
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
