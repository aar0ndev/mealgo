<template>
  <div class="planner">
    <Calendar v-model="date" :num-weeks="2" />
    <div>{{ date.toLocaleDateString() }}</div>
    <div v-if="todaysMeals.length">
      <div v-for="meal in todaysMeals" :key="meal.uid || meal.name">
        <h3 v-if="editMealUid != meal.uid">
          <span @click="startEditMeal(meal)">{{meal.name}}</span>
          <button @click="removeMeal(meal)">X</button>
        </h3>
        <input
          v-else
          type="text"
          v-model="editMealName"
          @change="editMeal(meal)"
          @blur="editMeal(meal)"
          :ref="'editMealInput-'+meal.uid"
        />
      </div>
    </div>
    <div v-if="!(searchVisible || addVisible)">
      <button @click="searchVisible = true">Search Meals</button>
    </div>
    <div v-if="searchVisible" class="searchbox">
      <SearchInput
        :values="allMeals"
        @change="addMeal"
        :focus="true"
        @cancel="searchVisible=false"
      />
    </div>
    <div v-if="!(searchVisible || addVisible)">
      <button @click="addVisible = true">[+] Add New</button>
    </div>
    <div v-if="addVisible" class="addbox">
      <AddMealInput @change="addNewMeal" :focus="true" @cancel="addVisible=false" />
    </div>
  </div>
</template>

<script>
import Calendar from '@/components/Calendar.vue'
import SearchInput from '@/components/SearchInput.vue'
import AddMealInput from '@/components/AddMealInput.vue'
import { generateID } from '@/util.js'

function getDateInt (date) {
  return (date.getFullYear() * 100 + (date.getMonth() + 1)) * 100 + date.getDate()
}
export default {
  components: { Calendar, SearchInput, AddMealInput },
  data () {
    return {
      date: new Date(),
      meals: [],
      allMeals: [],
      searchVisible: false,
      addVisible: false,
      newMealName: '',
      editMealName: '',
      editMealUid: ''
    }
  },
  computed: {
    dateInt () {
      return this.date && getDateInt(this.date)
    },
    todaysMeals () {
      return this.meals.filter(m => m.planned_date === this.dateInt)
    }
  },
  watch: {
    meals () {
      localStorage.setItem('meals', JSON.stringify(this.meals))
    }
  },
  methods: {
    async addMeal ({ text }) {
      // todo: use current plan id
      var newMeal = { name: text, planned_date: this.dateInt, uid: generateID(), plan_id: 1 }
      this.meals = [...this.meals, newMeal]
      // this.searchVisible = false
      this.$store.addMeal(newMeal)
      // this.meals = [...this.meals.filter(m => m.uid !== meal.uid), { ...meal, ..._meal }]
    },
    addNewMeal (mealName) {
      this.addMeal({ text: mealName })
      this.addVisible = false
    },
    async removeMeal (meal) {
      this.meals = this.meals.filter(m => m.uid !== meal.uid)
      await this.$api.delete('meal', meal.id)
    },
    editMeal (meal) {
      if (this.editMealUid === '') return
      this.editMealUid = ''
      if (meal.name === this.editMealName) return
      meal.name = this.editMealName
      this.meals = [...this.meals]
      this.$api.update('meal', this.mealOrig.id, meal)
    },
    startEditMeal (meal) {
      this.mealOrig = { ...meal }
      this.editMealUid = meal.uid
      this.editMealName = meal.name
      this.$nextTick(() =>
        setTimeout(() => this.$refs['editMealInput-' + meal.uid][0].focus(), 10)
      )
    }
  },
  async mounted () {
    const self = this
    // todo: handle per-user cache
    this.meals = JSON.parse(localStorage.getItem('meals') || '[]')
    if (this.$global.loggedIn || !navigator.onLine) {
      // get actual plan
      // todo: add functionality around multiple plans/users
      try {
        var { meals } = await this.$api.get('plans')
        this.meals = meals.map(m => ({ ...m, uid: m.id + '_' + generateID() }))
      } catch (err) {
        console.log(err)
      }
    }

    // get dummy info
    fetch('/data/meals.json')
      .then(res => (res.ok ? res.json() : { meals: [] }))
      .then(data => {
        self.allMeals = data.meals
      })
  }
}
</script>

<style scoped>
.searchbox,
.addbox {
  max-width: 400px;
}
</style>
