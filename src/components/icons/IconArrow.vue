<template>
  <svg
    :width="width"
    :height="height"
    :viewBox="`0 0 ${width} ${height}`"
    fill="none"
    xmlns="http://www.w3.org/2000/svg"
  >
    <path
      fill-rule="evenodd"
      clip-rule="evenodd"
      d="M8.46974 0.82314C8.76264 0.53024 9.23744 0.53024 9.53034 0.82314L17.1768 8.46964C17.4697 8.76254 17.4697 9.23734 17.1768 9.53024L16.8233 9.88384C16.5304 10.1767 16.0555 10.1767 15.7626 9.88384L9.00004 3.12124L2.23744 9.88384C1.94454 10.1767 1.46974 10.1767 1.17684 9.88384L0.823237 9.53024C0.530336 9.23734 0.530336 8.76254 0.823237 8.46964L8.46974 0.82314Z"
      :fill="fill"
      :style="getTransformByDirection(direction)"
    />
  </svg>
</template>

<script lang="ts">
export default {
  props: {
    fill: {
      type: String,
      default: '#fff',
    },
    direction: {
      type: String as () => 'up' | 'down' | 'left' | 'right',
      default: 'up',
    },
    width: {
      type: Number,
      default: 18,
    },
    height: {
      type: Number,
      default: 11,
    },
  },
  methods: {
    getTransformByDirection(direction: string): string {
      const rotations: Record<string, number> = {
        down: 180,
        right: 90,
        left: 270,
      }
      const rotationDeg = rotations[direction.toLowerCase()] || 0
      return `transform: rotate(${rotationDeg}deg); transform-origin: center;`
    },
  },
}
</script>
