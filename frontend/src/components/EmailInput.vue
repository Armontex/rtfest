<template>
  <input 
    type="email" 
    class="input" 
    v-model="emailValue" 
    placeholder="Введите ваш email" 
    @input="updateEmail"
  />
</template>

<script>
export default {
  emits: ['update:email'],
  data() {
    return {
      emailValue: ''
    }
  },
  methods: {
    updateEmail() {
      this.$emit('update:email', this.emailValue)
    }
  }
}
</script>

<style scoped>
.input {
  padding: 0.75rem;
  background-color: transparent;
  border: 1px solid var(--main-color);
  border-radius: 15px;
  height: 47.5px;
  color: #fff;
}

.input:focus {
  border-color: #fff;
}
</style>
