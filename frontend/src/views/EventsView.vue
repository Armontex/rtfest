<template>
  <main>
    <div class="events__wrapper container">
      <div class="events__components">
        <EventFilter />
        <div class="events__cards">
          <EventCard
            v-for="event in events"
            :id="event.id"
            :type="event.type"
            :cover="event.cover"
            :title="event.title"
            :date="event.date"
            :time="event.time"
            :location="event.location"
          />
        </div>
      </div>
    </div>
  </main>
</template>

<script>
import E1 from '@/assets/images/e1.png'
import E2 from '@/assets/images/e2.png'
import E3 from '@/assets/images/e3.png'
import E4 from '@/assets/images/e4.png'
import E5 from '@/assets/images/e5.png'
import E6 from '@/assets/images/e6.png'

import EventCard from '@/components/EventCard.vue'
import EventFilter from '@/components/EventFilter.vue'
import { ref, onMounted } from 'vue'
import axios from 'axios'

const API_BASE_URL = 'http://localhost:8000';

export default {
  name: 'Events',
  components: {
    EventCard,
    EventFilter,
  },
  setup() {
    const events = ref([])

    const fetchEvents = async () => {
      try {
        const response = await axios.get(`${API_BASE_URL}/events`);
        events.value = response.data;
        console.log('Мероприятия загружены:', events.value);
      } catch (error) {
        console.error('Ошибка при загрузке мероприятий:', error)
      }
    }
    onMounted(() => {
      fetchEvents()
    })

    return {
      events,
    }
  },
}
</script>

<style scoped>
.events__wrapper {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-bottom: 150px;
  margin-top: 65px;
  min-height: 950px;
}

.events__components {
  display: flex;
  gap: 22px;
}

.events__cards {
  margin-left: auto;
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 43px 50px;
}
</style>
