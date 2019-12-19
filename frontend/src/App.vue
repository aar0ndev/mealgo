<template>
  <div id="app" :class="{home: !logged_in}">
    <header id="nav">
      <div id="nav-container">
        <span id="home">
          <router-link to="/" class="logo">MealGo</router-link>
        </span>
        <span id="links">
          <template v-if="logged_in">
            <router-link to="/planner">Planner</router-link>
            <router-link to="/recipes">Recipes</router-link>
            <router-link to="/shopping">Shopping List</router-link>
          </template>
          <template v-else>
            <router-link to="/signup">Sign Up</router-link>
            <router-link to="/login">Log In</router-link>
          </template>
        </span>
      </div>
    </header>
    <section id="content">
      <transition name="fade">
        <router-view />
      </transition>
    </section>
    <footer id="footer">
      <div class="copyright">&copy; 2019 MealGo.app</div>
    </footer>
  </div>
</template>

<style>
* {
  box-sizing: border-box;
}

html,
body {
  margin: 0;
  padding: 0;
  min-height: 100vh;
  background: #fff;
}

#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  margin: 0;
  padding: 0;
  display: flex;
  flex-flow: stretch;
  flex-direction: column;
  min-height: 100vh;
}

#nav {
  background: linear-gradient(#eff, #dff);
}

#content {
  flex-grow: 1;
}

#nav-container {
  display: flex;
  width: 100%;
  max-width: 1200px;
  margin: 0 auto;
}

#nav-container,
#footer {
  padding: 0 0 0 20px;
  flex-grow: 0;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a {
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
  color: #999;
  font-size: 10pt;
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
}

#footer .copyright {
  margin: 0 auto;
}

#home {
  display: block;
  text-align: left;
  flex-grow: 1;
  font-size: 24px;
  line-height: 24px;
}

@media (max-width: 550px) {
  #links {
    flex-direction: column;
  }
  #nav-container {
    display: flex;
  }
  #links a {
    flex-grow: 1;
  }
}

a.logo {
  text-decoration: none;
}

.fade-leave-active {
  position: absolute;
  width: 100%;
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 300ms;
}
.fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
  opacity: 0;
  transition: opacity 300ms cubic-bezier(0.075, 0.82, 0.165, 1);
}
</style>
