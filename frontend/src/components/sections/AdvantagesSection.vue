<template>
  <section id="advantages">
    <div class="container wrapper advs__wrapper">
      <h2 class="advs__title">
        Преимущества использования платформы <span class="highlight-text bold">RTFEST</span> для
        организации ваших мероприятий
      </h2>
      <!-- <p class="advs__descr">
          <span class="bold">RTFEST</span> упрощает процесс планирования мероприятий, предоставляя
          все необходимые инструменты в&nbsp;одном месте. С&nbsp;нашей платформой вы&nbsp;сможете
          сосредоточиться на&nbsp;создании незабываемых моментов.
        </p> -->
      <div class="advs__content">
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
          <div class="advs__card">
            <IconList class="advs__card-icon" />
            <h3 class="advs__card-title highlight-text bold">
              Простота записи на&nbsp;мероприятия
            </h3>
            <p class="advs__card-descr">
              Вы&nbsp;можете легко записываться на&nbsp;интересующее вас мероприятие, без
              регистрации
            </p>
          </div>
          <div class="advs__card">
            <IconFilter class="advs__card-icon" />
            <h3 class="advs__card-title highlight-text bold">Фильтрация мероприятий</h3>
            <p class="advs__card-descr">
              Быстрый поиск мероприятий по&nbsp;дате, категории, спикерам и&nbsp;другим параметрам.
            </p>
          </div>
        </div>
        <img src="/src/assets/images/advs.png" alt="" class="crap-image advs__image" />
      </div>
    </div>
  </section>
</template>

<script>
import IconCalendar from '../icons/IconCalendar.vue'
import IconNotify from '../icons/IconNotify.vue'
import IconList from '../icons/IconList.vue'
import IconFilter from '../icons/IconFilter.vue'

export default {
  components: {
    IconCalendar,
    IconNotify,
    IconList,
    IconFilter,
  },
}
</script>

<style></style>

<style scoped>
.advs__wrapper {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 2rem;
}

.advs__title {
  font-size: 28px;
  text-align: center;
}

.advs__content {
  display: flex;
  flex-direction: column;
  gap: 2rem;
  align-items: center;
}

.advs__cards {
  display: grid;
  grid-template-columns: 1fr;
  gap: 45px;
}

.advs__card {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  gap: 20px;
}

.advs__card-title {
  font-size: 24px;
}

.advs__card-descr {
  font-size: 16px;
}

.advs__card-icon {
  width: 55px;
  height: auto;
}

@media (min-width: 1024px) {
  .advs__title {
    font-size: 40px;
    text-align: center;
  }

  .advs__cards {
    display: grid;
    grid-template-columns: 1fr 1fr;
  }
}

@media (min-width: 1200px) {
  .advs__content {
    flex-direction: row;
  }
}
</style>
