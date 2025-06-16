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
        <LightButton text="Начать"/>
        <DarkButton text="Узнать больше" href="#faq"/>
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
}

.sta__header {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  width: 60%;
}

.sta__title {
  font-size: 48px;
}

.sta__descr {
  font-size: 18px;
}

.sta__buttons {
  display: flex;
  gap: 1rem;
}
</style>
