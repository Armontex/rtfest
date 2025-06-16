<template>
  <label class="checkbox__label">
    <input
      type="checkbox"
      class="checkbox__input"
      :checked="modelValue"
      @change="$emit('update:modelValue', $event.target.checked)"
    />
    <span class="checkbox__checkmark">{{ text }}</span>
  </label>
</template>

<script>
export default {
  props: {
    name: { type: String, required: true },
    text: { type: String, required: true },
    modelValue: {
      type: Boolean,
      default: false,
    },
  },
  emits: ['update:modelValue'],
}
</script>

<style></style>

<style scoped>
.checkbox__label {
  position: relative;
  display: flex;
  align-items: center;
  gap: 8px;
}

.checkbox__input {
  appearance: none;
  -webkit-appearance: none;
  width: 16px;
  height: 16px;
  border: 1px solid #fff;
  border-radius: 100%;
}

.checkbox__input:checked::before {
  content: '✓';
  color: white;
  position: absolute;
  top: -2px;
  left: 3px;
  font-size: 16px;
}

.checkbox__checkmark {
  font-family: var(--title-font-family);
  font-weight: 700;
  font-size: 14px;
  color: #fff;
}
</style>
