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
        victorins: false,
        computer_games: false,
        quests: false,
        master_class: false,
        music: false,
        board_games: false,
        picnics: false,
        sport: false,
        dances: false,
        stendup: false,
        festivals: false,
      },
    }
  },
  methods: {
    handleCategoryChange(category, value) {
      if (category !== 'all' && value) {
        this.selectedCategories.all = false;
      }
      if (category === 'all' && value) {
        Object.keys(this.selectedCategories).forEach((key) => {
          if (key !== 'all') {
            this.selectedCategories[key] = false;
          }
        })
      }
      
      const hasActiveFilters = Object.keys(this.selectedCategories)
        .some(key => key !== 'all' && this.selectedCategories[key]);

      if (!hasActiveFilters) {
        this.selectedCategories.all = true;
      }
      this.$emit('filter-change', this.selectedCategories);
    },
  },
  emits: ['filter-change']
}
</script>

<template>
  <div class="event-filter">
    <h1 class="event-filter__title">Мероприятия</h1>
    <div class="event-filter__types">
      <div class="event-filter__types-header">
        <IconFilter2 class="icon-filter" />
        <h2 class="event-filter__types-title">Категории мероприятий</h2>
      </div>
      <div class="event-filter__types-checkboxes">
        <CheckBox
          name="all"
          text="Все"
          v-model="selectedCategories.all"
          @change="(val) => handleCategoryChange('all', val)"
        />
        <CheckBox
          name="cinema"
          text="Кино"
          v-model="selectedCategories.cinema"
          @change="(val) => handleCategoryChange('cinema', val)"
        />
        <CheckBox
          name="victorins"
          text="Викторины"
          v-model="selectedCategories.victorins"
          @change="(val) => handleCategoryChange('victorins', val)"
        />
        <CheckBox
          name="computer_games"
          text="Компьютерные игры"
          v-model="selectedCategories.computer_games"
          @change="(val) => handleCategoryChange('computer_games', val)"
        />
        <CheckBox
          name="quests"
          text="Квесты"
          v-model="selectedCategories.quests"
          @change="(val) => handleCategoryChange('quests', val)"
        />
        <CheckBox
          name="master_class"
          text="Мастер-классы"
          v-model="selectedCategories.master_class"
          @change="(val) => handleCategoryChange('master_class', val)"
        />
        <CheckBox
          name="music"
          text="Музыка"
          v-model="selectedCategories.music"
          @change="(val) => handleCategoryChange('music', val)"
        />
        <CheckBox
          name="board_games"
          text="Настолки"
          v-model="selectedCategories.board_games"
          @change="(val) => handleCategoryChange('board_games', val)"
        />
        <CheckBox
          name="picnics"
          text="Пикники"
          v-model="selectedCategories.picnics"
          @change="(val) => handleCategoryChange('picnics', val)"
        />
        <CheckBox
          name="sport"
          text="Спорт"
          v-model="selectedCategories.sport"
          @change="(val) => handleCategoryChange('sport', val)"
        />
        <CheckBox
          name="dances"
          text="Танцы"
          v-model="selectedCategories.dances"
          @change="(val) => handleCategoryChange('dances', val)"
        />
        <CheckBox
          name="stendup"
          text="Стендап-вечера"
          v-model="selectedCategories.stendup"
          @change="(val) => handleCategoryChange('stendup', val)"
        />
        <CheckBox
          name="festivals"
          text="Фестивали"
          v-model="selectedCategories.festivals"
          @change="(val) => handleCategoryChange('festivals', val)"
        />
      </div>
    </div>
    <Calendar class="event-filter__calendar" />
  </div>
</template>

<style scoped>
.event-filter {
  display: flex;
  flex-direction: column;
  align-items: center;
  border-radius: 42px;
  padding: 19px 26px;
  width: 320px;
  height: 800px;
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
</style>
