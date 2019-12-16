<template>
  <div id="app">
    <header id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/planner">Planner</router-link> |
      <router-link to="/recipes">Recipes</router-link> |
      <router-link to="/shopping">Shopping List</router-link> |
      <router-link to="/signup">Sign Up</router-link> |
      <router-link to="/login">Log In</router-link>
    </header>
    <section class="content">
      <router-view />
    </section>
    <footer>
      <div class="copyright">&copy; 2019 MealGo.app</div>
    </footer>
  </div>
</template>

<style>

html, body {
  margin: 0;
  padding: 0;
}

.content {
  min-height: 50vh;
}

#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin: 0;
  padding: 0;
}
#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #0a884f;
}

a {
  display: inline-block;
  min-width: 48px;
  min-height: 48px;
  outline: 1px dashed;
  color: #2f815c;
}

button {
  min-width: 48px;
  min-height: 48px;
}

footer {
  margin-top: 20px;
  min-height: 200px;
  vertical-align: center;
  background: #222;
  color: white;
  bottom: 0;
}

footer .copyright {
  line-height: 3em;
}
</style>
