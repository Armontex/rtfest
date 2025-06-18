<template>
  <section id="sta">
    <div class="container wrapper sta__wrapper">
      <header class="sta__header">
        <h2 class="sta__title highlight-text">
          Планируйте мероприятия с&nbsp;<span class="highlight-text bold">RTFEST</span>
        </h2>
        <p class="sta__descr">
          Присоединяйтесь к&nbsp;нам и&nbsp;начните организовывать незабываемые события
          с&nbsp;легкостью и&nbsp;удовольствием.
        </p>
      </header>
      <div class="sta__buttons">
        <LightButton text="Начать" />
        <DarkButton text="Узнать больше" href="#faq" />
      </div>
    </div>
  </section>
</template>

<script>
import DarkButton from '../DarkButton.vue'
import LightButton from '../LightButton.vue'

export default {
  components: {
    DarkButton,
    LightButton,
  },
}
</script>

<style></style>

<style scoped>
.sta__wrapper {
  display: flex;
  flex-direction: column;
  gap: 2rem;
  align-items: center;
  text-align: center;
}

.sta__header {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.sta__title {
  font-size: 28px;
}

.sta__descr {
  font-size: 16px;
}

.sta__buttons {
  display: flex;
  gap: 1rem;
}

@media (min-width: 768px) {
  .sta__wrapper {
    align-items: start;
    text-align: start;
  }

  .sta__header {
    width: 60%;
  }
}

@media (min-width: 1024px) {
  .sta__title {
    font-size: 48px;
  }

  .sta__descr {
    font-size: 18px;
  }
}
</style>
