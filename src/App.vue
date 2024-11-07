<template>
  <div id="app">
    <header>
      <h1>Кормилина Александра</h1>
      <p>Буратино посадили в тюрьму. Захлопнулась за ним дверь камеры. И прокурор, снимая шляпу, сказал: Наконец-то я посадил дерево!</p>
      <nav>
        <router-link to="/">Главная</router-link>
        <router-link to="/info">Информация</router-link>
      </nav>
    </header>
    <div class="content-container">
      <router-view></router-view> 
    </div>
  </div>
</template>

<script>
export default {
  name: 'App'
};
</script>

<style scoped>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  text-align: center;
  color: #2c3e50;
  background-color: #2c3e50;
  margin-top: 60px;
  min-height: 100vh;
}
header {
  position: fixed;
  top: 0;
  width: 100%;
  background-color: #42b983;
  padding: 20px;
  color: white;
  z-index: 1000;
}
header h1 {
  margin: 0;
}
header p {
  margin: 10px 0 0;
  font-size: 16px;
}
nav {
  margin-top: 10px;
}
nav a {
  margin: 0 10px;
  color: white;
  text-decoration: none;
}
nav a:hover {
  text-decoration: underline;
}
.content-container {
  display: flex;
  margin-top: 100px;
  padding: 20px;
  justify-content: center;
}
</style>