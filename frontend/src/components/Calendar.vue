<template>
  <div class="container">

  <div class="controls">
    <button @click="changeWeek(null)" :disabled="sameDate(selected,today)">Today</button>
    <button class='weekchange' @click="changeWeek(-1)">▲</button><button class='weekchange' @click="changeWeek(1)">▼</button>
    <div class="datestring">{{ selected.toLocaleDateString('default', {month: 'long', day: 'numeric', year: 'numeric'}) }}</div>
  </div>

  <div class="calendar">
    <div class="header">
      <div v-for="day in 'Su Mo Tu We Th Fr Sa'.split(' ')" :key="day" class="day">{{day[0]}}</div>
    </div>
    <transition-group name="fade" class="week" tag="div">

      <a v-for="day in days" :key="day.toString()" @click="change(day)">

        <div class="day" :class="{today: isToday(day), selected: isSelected(day)}">
          <span v-if="day.getDate() == 1" style="position: absolute; left: 10px; top: -10px; font-size: 14px">{{day.toLocaleDateString('default', {month: 'long'})}}</span>
          {{day.getDate()}}</div>
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
  watch: {
    selected () {
      this.$emit('input', this.selected)
    }
  },
  methods: {
    isToday (date) {
      return !!this.today && this.today.getDate() === date.getDate() &&
      this.today.getMonth() === date.getMonth() &&
      this.today.getFullYear() === date.getFullYear()
    },
    isSelected (date) {
      // return !!this.selected && this.selected.getDate() === date.getDate() &&
      // this.selected.getMonth() === date.getMonth() &&
      // this.selected.getFullYear() === date.getFullYear()
      return this.sameDate(date, this.selected)
    },
    sameDate (date1, date2) {
      return date1.getFullYear() == date2.getFullYear() && date1.getMonth() == date2.getMonth() && date1.getDate() == date2.getDate()
    },
    changeWeek (num) {
      if (num == null) {
        this.start = start
        this.selected = today
      } else {
        this.start = new Date(this.start.getFullYear(), this.start.getMonth(), this.start.getDate() + num * 7)
        this.selected = new Date(this.selected.getFullYear(), this.selected.getMonth(), this.selected.getDate() + num * 7)
      }
    },
    change (date) {
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
  position: relative;
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
  position: relative;
  text-align: right;
  xtop: -48px;
  xright: 0;
}

.datestring {
  position: absolute;
  left: 0;
  bottom: 0;
  font-size: 14pt;
  min-height: 48px;
  line-height: 48px;
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
