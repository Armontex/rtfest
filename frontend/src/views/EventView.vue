<template>
  <main>
    <div class="event__wrapper container">
      <div class="event__components">
        <EventFilter />
        <Event
          :type="event.type"
          :cover="event.cover"
          :title="event.title"
          :time="event.time"
          :descr="event.descr"
          :location="event.location"
        />
      </div>
    </div>
  </main>
</template>

<script>
import E1 from '@/assets/images/e1.png'
import Event from '@/components/Event.vue'
import EventFilter from '@/components/EventFilter.vue'

import { ref, onMounted } from 'vue'
import axios from 'axios'

const API_BASE_URL = 'http://localhost:8000'

export default {
  name: 'EventView',
  components: {
    Event,
    EventFilter,
  },
  props: {
    id: {
      type: String,
      required: true,
    },
  },
  setup(props) {
    const event = ref({})

    const fetchEvents = async () => {
      try {
        console.log('ID:', props.id);
        const response = await axios.get(`${API_BASE_URL}/event/${props.id}`)
        event.value = response.data
        console.log('Мероприятие загружено:', event.value);
      } catch (error) {
        console.error('Ошибка при загрузке мероприятий:', error)
      }
    }

    onMounted(() => {
      fetchEvents()
    })

    return {
      event,
    }
  },
}
</script>

<style scoped>
.event__wrapper {
  margin-top: 70px;
}
.event__components {
  display: flex;
  gap: 45px;
}
</style>
