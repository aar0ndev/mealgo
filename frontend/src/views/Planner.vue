<template>
    <div class="planner">
        <Calendar v-model="date" :num-weeks=2 />
        <div> {{ date.toLocaleDateString() }} </div>
        <div v-if="meal.length">{{ JSON.stringify(meal) }}</div>
        <div><button>[+] Add Meal</button></div>
    </div>
</template>

<script>
import Calendar from '@/components/Calendar.vue'
export default {
  components: { Calendar },
  data () {
    return {
      date: new Date(),
      meals: [
      ]
    }
  },
  computed: {
    dateString () {
      return this.date && this.date.toISOString().substring(0, 10)
    },
    meal () {
      return this.meals.filter(m => m.date === this.dateString)
    }
  }
}
</script>

<style scoped>
</style>
