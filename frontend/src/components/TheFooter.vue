<template>
  <div class="container wrapper footer__wrapper">
    <div class="footer__content">
      <div class="footer__header">
        <h4 class="footer__title">Подпишитесь на&nbsp;новости</h4>
        <p class="footer__descr">
          Получайте обновления о&nbsp;наших мероприятиях и&nbsp;акциях.
        </p>
      </div>
      <div class="footer__form">
        <div class="footer__form-wrapper">
          <EmailInput class="email-input" />
          <DarkButton class="form-btn" text="Подписаться" />
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

  gap: 1.5rem;

  font-family: var(--second-family);
}

.footer__content {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.footer__header {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.footer__title {
  font-size: 18px;
  font-weight: var(--semi-bold);
}

.footer__descr {
  font-size: 16px;
}

.footer__form {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.footer__form-wrapper {
  display: flex;
  gap: 10px;
}

.email-input {
  flex: 1;
}

.form-btn {
  flex: 1;
}

.footer__under {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.footer__logo {
  height: 40px;
  width: 40px;
}

.footer__copy {
  font-size: 14px;
}

@media (min-width: 768px) {
  .footer__wrapper {
    gap: 3rem;
  }
  .footer__content {
    flex-direction: row;
    justify-content: space-between;
  }

  .footer__form {
    font-size: 16px;
    gap: 5px;
  }

  .footer__form-descr {
    font-size: 12px;
  }

  .footer__under {
    flex-direction: row;
    align-items: center;
    justify-content: space-between;
  }

  .footer__logo {
    height: 70px;
    width: 70px;
  }
}
</style>
