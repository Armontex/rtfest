<template>
  <section id="faq">
    <div class="container wrapper faq__wrapper">
      <header class="faq__header">
        <h2 class="faq__title highlight-text">Часто задаваемые вопросы</h2>
        <p class="faq__descr">
          Здесь вы&nbsp;найдете ответы на&nbsp;самые распространенные вопросы о&nbsp;платформе
          <span class="bold">RTFEST</span>.
        </p>
      </header>
      <div class="faq__content">
        <Dropdown title="Что такое RTFEST?">
          <p class="dropdown-descr">
            RTFEST&nbsp;&mdash; это платформа для организации мероприятий. Она помогает
            пользователям планировать и&nbsp;проводить различные события. Мы&nbsp;предлагаем удобные
            инструменты для организаторов и&nbsp;участников.
          </p>
        </Dropdown>
        <Dropdown title="Как зарегистрироваться на платформе?">
          <p class="dropdown-descr">
            Для пользования сайтом вам не&nbsp;нужно регистрироваться, просто заполните анкету,
            когда выберете интересующее вас мероприятие.
          </p>
        </Dropdown>
        <Dropdown title="Как связаться с&nbsp;поддержкой?">
          <p class="dropdown-descr">
            Вы&nbsp;можете обратиться в&nbsp;службу поддержки через раздел &rsquo;Контакты&rsquo;.
            Мы&nbsp;готовы ответить на&nbsp;ваши вопросы и&nbsp;помочь с&nbsp;любыми проблемами.
            Наша команда работает круглосуточно.
          </p>
        </Dropdown>
        <Dropdown title="Какие мероприятия вас ждут?">
          <p class="dropdown-descr">
            Вас ждут фестивали, квесты, вечеринки и&nbsp;другие мероприятия.
          </p>
        </Dropdown>
        <Dropdown title="Как позвать друзей?">
          <p class="dropdown-descr">
            Вы&nbsp;можете поделиться мероприятием, отправив ссылку на&nbsp;платформу. Любой
            пользователь может стать участником. Участники получат уведомления о&nbsp;записи
            и&nbsp;скором начале мероприятия.
          </p>
        </Dropdown>
        <Dropdown title="Есть&nbsp;ли мобильное приложение?">
          <p class="dropdown-descr">Нет, пока у&nbsp;нас нет мобильного приложения.</p>
        </Dropdown>
        <Dropdown title="Как оставить отзыв?" isBottomHr="true">
          <p class="dropdown-descr">
            Вы&nbsp;можете оставить отзыв о&nbsp;платформе в&nbsp;разделе &rsquo;Отзывы&rsquo;.
            Мы&nbsp;ценим ваше мнение и&nbsp;используем его для улучшения сервиса. Ваш отзыв поможет
            другим пользователям.
          </p>
        </Dropdown>
        <Dropdown title="Как отменить мероприятие?" isBottomHr="true">
          <p class="dropdown-descr">
            Для отмены мероприятия вам нужно зайти в&nbsp;свой аккаунт. Выберите событие
            и&nbsp;нажмите &rsquo;Отменить&rsquo;. Мы&nbsp;отправим уведомление всем участникам.
          </p>
        </Dropdown>
      </div>
    </div>
  </section>
</template>

<script>
import IconArrow from '../icons/IconArrow.vue'
import Dropdown from '../Dropdown.vue'
export default {
  components: {
    IconArrow,
    Dropdown,
  },
}
</script>

<style></style>

<style scoped>
.faq__wrapper {
  display: flex;
  flex-direction: column;
  gap: 5rem;
}

.faq__header {
  display: flex;
  flex-direction: column;
  text-align: center;
  gap: 1.5rem;
}

.faq__title {
  font-size: 48px;
}

.faq__descr {
  font-size: 18px;
}

.faq__content {
  display: grid;
  grid-template-columns: 1fr 1fr;
  column-gap: 4rem;
}
</style>
