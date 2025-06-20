<template>
  <button class="btn" @click="handleClick">
    <a :href="href" class="link">
      <span class="btn__text">{{ text }}</span>
    </a>
  </button>
</template>

<script>
export default {
  props: {
    text: { type: String, required: true },
    href: String,
  },
  emits: ['click'],
  methods: {
    handleClick() {
      this.$emit('click')
    }
  }
}
</script>

<style scoped>
button {
  background-color: var(--main-color);
}

button:hover,
button:focus {
  background-color: transparent;
}
</style>
