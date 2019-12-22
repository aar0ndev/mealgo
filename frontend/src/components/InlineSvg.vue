<template>
    <div class="inline-svg" v-html="src" ref="container"/>
</template>

<script>
export default {
  props: {
    src: { type: String, required: true },
    preserveAspectRatio: { type: String, default: '' }
  },
  mounted () {
    var container = this.$refs.container
    if (container) {
      container.children[0].setAttribute('preserveAspectRatio', this.preserveAspectRatio)
    }
  }
}
</script>

<style>
.inline-svg > svg {
    width: 100%;
    height: 100%;
}
</style>
