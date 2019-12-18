<template>
  <div class="signup">
    <h1>Sign Up</h1>
    <form action="/api/login?redirect=/login" method="POST">
      <label for="username">
        Email
        <br />
        <input id="username" name="username" type="text" />
      </label>
      <br />
      <label for="password">
        Enter Password
        <br />
        <input id="password" name="password" type="password" />
      </label>
      <br />
      <label for="password2">
        Re-Enter Password
        <br />
        <input id="password2" name="password2" type="password" />
      </label>
      <br />
      <p>
        Already a member?
        <router-link to="login">Log In</router-link>instead.
      </p>
      <a href="/planner">Use as Guest</a>
      <br />
    </form>
  </div>
</template>

<style scoped>
.signup {
  max-width: 1200px;
  margin: 0 auto;
  padding-left: 20px;
}
</style>
