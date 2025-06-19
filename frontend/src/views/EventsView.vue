<template>
  <main>
    <div class="events__wrapper container">
      <div class="events__components">
        <EventFilter @filter-change="fetchEvents"/>
        <div class="events__cards">
          <EventCard
            class="event__card"
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
    const activeFilters = ref({})

    const buildQueryParams = (filters) => {
      const params = new URLSearchParams()
      
      if (filters.all) {
        return params
      }
      
      for (const [key, value] of Object.entries(filters)) {
        if (value && key !== 'all') {
          params.append('types', key)
        }
      }
      
      return params
    }

    const fetchEvents = async (filters = {}) => {
      try {
        const params = buildQueryParams(filters)
        let url = `${API_BASE_URL}/events`
        
        if (params.toString()) {
          url += `?${params.toString()}`
          window.history.pushState({}, '', `?${params.toString()}`)
        } else {
          window.history.pushState({}, '', window.location.pathname)
        }
        
        const response = await axios.get(url)
        events.value = response.data
        console.log('Мероприятия загружены:', events.value)
      } catch (error) {
        console.error('Ошибка при загрузке мероприятий:', error)
      }
    }

    onMounted(() => {
      fetchEvents()
    })

    return {
      events,
      fetchEvents
    }
  },
}
</script>

<style scoped>
.events__wrapper {
  display: flex;
  flex-direction: column;
  margin-bottom: 150px;
  margin-top: 65px;
  min-height: max-content;
}

.events__components {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 50px;
}

.events__cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(275px, 100%), 1fr));
  width: 100%;
  justify-items: start;
  gap: 30px;
}

@media (min-width: 950px) {
  .events__components {
    flex-direction: row;
    align-items: start;
  }
}
</style>
