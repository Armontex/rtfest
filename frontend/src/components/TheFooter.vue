<template>
  <div class="container wrapper footer__wrapper">
    <div class="footer__content">
      <div class="footer__header">
        <h4 class="footer__title">Подпишитесь на&nbsp;новости</h4>
        <div class="footer__descr">
          Получайте обновления о&nbsp;наших мероприятиях и&nbsp;акциях.
        </div>
      </div>
      <div class="footer__form">
        <div class="footer__form-wrapper">
          <EmailInput />
          <DarkButton text="Подписаться" />
        </div>
        <p class="footer__form-descr">
          Подписываясь, вы&nbsp;соглашаетесь с&nbsp;нашей Политикой конфиденциальности.
        </p>
      </div>
    </div>
    <hr />
    <hr />
    <div class="footer__under">
      <IconLogo class="footer__logo" />
      <span class="footer__copy">&copy;&nbsp;2025&nbsp;RTFEST. Все права защищены.</span>
    </div>
  </div>
</template>

<script>
import IconLogo from '@/components/icons/IconLogo.vue'
import DarkButton from './DarkButton.vue'
import EmailInput from './EmailInput.vue'

export default {
  components: {
    IconLogo,
    DarkButton,
    EmailInput,
  },
}
</script>

<style scoped>
.footer__wrapper {
  display: flex;
  flex-direction: column;
  gap: 50px;
}

.footer__content {
  display: flex;
  justify-content: space-between;
}

.footer__header {
  display: flex;
  flex-direction: column;
}

.footer__title {
  font-size: 18px;
  font-weight: var(--semi-bold);
}

.footer__form {
  display: flex;
  flex-direction: column;
}

.footer__form-wrapper {
  display: flex;
  gap: 1rem;
  align-items: center;
}

.footer__form-descr {
  font-size: 12px;
}

.footer__under {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.footer__logo {
  height: 80px;
}

.footer__copy {
  font-size: 14px;
}
</style>
