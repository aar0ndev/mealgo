<template>
  <div class="container" :class="{hide: !$global.waiting}">
    <div class="spinner">
      <div :class="{show: dots[0]}">.</div>
      <div :class="{show: dots[1]}">.</div>
      <div :class="{show: dots[2]}">.</div>
    </div>
  </div>
</template>

<style scoped>
.container {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  pointer-events: none;
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  opacity: 1;
  background: rgba(150, 160, 160, 0.25);
  transition: visibility 1s;
  transition: opacity 1s 1s;
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
}

.hide {
  opacity: 0;
  /*visibility: hidden;*/
  transition: opacity 0.5s;
  transition: visibility 0 0.5;
}

.spinner {
  font-size: 100px;
  display: flex;
  position: relative;
  top: -0.25em;
}

.spinner > div {
  opacity: 0.1;
  text-shadow: 0 0 5px white;
  flex: 0;
}
.spinner > .show {
  opacity: 1;
  color: black;
  color: white;
}
</style>

<script>
export default {
  data() {
    return {
      dots: ""
    };
  },
  watch: {
    "$global.waiting": function() {
      if (!this.interval) {
        this.dots = "";
        this.interval = setInterval(() => {
          this.dots = this.dots === "..." ? "" : this.dots + ".";

          if (!this.$global.waiting) {
            clearInterval(this.interval);
            this.interval = null;
          }
        }, 500);
      }
    }
  }
};
</script>