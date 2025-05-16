<template>
  <button class="btn">
    <a :href="href" class="link">
      <span class="btn__text">{{ text }}</span>
    </a>
  </button>
</template>

<script>
export default {
  props: {
    text: { type: String, require: true },
    href: String,
  },
}
</script>

<style scoped>
button:hover {
  background-color: var(--main-color);
}
</style>
