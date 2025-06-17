<template>
  <header>
    <TheHeader />
  </header>
  <!-- <main id="main">
    <router-view />
  </main> -->
  <!-- <footer>
    <TheFooter />
  </footer> -->
</template>

<script>
import TheHeader from './components/TheHeader.vue'
import TheFooter from './components/TheFooter.vue'

export default {
  components: {
    TheHeader,
    TheFooter,
  },
}
</script>
