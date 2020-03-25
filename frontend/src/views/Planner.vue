<template>
  <div class="planner">
    <Calendar class='cal' v-model="date" :num-weeks="2" />

    <div v-if="searchVisible" class="searchbox">
      <SearchInput style="z-index: 100;"
        :values="allMeals"
        @change="addMeal"
        :focus="true"
        @cancel="searchVisible=false"
      />
    </div>
    <div>
      <span v-if="!(searchVisible || addVisible)">
      <button @click="searchVisible = true">Search Meals</button>
    </span>
    <span v-if="!(searchVisible || addVisible)">
      <button @click="addVisible = true">[+] Add New</button>
    </span>
    <span v-if="addVisible" class="addbox">
      <AddMealInput @change="addNewMeal" :focus="true" @cancel="addVisible=false" />
    </span>
    </div>
    <div v-if="todaysMeals.length" class="day-meal-list">
      <div v-for="meal in todaysMeals" :key="meal.uid || meal.name">
        <div v-if="editMealUid != meal.uid">
          <button class='meal-edit-button' @click="startEditMeal(meal)">{{meal.name}}</button>
        </div>
        <div v-else class='meal-edit-box'>
          <input
            type="text"
            v-model="editMealName"
            @change="editMeal(meal)"
            @blur="editMeal(meal)"
            @keypress.enter="editMeal(meal)"
            :ref="'editMealInput-'+meal.uid"
          />
          <button class='remove-meal-button' @mousedown="removeMeal(meal)" @touchdown="removeMeal(meal)">⌫</button>
        </div>
      </div>
    </div>
    <div v-else class='no-meals'> No meals planned yet. </div>
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
      this.searchVisible = false
      var mealFromServer = await this.$store.addMeal(newMeal)
      this.meals = [...this.meals.filter(m => m.uid !== newMeal.uid), { ...newMeal, ...mealFromServer }]
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

.planner {
    max-width: 1125px;
    margin: 0 auto;
}

.cal {
  margin-bottom: 25px;
}
.no-meals {
  min-height: 100px;
  text-align: center;
}

.remove-meal-button {
  border: none;
  opacity: 0.3;
  transition: opacity 0.5s;
  color: rgb(180,0,0);
  font-weight: bold;
}

.remove-meal-button:hover {
  opacity: 1;
  transition: opacity 0.25s;
}

.meal-edit-box {
  /*min-height: 48px;*/
  /*background: green;*/

}

.meal-edit-button {
  min-width: 300px;
  display: block;
  color: blue;
  text-align: left;
}

.meal-edit-box input {
  font-size: 1.1em;
  margin: 0;
  padding: 0 20px;
  min-height: 48px;
  box-sizing: border-box;
}

.day-meal-list {
  margin: 25px 0;
}

.day-meal-list > div {
  margin: 5px 0;
}
</style>
