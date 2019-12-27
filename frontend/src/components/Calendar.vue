<template>
  <div class="container">
  <div class="controls">
    <button class='weekchange' @click="changeWeek(-1)">▲</button><button class='weekchange' @click="changeWeek(1)">▼</button>
  </div>
  <div class="calendar">
    <div class="header">
      <div v-for="day in 'Su Mo Tu We Th Fr Sa'.split(' ')" :key="day" class="day">{{day[0]}}</div>
    </div>
    <transition-group name="fade" class="week" tag="div">

      <a v-for="day in days" :key="day.toString()" @click="change(day)">

        <div class="day" :class="{today: isToday(day), selected: isSelected(day)}">{{day.getDate()}}</div>
      </a>

    </transition-group>
    </div>
  </div>
</template>

<script>
const now = new Date()
const today = new Date(now.getFullYear(), now.getMonth(), now.getDate())
const start = new Date(today.getFullYear(), today.getMonth(), today.getDate() - today.getDay())
export default {
  name: 'Calendar',
  props: ['value', 'numWeeks'],
  data () {
    return {
      today,
      start,
      selected: this.value
    }
  },
  computed: {
    days () {
      const darr = []
      let d = new Date(this.start)
      while (darr.length < this.numWeeks * 7) {
        darr.push(d)
        d = new Date(d.getFullYear(), d.getMonth(), d.getDate() + 1)
      }
      return darr
    }
  },
  methods: {
    isToday (date) {
      return !!this.today && this.today.getDate() == date.getDate() &&
      this.today.getMonth() == date.getMonth() &&
      this.today.getFullYear() == date.getFullYear()
    },
    isSelected (date) {
      return !!this.selected && this.selected.getDate() == date.getDate() &&
      this.selected.getMonth() == date.getMonth() &&
      this.selected.getFullYear() == date.getFullYear()
    },
    changeWeek (num) {
      this.start = new Date(this.start.getFullYear(), this.start.getMonth(), this.start.getDate() + num * 7)
    },
    change (date) {
      this.$emit('input', date)
      this.selected = date
    }
  }
}
</script>

<style scoped>
.calendar {
  font-size: 20pt;
  text-align: right;
  user-select: none;
}

.header,
.week {
  display: grid;
  grid-template-columns: repeat(7, 1fr);
}

.header {
  color: #ddd;
  background: #aaa;
}

.day {
  border: 1px solid #eee;
  padding: 5px;
  cursor: pointer;
}

.week .day:hover {
  background: white;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
  border: 1px solid white;
}

.today {
  background: #DDE;
}

.selected, .day.selected:hover {
  border-color: blue;
}

.container {
  position: relative;
}

.weekchange {
  color: #999;
}

.controls {
  xposition: absolute;
  text-align: right;
  xtop: -48px;
  xright: 0;
}

.controls button {
  border: none;
}

.fade-enter-active {
  transition: opacity 300ms;
}
.fade-leave-active {
  display: none;
}

.fade-enter {
  opacity: 0;
}
</style>
