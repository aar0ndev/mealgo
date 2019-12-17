<template>
<div class='login'>
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
    <button type="submit">Log In</button>
    <br />
    <a href="/planner">Use as Guest</a>
    <br />
  </form>
  </div>
</template>

<style scoped>
  .login {
    max-width: 1200px;
    margin: 0 auto;
    padding-left: 20px;
  }
</style>