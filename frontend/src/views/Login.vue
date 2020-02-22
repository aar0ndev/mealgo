<template>
  <div class="login">
    <div class="container">
      <h1>Log In</h1>
      <form action="/api/login?redirect=/login" method="POST">
        <label for="username">
          Email
          <br />
          <input v-model="email" id="email" name="email" type="text" />
        </label>
        <br />
        <label for="password">
          Password
          <br />
          <input v-model="pass" id="password" name="password" type="password" />
        </label>
        <br />
        <button class="primary" @click="login" type="submit">Log In</button>
        <br />
        <router-link to="planner">Use as Guest</router-link>
        <br />
      </form>
    </div>
  </div>
</template>

<style scoped>
.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 40px;
}

form {
  max-width: 500px;
}
</style>

<script>
export default {
  data() {
    return {
      email: "",
      pass: ""
    };
  },
  methods: {
    async login(ev) {
      ev.preventDefault();
      try {
        await this.$api.login(this.email, this.pass);
        this.$global.loggedIn = true;
        this.$router.push("planner");
      } catch (err) {
        // if 401 error, say something like wrong password
        // if other error, say so
        console.log(err);
        if (err.message.includes("UNAUTHORIZED")) {
          window.alert("Incorrect username or password. Please try again.");
        } else {
          window.alert("Error logging in, please try again later.");
        }
      }
    }
  }
};
</script>
