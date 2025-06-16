<template>
    <div class="event">
        <h2 class="event__title">{{ name }}</h2>
        <p class="event__type">{{ type }}</p>
        <div class="event__body">
            <img :src="cover" alt="" class="event__cover">
            <div class="event__content">
                <div class="event__time event__info">
                    <IconWatches class="event__time-icon icon" />
                    <span class="event__time-text">Hачало:</span>
                    <span class="event__time-text">{{ time }}</span>
                </div>
                <div class="event__location event__info">
                    <IconLocation class="event__location-icon icon" />
                    <span class="event__location-text">Место:</span>
                    <span class="event__location-text">{{ location }}</span>
                </div>
            </div>
        </div>
        <p class="event__descr">{{ descr }}</p>
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
    cover: { type: Image, required: true },
    name: { type: String, required: true },
    time: { type: String, required: true },
    location: { type: String, required: true },
    descr: { type: String, default: '' },
  },
}
</script>

<style scoped>
.icon {
    width: 51px;
    height: 51px;
}
.event {
    display: flex;
    flex-direction: column;
    gap: 2rem;
}

.event__title {
    font-size: 40px;
    font-weight: bold;
}

.event__type {
    align-self: flex-start;
    font-size: 20px;
    font-weight: bold;

    padding: 9px 12px;
    background: #65B1DA;
    border-radius: 9px;
}

.event__body {
    display: flex;
    align-items: center;
    gap: 40px;

    background: #D9D9D9;
    padding: 25px 40px;
    border-radius: 42px;
}

.event__cover {
    width: 334px;
    height: 232px;
}

.event__content {
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
    color: #000;
    font-weight: bold;
    font-size: 24px;
}

.event__info {
    display: flex;
    align-items: center;
    gap: 20px;
}

.event__descr {
    font-size: 24px;
    font-weight: bold;
    white-space: pre-line;
}
</style>
