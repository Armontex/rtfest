<template>
  <section id="hero">
    <div class="container wrapper hero__wrapper">
      <div class="hero__content">
        <h1 class="hero__title">
          Организуйте незабываемые события с&nbsp;<span class="highlight-text bold">RTFEST</span>
        </h1>
        <p class="hero__descr">
          <span class="bold">RTFEST</span>&nbsp;&mdash; это ваш надежный помощник в&nbsp;организации
          мероприятий. Легко планируйте вечеринки, квесты и&nbsp;другие события с&nbsp;нашей
          интуитивно понятной платформой.
        </p>
        <div class="hero__buttons">
          <DarkButton text="Узнать больше" href="#faq" />
          <LightButton text="Начать" />
        </div>
      </div>
      <img :src="HeroImage" alt="" class="hero__image" />
    </div>
  </section>
</template>

<script>
import HeroImage from '@/assets/images/hero.png'
import DarkButton from '../DarkButton.vue'
import LightButton from '../LightButton.vue'
export default {
  components: {
    DarkButton,
    LightButton,
  },
  data() {
    return {
      HeroImage,
    }
  },
}
</script>

<style></style>

<style scoped>
.hero__wrapper {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.hero__content {
  display: flex;
  flex-direction: column;
  gap: 1.5em;
}

.hero__descr {
  font-size: 20px;
}

/* .hero__media {
  width: 100%;
  height: 640px;
} */
 
.hero__buttons {
  display: flex;
  gap: 1rem;
}

/* .hero__image {
  border-radius: 55px;
  min-width: 767px;
  height: 640px;
} */
</style>
