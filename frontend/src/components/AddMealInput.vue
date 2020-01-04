<template>
    <div class="container">
        <input class="input" type="text" v-model="value" placeholder="Enter New Meal Name" ref="input" @change="sendResult" @blur="onBlur">
    </div>
</template>

<script>
export default {
  props: {
    focus: { type: Boolean, default: false }
  },
  data () {
    return {
      value: ''
    }
  },
  methods: {
    focusInput () {
      this.$refs.input.focus()
    },
    sendResult () {
      this.$emit('change', this.value)
    },
    onBlur () {
      this.$emit('cancel')
    }
  },
  mounted () {
    if (this.focus) this.focusInput()
  }
}
</script>

<style scoped>
    .container {
        position: relative;
    }

    .input {
        width: 100%;
    }
</style>
