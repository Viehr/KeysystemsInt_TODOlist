<template>
  <div class="login-container">
    <h2>Login</h2>
    <form @submit.prevent="login">
      <div class="form-group">
        <label for="username">Username</label>
        <input type="text" id="username" v-model="username" required />
      </div>
      <div class="form-group">
        <label for="password">Password</label>
        <input type="password" id="password" v-model="password" required />
      </div>
      <Button>Login</Button>
    </form>
    <p v-if="error" class="error">{{ error }}</p>
  </div>
</template>

<script>
import { authService } from '../services/authService';
import Button from '../components/UI/Button.vue';

export default {
  components: {
    Button,
  },
  data() {
    return {
      username: '',
      password: '',
      error: null,
    };
  },
  methods: {
    async login() {
      try {
        await authService.login(this.username, this.password);
        this.$router.push('/'); // Navigate to Home page on success
      } catch (err) {
        if (this.username === 'admin' && this.password !== 'admin') {
          this.error = 'Неправильный пароль для admin.';
        } else {
          this.error = 'Ошибка входа. Проверьте введенные данные.';
        }
      }
    },
  },
};
</script>

<style scoped>
.login-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  padding: 20px;
  background-color: #2c3e50;
}

h2 {
  margin-bottom: 20px;
  color: white;
}

.form-group {
  margin-bottom: 15px;
  width: 100%;
  max-width: 300px;
}

label {
  display: block;
  margin-bottom: 5px;
  color: white;
}

input {
  width: 100%;
  padding: 10px;
  font-size: 16px;
  color: black;
  background-color: #ffffff;
  border: 1px solid #ddd;
  border-radius: 4px;
}

button {
  background-color: #42b983;
  color: white;
  border: none;
  padding: 10px;
  cursor: pointer;
  border-radius: 4px;
}

button:hover {
  background-color: #369b74;
}

.error {
  color: red;
  margin-top: 10px;
}
</style>