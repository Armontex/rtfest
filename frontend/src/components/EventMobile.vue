<template>
  <div class="event">
    <div class="event__body">
      <img :src="cover" alt="" class="event__cover" />
      <p class="event__type bold">{{ type }}</p>
      <h2 class="event__title bold">{{ title }}</h2>
      <div class="event__content">
        <div class="event__time event__info">
          <IconWatches class="event__time-icon icon" />
          <span class="event__time-text bold">Hачало:</span>
          <span class="event__time-text bold">{{ time }}</span>
        </div>
        <div class="event__location event__info">
          <IconLocation class="event__location-icon icon" />
          <span class="event__location-text bold">Место:</span>
          <span class="event__location-text bold">{{ location }}</span>
        </div>
      </div>
    </div>
    <p class="event__descr" v-html="formatDescription(descr)"></p>
  </div>
</template>

<script>
import IconLocation from './icons/IconLocation.vue'
import IconWatches from './icons/IconWatches.vue'

export default {
  components: {
    IconLocation,
    IconWatches,
  },
  props: {
    type: { type: String, required: true },
    cover: { type: String, required: true },
    title: { type: String, required: true },
    time: { type: String, required: true },
    location: { type: String, required: true },
    descr: { type: String, default: '' },
  },
  methods: {
  formatDescription(text) {
    if (!text) return '';
    return text.split('\\n').join('<br>');
  }
}
}
</script>

<style scoped>
.icon {
  width: 25px;
  height: auto;
}

.event {
  display: flex;
  flex-direction: column;
  gap: 50px;
  align-items: center;
}

.event__body {
  display: flex;
  flex-direction: column;
  align-items: center;

  font-family: var(--main-color);
  color: #000;
  background: #F1F1F1;
  border-radius: 14px;
}

.event__type {
  text-align: center;
  color: #295E8F;
  text-transform: uppercase;

  margin-top: 10px;
}

.event__title {
  text-align: center;
  text-transform: uppercase;
  font-size: 11px;
  margin: 5px 0 10px;
}

.event__content {
  display: flex;
  flex-direction: column;
  align-self: start;
  align-items: start;

  margin: 0 0 10px 15px;
  gap: 0.5rem;
  font-size: 15px;
}

.event__info {
  display: flex;
  align-items: center;
  gap: 10px;
}

@media (min-width: 768px) {
  .event {
    flex-direction: row;
    align-items: center;
    justify-content: center;
  }


  .event__descr {
    max-width: 50%;
  }
}
</style>
