<template>
  <div class="login">
    <div class="container">
      <h1>Log In</h1>
      <form action="/api/login?redirect=/login" method="POST">
        <label for="username">
          Email
          <br />
          <input id="username" name="username" type="text" />
        </label>
        <br />
        <label for="password">
          Password
          <br />
          <input id="password" name="password" type="password" />
        </label>
        <br />
        <button class="primary" type="submit">Log In</button>
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
