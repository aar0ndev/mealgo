<template>
  <div class="home">
    <div class="banner">
      <div class="container">
        <div class="img"></div>
        <h1>Plan meals to save money and eat healthy</h1>
      </div>
    </div>
    <div class="boxes">
      <div class="box">
        <h2>Save money</h2>
        <p>Buy less, spend less, save more! Have less food waste!</p>
      </div>
      <div class="box">
        <h2>Eat healthy</h2>
        <p>Planning meals leads to eating better since you are more in control of you diet</p>
      </div>
      <div class="box">
        <h2>Shop Easier</h2>
        <p>Helpful dynamic shopping list can be shared and synced across multiple users</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'home'
}
</script>

<style scoped>
.home {
  color: #444;
}

.banner {
  background: linear-gradient(#dff -10%, #cff 100%);
}

.banner .container {
  display: flex;
  max-width: 1200px;
  min-height: 300px;
  margin: 0 auto;
}

.banner .img {
  flex-grow: 1;
  flex-basis: 1;
  flex-shrink: 1;
  width: 50%;
  background: url(../assets/quick-cart.svg);
  xoutline: 1px solid gray;
  background-repeat: no-repeat;
  background-origin: 50% 50%;
  background-position: 50% 50%;
  background-size: contain;
}

.banner h1 {
  display: inline-block;
  width: 50%;
  flex-grow: 1;
  flex-basis: 1;
  flex-shrink: 1;
  padding: 50px;
  font-size: 50px;
  font-weight: 300;
  margin: auto;
}

@media (max-width: 900px) {
  .banner h1 {
    font-size: 30px;
  }
}

@media (max-width: 550px) {
  .banner .container {
    flex-direction: column-reverse;
  }
  .banner h1,
  .banner .img {
    width: 100%;
  }
  .banner .img {
    min-height: 250px;
  }
}

.boxes {
  display: flex;
  max-width: 1200px;
  margin: 50px auto;
}
.box {
  flex-grow: 1;
  flex-basis: 0;
  margin: 20px;
  border: 1px solid #ccc;
  border-radius: 5px;
  padding: 10px;
  box-shadow: 0 3px 10px #bbb;
  font-size: 11pt;
}

@media (max-width: 650px) {
  .boxes {
    display: block;
  }
}
</style>
