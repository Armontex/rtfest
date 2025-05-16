<template>
  <main>
    <div class="events__wrapper container">
      <div class="events__components">
        <EventFilter />
        <div class="events__cards">
          <EventCard
            v-for="event in events"
            :type="event.type"
            :cover="event.cover"
            :name="event.name"
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

export default {
  name: 'Events',
  components: {
    EventCard,
    EventFilter,
  },
  setup() {
    const events = ref([])

    const mockEvents = [
      {
        type: 'КИНО',
        name: 'МАЛЬЧИК В ПОЛОСАТОЙ ПИЖАМЕ',
        cover: E1,
        date: '13 мая',
        time: '18:00',
        location: 'Р-217',
      },
      {
        type: 'МАСТЕР-КЛАССЫ',
        name: 'ВОЛШЕБНЫЕ ОТКРЫТКИ СВОИМИ РУКАМ',
        cover: E2,
        date: '20 февраля',
        time: '15:00',
        location: 'Р-044',
      },
      {
        type: 'СПОРТ',
        name: 'ЭСТАФЕТА',
        cover: E3,
        date: '03 мая',
        time: '18:00',
        location: 'Р-044',
      },
      {
        type: 'МАСТЕР-КЛАССЫ',
        name: 'ШНУРОМАНИЯ. СОЗДАЙ СВОЙ СТИЛЬНЫЙ РЕМЕШОК',
        cover: E4,
        date: '03 мая',
        time: '15:00',
        location: 'ул. Мира, 39',
      },
      {
        type: 'ФЕСТИВАЛИ',
        name: 'ВСЕЛЕННАЯ ИРИТ-РТФ',
        cover: E5,
        date: '03 мая',
        time: '18:00',
        location: 'Р-044',
      },
      {
        type: 'ВИКТОРИНЫ',
        name: 'НОВОГОДНИЙ КВИЗ',
        cover: E6,
        date: '03 мая',
        time: '15:00',
        location: 'Р-044',
      },
    ]

    const fetchEvents = async () => {
      try {
        // TODO: Запрос к API !!!
        events.value = mockEvents
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
