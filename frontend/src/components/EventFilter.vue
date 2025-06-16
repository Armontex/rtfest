<script>
import IconFilter2 from './icons/IconFilter2.vue'
import CheckBox from './CheckBox.vue'
import Calendar from './Calendar.vue'

export default {
  components: {
    IconFilter2,
    CheckBox,
    Calendar,
  },
  data() {
    return {
      selectedCategories: {
        all: true,
        cinema: false,
        quizzes: false,
        pcGames: false,
        quests: false,
        mClasses: false,
        music: false,
        puzzles: false,
        picnics: false,
        sport: false,
        dancing: false,
        stendup: false,
        festivals: false,
      },
    }
  },
}
</script>

<template>
  <div class="event-filter">
    <h1 class="event-filter__title">Мероприятия</h1>
    <div class="event-filter__types">
      <div class="event-filter__types-header">
        <IconFilter2 class="icon-filter"/>
        <h2 class="event-filter__types-title">Категории мероприятий</h2>
      </div>
      <div class="event-filter__types-checkboxes">
        <CheckBox name="all" text="Все" v-model="selectedCategories.all"/>
        <CheckBox name="cinema" text="Кино" v-model="selectedCategories.cinema"/>
        <CheckBox name="quizzes" text="Викторины" v-model="selectedCategories.quizzes"/>
        <CheckBox name="pc-games" text="Компьютерные игры" v-model="selectedCategories.pcGames"/>
        <CheckBox name="quests" text="Квесты" v-model="selectedCategories.quests"/>
        <CheckBox name="m-classes" text="Мастер-классы" v-model="selectedCategories.mClasses"/>
        <CheckBox name="music" text="Музыка" v-model="selectedCategories.music"/>
        <CheckBox name="puzzles" text="Настолки" v-model="selectedCategories.puzzles"/>
        <CheckBox name="picnics" text="Пикники" v-model="selectedCategories.picnics"/>
        <CheckBox name="sport" text="Спорт" v-model="selectedCategories.sport"/>
        <CheckBox name="dancing" text="Танцы" v-model="selectedCategories.dancing"/>
        <CheckBox name="stendup" text="Стендап-вечера" v-model="selectedCategories.stendup"/>
        <CheckBox name="festivals" text="Фестивали" v-model="selectedCategories.festivals"/>
      </div>
    </div>
    <Calendar class="event-filter__calendar" />
  </div>
</template>

<style></style>

<style scoped>
.event-filter {
  display: flex;
  flex-direction: column;
  align-items: center;
  border-radius: 42px;
  padding: 19px 26px;
  width: 366px;
  height: 941px;
  background: #f1f1f1;
}

.event-filter__title {
  font-family: var(--title-font-family);
  font-weight: 700;
  font-size: 32px;
  line-height: 150%;
  color: #000;
}

.event-filter__types {
  border-radius: 17px;
  width: 274px;
  /* height: 426px; */
  height: max-content;
  background: #65b1da;
  padding: 10px;
}

.event-filter__types-title {
  font-family: var(--title-font-family);
  font-weight: 700;
  font-size: 14px;
  color: #fff;
  font-size: 14px;
}

.event-filter__types-header {
  display: flex;
  align-items: center;
  gap: 10px;
}

.event-filter__types-checkboxes {
  margin-left: 15%;
  display: flex;
  flex-direction: column;
}

.event-filter__calendar {
  margin-top: 40px;
}

.icon-filter {

}
</style>
