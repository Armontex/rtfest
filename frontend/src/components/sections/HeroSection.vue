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
          <LightButton class="hero-btn" text="Узнать больше" href="#faq" />
          <DarkButton class="hero-btn" text="Начать" />
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
  flex-direction: column;
  gap: 50px;
  margin-top: 20px;
}

.hero__content {
  display: flex;
  flex-direction: column;
  gap: 30px;
  font-size: 16px;
}

.hero__title {
  font-size: 30px;
  text-align: center;
}

.hero__buttons {
  display: flex;
  justify-content: space-between;
  gap: 10px;
}

.hero-btn {
  flex: 1;
}

@media (min-width: 768px) {
  .hero__wrapper {
    margin-top: var(--wrapper-margin);
    flex-direction: row;
    align-items: center;
  }

  .hero__title {
    text-align: start;
    font-size: 32px;
  }

  .hero__image {
    width: 50vw;
    height: auto;
  }

  .hero__buttons {
    justify-content: start;
  }

  .hero-btn {
    flex: unset;
  }
}

@media (min-width: 1024px) {
  .hero__title {
    font-size: 42px;
  }

  .hero__descr {
    font-size: 20px;
  }
}

@media (min-width: 1200px) {
  .hero__title {
    font-size: 56px;
  }
}
</style>
