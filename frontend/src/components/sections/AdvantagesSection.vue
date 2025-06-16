<template>
  <section id="advantages">
    <div class="container wrapper advs__wrapper">
      <div class="advs__content">
        <h2 class="advs__title">
          Преимущества использования платформы <span class="highlight-text bold">RTFEST</span> для
          организации ваших мероприятий
        </h2>
        <p class="advs__descr">
          <span class="bold">RTFEST</span> упрощает процесс планирования мероприятий, предоставляя
          все необходимые инструменты в&nbsp;одном месте. С&nbsp;нашей платформой вы&nbsp;сможете
          сосредоточиться на&nbsp;создании незабываемых моментов.
        </p>
        <div class="advs__cards">
          <div class="advs__card">
            <IconCalendar class="advs__card-icon" />
            <h3 class="advs__card-title highlight-text bold">Удобство использования</h3>
            <p class="advs__card-descr">
              Легкий интерфейс и&nbsp;доступ к&nbsp;важной информации в&nbsp;любое время.
            </p>
          </div>
          <div class="advs__card">
            <IconNotify class="advs__card-icon" />
            <h3 class="advs__card-title highlight-text bold">Своевременные оповещения</h3>
            <p class="advs__card-descr">
              Мгновенные уведомления о&nbsp;важных изменениях и&nbsp;новых событиях.
            </p>
          </div>
        </div>
      </div>
      <img src="/src/assets/images/advs.png" alt="" class="crap-image advs__image" />
    </div>
  </section>
</template>

<script>
import IconCalendar from '../icons/IconCalendar.vue'
import IconNotify from '../icons/IconNotify.vue'

export default {
  components: {
    IconCalendar,
    IconNotify,
  },
}
</script>

<style></style>

<style scoped>
.advs__wrapper {
  display: flex;
  gap: 3rem;
  align-items: center;
}

.advs__content {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.advs__title {
  font-size: 40px;
}

.advs__descr {
  font-size: 18px;
}

.advs__cards {
  display: flex;
  justify-content: space-between;
}

.advs__card {
  display: flex;
  flex-direction: column;
  align-items: start;
  gap: 1rem;
}

.advs__card-icon {
  align-self: center;
}
</style>
