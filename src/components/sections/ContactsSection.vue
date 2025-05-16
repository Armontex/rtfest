<template>
  <section id="contacts">
    <div class="container wrapper contacts__wrapper">
      <h2 class="contacts__title">Все еще есть вопросы?</h2>
      <p class="contacts__desct highlight-text">Свяжитесь с&nbsp;нашей поддержкой!</p>
      <DarkButton text="Контакт" />
    </div>
  </section>
</template>

<script>
import DarkButton from '../DarkButton.vue'
export default {
  components: {
    DarkButton,
  },
}
</script>

<style></style>

<style scoped>
.contacts__wrapper {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1.5rem;
}

.contacts__title {
  font-size: 32px;
}

.contacts__desct {
   font-size: 18px;
}
</style>
