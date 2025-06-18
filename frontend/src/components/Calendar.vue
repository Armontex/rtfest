<template>
  <div class="calendar">
    <div class="header">
      <div class="header__content">
        <button @click="prevMonth">
          <IconArrow direction="left" fill="#fff"/>
        </button>
        <h2>{{ monthYear }}</h2>
        <button @click="nextMonth">
          <IconArrow direction="right" fill="#fff" />
        </button>
      </div>
      <div class="day-names">
        <div v-for="day in dayNames" :key="day" class="day-name">{{ day }}</div>
      </div>
    </div>
    <div class="days">
      <div v-for="emptyDay in emptyDays" :key="'empty-' + emptyDay" class="day empty">
        {{ emptyDay }}
      </div>
      <div v-for="day in daysInMonth" :key="day" class="day" :class="{ today: isToday(day) }">
        {{ day }}
      </div>
    </div>
  </div>
</template>
<style scoped></style>

<script>
import IconArrow from './icons/IconArrow.vue'
export default {
  components: {
    IconArrow,
  },
  data() {
    return {
      currentDate: new Date(),
      dayNames: ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс'],
    }
  },
  computed: {
    monthYear() {
      return this.currentDate.toLocaleString('default', {
        month: 'long',
        year: 'numeric',
      })
    },
    firstDayOfMonth() {
      return new Date(this.currentDate.getFullYear(), this.currentDate.getMonth(), 1)
    },
    lastDayOfMonth() {
      return new Date(this.currentDate.getFullYear(), this.currentDate.getMonth() + 1, 0)
    },
    // emptyDays() {
    //   // Возвращаем массив пустых дней для отступов
    //   const firstDayIndex = this.firstDayOfMonth.getDay() || 7 // Воскресенье = 0 -> 7
    //   return Array.from({ length: firstDayIndex - 1 }, (_, i) => i)
    // },
     emptyDays() {
      const firstDayIndex = this.firstDayOfMonth.getDay() || 7; // Воскресенье = 0 -> 7
      if (firstDayIndex === 1) return []; // Если месяц начинается с понедельника - пустых дней нет

      const prevMonthLastDay = new Date(
        this.currentDate.getFullYear(),
        this.currentDate.getMonth(),
        0
      ).getDate();

      // Возвращаем последние (firstDayIndex - 1) дней предыдущего месяца
      const startDay = prevMonthLastDay - (firstDayIndex - 2);
      return Array.from({ length: firstDayIndex - 1 }, (_, i) => startDay + i);
    },
    daysInMonth() {
      return Array.from({ length: this.lastDayOfMonth.getDate() }, (_, i) => i + 1)
    },
  },
  methods: {
    isToday(day) {
      const today = new Date()
      return (
        day === today.getDate() &&
        this.currentDate.getMonth() === today.getMonth() &&
        this.currentDate.getFullYear() === today.getFullYear()
      )
    },
    prevMonth() {
      this.currentDate = new Date(
        this.currentDate.getFullYear(),
        this.currentDate.getMonth() - 1,
        1,
      )
    },
    nextMonth() {
      this.currentDate = new Date(
        this.currentDate.getFullYear(),
        this.currentDate.getMonth() + 1,
        1,
      )
    },
  },
}
</script>

<style scoped>
.calendar {
  font-family: var(--title-font-family);
  font-size: 11px;
  overflow: hidden;
  background: #fff;
  border-radius: 10px;
  width: 100%;
}

.header {
  display: flex;
  flex-direction: column;
}

.header__content {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 8px;
  background: #a9d4ea;
  color: #fff;
}

.day-names {
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  gap: 5px;
  background: #86a8ba;
  padding: 8px;
}

.day-name {
  font-family: var(--font-4);
  text-align: center;
  padding: 5px;
  color: #fff8f8;
}

h2 {
  font-size: 11px;
  background: #65b2da;
  padding: 2px 8px;
  border-radius: 4px;
}

.header button {
  background: transparent;
  border: none;
  color: white;
  font-size: 16px;
  cursor: pointer;
  padding: 5px 10px;
}

.days {
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  gap: 5px;
  padding: 8px;
}

.day {
  font-family: var(--font-4);
  font-weight: bold;
  color: #000;
  text-align: center;
  padding: 5px;
  cursor: pointer;
  border-radius: 4px;
}
.day.today {
  background: #65b2da;
  color: white;
}

.day.empty {
  color: #ccc;
  /* background: transparent; */
  /* cursor: default; */
}
</style>
