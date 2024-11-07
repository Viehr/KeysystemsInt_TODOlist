<template>
  <table>
    <thead>
      <tr>
        <th>Автор</th>
        <th>Тэг</th>
        <th>Пост</th>
        <th>Действие</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="(todo, index) in todos" :key="index">
        <td>{{ todo.author }}</td>
        <td>{{ todo.tag }}</td>
        <td>{{ todo.post }}</td>
        <td><button @click="$emit('deleteTodo', index)">Удалить</button></td>
      </tr>
    </tbody>
  </table>
</template>

<script>
export default {
  props: {
    todos: {
      type: Array,
      required: true
    }
  }
};
</script>

<style scoped>
table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 20px;
}
th, td {
  border: 1px solid #ddd;
  padding: 8px;
  color: white; 
}
th {
  background-color: #42b983;
  color: white;
}
tbody tr {
  background-color: #2c3e50; 
}
button {
  background-color: #e74c3c;
  color: white;
  border: none;
  padding: 5px 10px;
  cursor: pointer;
}
button:hover {
  background-color: #c0392b;
}
</style>