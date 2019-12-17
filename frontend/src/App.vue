<template>
  <div id="app">
    <header id="nav">
      <span id="home">
        <router-link to="/">MealGo</router-link>
      </span>
      <template v-if="logged_in">
        <router-link to="/planner">Planner</router-link>
        <router-link to="/recipes">Recipes</router-link>
        <router-link to="/shopping">Shopping List</router-link>
      </template>
      <template v-else>
        <router-link to="/signup">Sign Up</router-link>
        <router-link to="/login">Log In</router-link>
      </template>
    </header>
    <section id="content">
      <router-view />
    </section>
    <footer id="footer">
      <div class="copyright">&copy; 2019 MealGo.app</div>
    </footer>
  </div>
</template>

<style>
html,
body {
  margin: 0;
  padding: 0;
}

#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  margin: 0;
  padding: 0;
}

#content {
  min-height: 80vh;
  padding-left: 20px;
}

#nav {
  display: flex;
}

#content,
#nav {
  max-width: 1200px;
  margin: 0 auto;
}

#nav,
#footer {
  padding: 0 0 0 20px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav > a {
  padding-left: 10px;
  padding-right: 10px;
}

#nav a.router-link-exact-active {
  color: #558790;
}

a {
  display: inline-block;
  min-width: 48px;
  min-height: 48px;
  xoutline: 1px dashed;
  box-sizing: border-box;
  line-height: 48px;
  color: #2f3781;
}

button {
  min-width: 48px;
  min-height: 48px;
}

#footer {
  text-align: left;
  padding: 20px;
  min-height: 200px;
  background: #222;
  color: #888;
  font-size: 10pt;
}

#footer .copyright {
  line-height: 3em;
  max-width: 1200px;
  margin: 0 auto;
}

#home {
  display: block;
  text-align: left;
  flex-grow: 1;
  font-size: 24px;
  line-height: 24px;
}
</style>
