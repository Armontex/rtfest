<template>
  <div class="dropdown" :class="{ active: isOpen }">
    <hr />
    <h4 class="dropdown__title" @click="toggle">
      {{ title }}
      <IconArrow :direction="isOpen ? 'up' : 'down'" class="arrow" />
    </h4>
    <div class="dropdown__content">
      <slot></slot>
    </div>
    <hr class="dropdown__hr" v-if="isBottomHr" />
  </div>
</template>

<script>
import IconArrow from './icons/IconArrow.vue'
export default {
  components: {
    IconArrow,
  },
  props: {
    title: {type: String, require: true },
    isBottomHr: Boolean,
  },
  data() {
    return {
      isOpen: false,
    }
  },
  methods: {
    toggle() {
      this.isOpen = !this.isOpen
    },
  },
}
</script>

<style scoped>
.dropdown__content {
  max-height: 0;
  overflow: hidden;
  transition: max-height 0.3s ease;
}

.dropdown__title {
  display: flex;
  align-items: center;
  justify-content: space-between;
  color: var(--color-base);
  width: 100%;
  margin: 10px 0;
}

.dropdown.active .dropdown__content {
  max-height: 1000px;
}
</style>
