<template>
  <div class="signup">
    <div class="container">
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
        <button type="submit" class="primary">Sign Up</button>
        <div>
          Already a member?
          <router-link to="login">Log In</router-link>
        </div>
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
