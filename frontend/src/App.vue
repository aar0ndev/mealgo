<template>
  <div id="app" :class="{home: !$global.loggedIn}">
    <header id="nav">
      <div id="nav-container">
        <span id="home">
          <div class="debug" v-if="$global.NODE_ENV == 'development'">
            loggedIn
            <input type="checkbox" v-model="$global.loggedIn" />
            waiting
            <input type="checkbox" v-model="$global.waiting" />
          </div>
          <router-link to="/" class="logo">MealGo</router-link>
        </span>
        <span id="links" :class="{linksExpanded}">
          <HamburgerButton @click.native="toggleLinks" class="linkToggle" @blur.native="linkToggleBlur">
          </HamburgerButton>
          <template v-if="$global.loggedIn">
            <router-link to="/planner">Planner</router-link>
            <router-link to="/recipes">Recipes</router-link>
            <router-link to="/shopping">Shopping List</router-link>
            <router-link to="/login">
              <span @click="logout">Log Out</span>
            </router-link>
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
      <div class="copyright">
        &copy; 2019
        <a href="//theaaron.dev">theaaron.dev</a>
      </div>
    </footer>
    <WaitingSpinner />
  </div>
</template>

<script>
import WaitingSpinner from '@/components/WaitingSpinner.vue'
import HamburgerButton from '@/components/HamburgerButton.vue'

export default {
  components: {
    HamburgerButton,
    WaitingSpinner
  },
  data () {
    return {
      linksExpanded: false
    }
  },
  methods: {
    logout () {
      this.$api.logout()
    },
    toggleLinks () {
      this.linksExpanded = !this.linksExpanded
    },
    linkToggleBlur () {
      this.$nextTick(setTimeout(() => { this.linksExpanded = false }, 200))
    }
  }
}
</script>

<style>
* {
  box-sizing: border-box;
}

html {
  overflow-y: scroll;
  cursor: default;
}

html,
body {
  margin: 0;
  padding: 0;
  min-height: 100vh;
  background: #fff;
}

#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
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
  padding: 0 20px;
  flex-grow: 0;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a {
  padding-left: 20px;
  padding-right: 20px;
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

button,
.primary {
  min-width: 48px;
  min-height: 48px;
  padding: 5px 20px;
  border-radius: 5px;
  font-size: 1.1em;
  border: 1px solid black;
  background: white;
}

.primary {
  color: #dff;
  background: rgb(2, 141, 141);
  border: 2px solid rgb(100, 141, 141);
  text-decoration: none;
  font-size: 24px;
  font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
}

#footer,
#footer a {
  color: #999;
}

#footer {
  text-align: left;
  padding: 20px;
  min-height: 200px;
  background: #222;

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
  position: relative;
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
  transition: opacity 200ms;
}

label > input {
  xoutline: 1px solid red;
  margin: 10px 0 30px 0;
  font-size: 1em;
  width: 100%;
  border-radius: 5px;
  padding: 6px;
}

a {
  text-decoration: none;
}

a:hover {
  text-decoration: underline;
}
.debug {
  position: absolute;
  left: 20px;
  top: 50px;
  font-size: 15px;
  line-height: 1em;
  z-index: 20;
}

.linkToggle {
  display: none;
}

@media only screen and (max-width: 750px) {
  .linkToggle {
    display: unset;
  }

  #links a {
    display: none;
  }

  #links.linksExpanded {
    position: fixed;
    z-index: 100;
    background: white;
    left: 0;
    top: 0;
    width: 100vw;
  box-shadow: 0 3px 10px -6px black;
  }

  #links.linksExpanded a {
    display: block;
  }

  #links.linksExpanded .linkToggle {
    position: fixed;
    right: 20px;
    top: 0px;
  }
}
</style>
