<template>
  <button class="btn">
    <a :href="href" class="link">
      <span class="btn__text">{{ text }}</span>
      <IconArrow direction="right" :fill="fill" />
    </a>
  </button>
</template>

<script>
import IconArrow from './icons/IconArrow.vue'
export default {
  components: {
    IconArrow,
  },
  props: {
    text: { type: String, require: true },
    fill: String,
    href: String,
  },
}
</script>

<style scoped>
button {
  position: relative;
  display: flex;
  gap: 0.5rem;
  border-color: transparent;
}

button::after {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  height: 100%;
  width: 0;
  background: var(--main-color);
  transition: all 0.3s ease;
  z-index: -1;
}

button:hover::after {
  width: 100%;
}

button:hover {
  border-color: var(--main-color);
}
</style>
