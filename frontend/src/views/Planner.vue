<template>
  <div class="planner">
    <Calendar v-model="date" :num-weeks="2" />
    <div>{{ date.toLocaleDateString() }}</div>
    <div v-if="todaysMeals.length">
      <div v-for="meal in todaysMeals" :key="meal.uid || meal.text">
        <h3 v-if="editMealUid != meal.uid">
          <span @click="startEditMeal(meal)">{{meal.text}}</span>
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
    dateString () {
      return this.date && this.date.toISOString().substring(0, 10)
    },
    todaysMeals () {
      return this.meals.filter(m => m.date === this.dateString)
    }
  },
  watch: {
    meals () {
      localStorage.setItem('meals', JSON.stringify(this.meals))
    }
  },
  methods: {
    addMeal (meal) {
      var newMeal = { ...meal, date: this.dateString, uid: generateID() }
      this.meals = [...this.meals, newMeal]
      this.searchVisible = false
    },
    addNewMeal (mealName) {
      this.addMeal({ text: mealName })
      this.addVisible = false
    },
    removeMeal (meal) {
      this.meals = this.meals.filter(m => m.uid !== meal.uid)
    },
    editMeal (meal) {
      if (this.editMealUid === '') return
      this.editMealUid = ''
      if (meal.text === this.editMealName) return
      meal.text = this.editMealName
      this.meals = [...this.meals]
    },
    startEditMeal (meal) {
      this.editMealUid = meal.uid
      this.editMealName = meal.text
      this.$nextTick(() =>
        setTimeout(() => this.$refs['editMealInput-' + meal.uid][0].focus(), 10)
      )
    }
  },
  async mounted () {
    const self = this
    if (this.$global.loggedIn) {
      // get actual plan
      // todo: add functionality around multiple plans
      var { meals } = await this.$api.get('plans')
      this.meals = meals
    } else {
      // get dummy info
      fetch('/data/meals.json')
        .then(res => (res.ok ? res.json() : { meals: [] }))
        .then(data => {
          self.allMeals = data.meals
        })
      this.meals = JSON.parse(localStorage.getItem('meals') || '[]')
    }
  }
}
</script>

<style scoped>
.searchbox,
.addbox {
  max-width: 400px;
}
</style>
