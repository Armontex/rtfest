<template>
  <section id="workflow">
    <div class="container wrapper workflow__wrapper">
      <h2 class="workflow__title">
        Как работает платформа <span class="highlight-text bold">RTFEST</span> для организации ваших
        мероприятий
      </h2>
      <div class="workflow__cards">
        <div class="workflow__card">
          <IconList class="workflow__card-icon" />
          <h3 class="workflow__card-title highlight-text bold">
            Простота записи на&nbsp;мероприятия
          </h3>
          <p class="workflow__card-descr">
            Вы&nbsp;можете легко записываться на&nbsp;интересующее вас мероприятие.
          </p>
          <ArrowButton text="Узнать" href="#faq" fill="var(--main-color)"/>
        </div>
        <div class="workflow__card">
          <IconFilter class="workflow__card-icon" />
          <h3 class="workflow__card-title highlight-text bold">Фильтрация мероприятий</h3>
          <p class="workflow__card-descr">
            Быстрый поиск мероприятий по&nbsp;дате, категории, спикерам и&nbsp;другим параметрам.
          </p>
          <ArrowButton text="Начать" fill="var(--main-color)"/>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import IconFilter from '../icons/IconFilter.vue'
import IconList from '../icons/IconList.vue'
import ArrowButton from '../ArrowButton.vue'

export default {
  components: {
    IconFilter,
    IconList,
    ArrowButton,
  },
}
</script>

<style></style>

<style scoped>
.workflow__wrapper {
  display: flex;
  flex-direction: column;
  gap: 5rem;
  align-items: center;
  text-align: center;
}

.workflow__title {
  font-size: 40px;
  width: 60vw;
}

.workflow__cards {
  display: flex;
  justify-content: space-between;
  width: 100%;
}

.workflow__card {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1.5rem;
}
</style>
