<template>
  <div class="dialog-overlay" v-if="isVisible">
    <div class="dialog-content">
      <p>{{ message }}</p>
      <div class="dialog-buttons">
        <Button @click="confirm">Да</Button>
        <Button @click="cancel">Нет</Button>
      </div>
    </div>
  </div>
</template>

<script>
import Button from './Button.vue';

export default {
  components: { Button },
  props: {
    isVisible: {
      type: Boolean,
      required: true
    },
    message: {
      type: String,
      default: 'Вы уверены?'
    }
  },
  methods: {
    confirm() {
      this.$emit('confirm');
    },
    cancel() {
      this.$emit('cancel');
    }
  }
};
</script>

<style scoped>
.dialog-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(7, 7, 7, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
}
.dialog-content {
  background: white;
  padding: 20px;
  border-radius: 8px;
  text-align: center;
}
.dialog-buttons {
  margin-top: 10px;
}
.dialog-buttons button {
  margin: 0 5px;
}
</style>