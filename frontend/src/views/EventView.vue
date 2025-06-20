<template>
  <main>
    <div class="event__wrapper container">
      <div class="event__components">
        <!-- <EventFilter /> -->
        <EventMobile class="mobile"
          :type="event.type"
          :cover="event.cover"
          :title="event.title"
          :time="event.time"
          :descr="event.descr"
          :location="event.location"
        />
        <EventDesktop class="desktop"
          :type="event.type"
          :cover="event.cover"
          :title="event.title"
          :time="event.time"
          :descr="event.descr"
          :location="event.location"
        />
      </div>
      <div class="event__form">
        <EmailInput 
          class="event__form-item email" 
          @update:email="email = $event"
        />
        <LightButton 
          class="event__form-item button" 
          text="Записаться"
          @click="registerUser"
        />
      </div>
    </div>
  </main>
</template>

<script>
import EventMobile from '@/components/EventMobile.vue'
import EventDesktop from '@/components/EventDesktop.vue'
import EventFilter from '@/components/EventFilter.vue'

import EmailInput from '@/components/EmailInput.vue'
import LightButton from '@/components/LightButton.vue'

import { ref, onMounted } from 'vue'
import axios from 'axios'

const API_BASE_URL = 'http://localhost:8000'

export default {
  name: 'EventView',
  components: {
    EventMobile,
    EventFilter,
    EventDesktop,
    EmailInput,
    LightButton
  },
  props: {
    id: {
      type: String,
      required: true,
    },
  },
  setup(props) {
    const event = ref({})
    const email = ref('')

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

    const registerUser = async () => {
      if (!email.value) {
        alert('Пожалуйста, введите email')
        return
      }

      try {
        const response = await axios.post(`${API_BASE_URL}/register`, {
          event_id: props.id,
          email: email.value
        })
        console.log('Успешная регистрация:', response.data)
        alert('Вы успешно зарегистрированы на мероприятие!')
      } catch (error) {
        console.error('Ошибка регистрации:', error)
        alert('Произошла ошибка при регистрации. Попробуйте позже.')
      }
    }

    onMounted(() => {
      fetchEvents()
    })

    return {
      event,
      email,
      registerUser
    }
  },
}
</script>

<style scoped>
.desktop {
  display: none;
}

.event__wrapper {
  display: flex;
  flex-direction: column;
  gap: 50px;
  margin-top: 70px;
}
.event__components {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 50px;
}

.event__form {
  display: flex;
  justify-content: space-between;
  gap: 10px;
}

.event__form-item {
  flex: 1;
}


@media (min-width: 1024px) {
  .desktop {
    display: flex;
  }

  .mobile {
    display: none;
  }

  .event__components {
    align-items: start;
  }

  .event__form {
    justify-content: start;
  }

  .event__form-item {
    flex: unset;
  }
}
</style>
