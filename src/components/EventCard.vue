<template>
  <div class="event-card">
    <img :src="cover" alt="" class="event-card-image" />
    <div class="event-card__header">
      <p class="event-card__type">{{ type }}</p>
      <h3 class="event-card__title">{{ name }}</h3>
    </div>
    <div class="event-card__info">
      <div class="event-card__info-date label">
        <IconCalendarSmall class="event-card__date-icon icon" />
        <p class="event-card__date-text">{{ date }}</p>
      </div>
      <div class="event-card__info-time label">
        <IconWatches class="event-card__time-icon icon" />
        <p class="event-card__time-text">{{ time }}</p>
      </div>
      <div class="event-card__info-location label">
        <IconLocation class="event-card__location-icon icon" />
        <p class="event-card__location-text">{{ location }}</p>
      </div>
    </div>
    <div class="event-card__btn">
      <a href="" class="event-card__btn-link">Подробнее</a>
      <IconArrow direction="down" class="event-card__btn-icon" />
    </div>
  </div>
</template>

<script>
// import noneImage from '@/assets/images/none.png'
import IconLocation from './icons/IconLocation.vue'
import IconCalendarSmall from './icons/IconCalendar-small.vue'
import IconArrow from './icons/IconArrow.vue'
import IconWatches from './icons/IconWatches.vue'

export default {
  components: {
    // noneImage,
    IconLocation,
    IconCalendarSmall,
    IconArrow,
    IconWatches,
  },
  props: {
    type: { type: String, required: true },
    cover: { type: Image, required: true },
    name: { type: String, required: true },
    date: { type: String, required: true },
    time: { type: String, required: true },
    location: { type: String, required: true },
  },
  data() {
    return {
      // noneImage,
    }
  },
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Open+Sans:ital,wght@0,300..800;1,300..800&display=swap');

:root {
  --font3: "Open Sans", sans-serif;
}
</style>

<style scoped>
.event-card {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-between;

  gap: 5px;

  width: 275px;
  max-height: max-content;
  border-radius: 14px;

  box-shadow: 0 4px 12px 0 rgba(0, 0, 0, 0.25);
  background: #f1f1f1;
}

.event-card__header {
  display: flex;
  flex-direction: column;
  text-align: center;
  max-width: 70%;
}

.event-card__type {
  font-family: var(--title-font-family);
  font-weight: 700;
  font-size: 12px;
  color: #295e8f;
}

.event-card__title {
  font-family: var(--title-font-family);
  font-weight: 700;
  font-size: 11px;
  color: #141414;
  height: 48px;
}

.event-card__info {
  justify-self: end;
  display: flex;
  flex-direction: column;
  gap: 10px;
  width: 80%;
}

.label {
  flex: 1;
  display: flex;
  align-items: center;
  background: #65b1da;
  border-radius: 9px;
  gap: 3px;

  font-family: var(--title-font-family);
  font-weight: 700;
  font-size: 12px;
  color: #000;
}

.icon {
  width: 26px;
  height: 26px;
}

.event-card__btn {
  display: flex;
  flex-direction: column;
  align-items: center;
  /* gap: 5px; */
  font-family: var(--font3);
  font-weight: 700;
  font-size: 10px;
  color: #295e8f;
}
</style>
