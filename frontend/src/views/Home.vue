<template>
  <div class="home">
   <h1>Welcome to MealGo</h1>
   <h3>Plan meals to save money and eat healthy!</h3>
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
       <h2>Easier Shopping</h2>
       <p>Helpful dynamic shopping list can be shared and synced across multiple users</p>
     </div>
     </div>
  </div>
</template>

<script>

export default {
  name: 'home',
}
</script>

<style scoped>
.home {
  max-width: 1200px;
  margin: 0 auto;
}

.boxes{
  display: flex;
  margin: 0 auto;
}
.box {
  flex-grow: 1;
  flex-basis: 0;
  margin: 20px;
  border: 1px solid #888;
  border-radius: 5px;
  padding: 10px;
}

@media (max-width: 650px) {
  .boxes { display: block; }
}
</style>
