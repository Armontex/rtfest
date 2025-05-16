<!-- <template>
    <input
      class="input"
      v-model="email"
      @blur="validateEmail"
      placeholder="Введите ваш email"
      :class="{ 'invalid': !isValid }"
    >
    <p v-if="!isValid" class="error">Некорректный email</p>
</template> -->

<template>
  <input type="email" class="input" v-model="email" placeholder="Введите ваш email" />
</template>

<script></script>

<style scoped>
.input {
  padding: 0.75rem;
  background-color: transparent;
  border: 1px solid var(--main-color);
  height: 47.5px;
  color: #fff;
}

.input:focus {
  border-color: #fff;
}

/* .invalid {
  border-color: red;
}
.error {
  color: red;
} */
</style>
