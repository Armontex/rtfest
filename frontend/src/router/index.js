import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import EventsView from '@/views/EventsView.vue';
import EventView from '@/views/EventView.vue';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/events',
      name: 'Events',
      component: EventsView
    },
    {
      path: '/event/:id',
      name: 'Event',
      component: EventView,
      props: true
    }
  ],
})

export default router
