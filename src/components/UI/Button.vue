<template>
  <button :class="buttonClass" @click="$emit('click')">
    <slot></slot>
  </button>
</template>

<script>
export default {
  props: {
    buttonClass: {
      type: String,
      default: 'default-button'
    }
  }
};
</script>

<style scoped>
.default-button {
  background-color: #42b983;
  color: white;
  border: none;
  padding: 10px;
  cursor: pointer;
}
.default-button:hover {
  background-color: #369b74;
}
</style>