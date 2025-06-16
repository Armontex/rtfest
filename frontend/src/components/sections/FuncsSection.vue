<template>
  <section id="funcs">
    <div class="container wrapper funcs__wrapper">
      <header class="funcs__header">
        <h2 class="funcs__title">Ключевые возможности платформы</h2>
        <p class="funcs__descr">
          <span class="bold">RTFEST</span> предлагает удобные инструменты для организации
          мероприятий. Мы&nbsp;помогаем сделать процесс планирования простым и&nbsp;приятным.
        </p>
      </header>
      <div class="funcs__cards">
        <div class="funcs__card">
          <div class="crap-wrapper funcs__card-media">
            <img
              src="/src/assets/images/funcs-p1.png"
              alt=""
              class="crap-image funcs__card-image"
            />
          </div>
          <h3 class="funcs__card-title">Удобный интерфейс и&nbsp;минималистичный дизайн</h3>
          <p class="funcs__card-descr">Легкость в&nbsp;управлении и&nbsp;планировании событий.</p>
        </div>
        <div class="funcs__card">
          <div class="crap-wrapper funcs__card-media">
            <img
              src="/src/assets/images/funcs-p2.png"
              alt=""
              class="crap-image funcs__card-image"
            />
          </div>
          <h3 class="funcs__card-title">Интерактивные функции для участников мероприятий</h3>
          <p class="funcs__card-descr">
            Участники могут легко находить и&nbsp;присоединяться к&nbsp;событиям.
          </p>
        </div>
      </div>
      <div class="funcs__buttons">
        <DarkButton text="Узнать" href="#faq" />
        <ArrowButton text="Записаться" />
      </div>
    </div>
  </section>
</template>

<script>
import DarkButton from '../DarkButton.vue'
import ArrowButton from '../ArrowButton.vue'
export default {
  components: {
    DarkButton,
    ArrowButton,
  },
}
</script>

<style scoped>
.funcs__wrapper {
  display: flex;
  flex-direction: column;
  gap: clamp(20px, 15vh, 80px);
  align-items: center;
}

.funcs__header {
  display: flex;
  flex-direction: column;
  text-align: center;
  gap: 1.5rem;
  width: 60%;
}

.funcs__title {
  font-size: 48px;
}

.funcs__cards {
  display: flex;
  gap: 2rem;
}

.funcs__card {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
  align-items: center;
  text-align: center;
}

.funcs__card-title {
  font-size: 32px;
}

.funcs__buttons {
  display: flex;
  gap: 0.5rem;
}
</style>
