<template>
    <div class="info">
      <h2>Информация</h2>
      <p>Информация о пользователе.</p>
      <div class="stats">
        <h3>Статистика:</h3>
        <ul>
          <li>Количество постов: {{ totalPosts }}</li>
          <li>Количество уникальных авторов: {{ totalAuthors }}</li>
          <li>Количество уникальных тегов: {{ totalTags }}</li>
        </ul>
      </div>
    </div>
  </template>
  
  <script>
  import { mapGetters } from 'vuex'; 
  
  export default {
    name: 'Info',
    computed: {
      ...mapGetters(['totalPosts', 'totalAuthors', 'totalTags']) 
    }
  };
  </script>
  
  <style scoped>
  .info {
    padding: 20px;
    text-align: center;
    background-color: #ffffff;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  }
  .info h2 {
    margin-bottom: 20px;
  }
  .info p {
    font-size: 16px;
    line-height: 1.5;
  }
  .stats {
    margin-top: 20px;
  }
  .stats h3 {
    margin-bottom: 10px;
  }
  .stats ul {
    list-style-type: none;
    padding: 0;
  }
  .stats li {
    margin-bottom: 5px;
    font-size: 16px;
    color: #2c3e50;
  }
  </style>