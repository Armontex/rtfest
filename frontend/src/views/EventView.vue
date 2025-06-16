<template>
  <main>
    <div class="event__wrapper container">
      <div class="event__components">
        <EventFilter />
        <Event
          :type="event.type"
          :cover="event.cover"
          :name="event.name"
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

export default {
  name: 'EventView',
  components: {
    Event,
    EventFilter,
  },
  setup() {
    const event = ref({})

    const mockEvent = {
      type: 'Викторины',
      name: 'Новогодний квиз',
      cover: E1,
      date: '13 мая',
      time: '17 : 30',
      location: 'Коворкинг (Р-044)',
      descr:
        'Все вокруг наполняется атмосферой приближающегося праздника, а это значит, что самое время для традиционного новогоднего мероприятия в формате квиза, в котором каждый сможет принять участие. Поэтому не упусти возможность зарядиться волшебным настроением в предверии Нового года\n\nС нетерпением ждем тебя: 23 декабря в 17:30 в коворкинге ИРИТ-РТФ (Р-044)\n\nСкорее собирай команду из 3-5 человек, запасайся новогодним настроением, мишурой и мандаринами, а также приходи в ярком праздничном костюме. Говорят, что за это будут дополнительные баллы ',
    }

    const fetchEvents = async () => {
      try {
        // TODO: Запрос к API !!!
        event.value = mockEvent
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
