<template>
    <div class="sort-controls">
      <Button @click="setSortOrder('author')">Сортировка по автору</Button>
      <Button @click="setSortOrder('tag')">Сортировка по тегу</Button>
      <Button @click="setSortOrder('none')">Без сортировки</Button>
    </div>
  </template>
  
  <script>
  import Button from './Button.vue';
  
  export default {
    components: { Button },
    props: {
      modelValue: {
        type: String,
        default: 'none'
      }
    },
    methods: {
      setSortOrder(order) {
        this.$emit('update:modelValue', order);
      }
    }
  };
  </script>
  
  <style scoped>
  .sort-controls {
    margin-bottom: 20px;
    display: flex;
    justify-content: space-around;
    flex-wrap: wrap;
  }
  
  .sort-controls button {
    margin-bottom: 10px;
  }
  </style>