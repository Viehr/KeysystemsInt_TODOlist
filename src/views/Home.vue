<template>
    <div>
      <div class="form-container">
        <form @submit.prevent="handleAddTodo"> 
          <input v-model="newAuthor" placeholder="Автор" required />
          <input v-model="newTag" placeholder="Тэг" required />
          <textarea v-model="newPost" placeholder="Пост" required></textarea>
          <Button>Добавить</Button>
        </form>
      </div>
      <div class="todos-container">
        <SortControls v-model="sortOrder" />
        <todo-table :todos="sortedTodos" @deleteTodo="showConfirmDialog"></todo-table>
        <p v-if="todos.length === 0">Нет записей для отображения</p>
      </div>
      <confirmation-dialog 
        :isVisible="isDialogVisible" 
        message="Вы уверены, что хотите удалить запись?" 
        @confirm="handleConfirmDelete" 
        @cancel="handleCancelDelete">
      </confirmation-dialog>
    </div>
  </template>
  
  <script>
  import { mapState, mapActions } from 'vuex';
  import TodoTable from '../components/TodoTable.vue';
  import Button from '../components/UI/Button.vue';
  import ConfirmationDialog from '../components/UI/ConfirmationDialog.vue';
  import SortControls from '../components/UI/SortControls.vue';
  
  export default {
    components: {
      TodoTable,
      Button,
      ConfirmationDialog,
      SortControls
    },
    data() {
      return {
        newAuthor: '',
        newTag: '',
        newPost: '',
        sortOrder: 'none',
        isDialogVisible: false,
        deleteIndex: null
      };
    },
    computed: {
      ...mapState(['todos']), 
      sortedTodos() {
        if (this.sortOrder === 'author') {
          return [...this.todos].sort((a, b) => a.author.localeCompare(b.author));
        } else if (this.sortOrder === 'tag') {
          return [...this.todos].sort((a, b) => a.tag.split(',').length - b.tag.split(',').length);
        } else {
          return this.todos;
        }
      }
    },
    methods: {
      ...mapActions(['addTodo', 'deleteTodo']), 
      handleAddTodo() { 
        const newTodo = {
          author: this.newAuthor,
          tag: this.newTag,
          post: this.newPost
        };
  
        
        this.addTodo(newTodo);
  
        
        this.newAuthor = '';
        this.newTag = '';
        this.newPost = '';
      },
      showConfirmDialog(index) {
        this.deleteIndex = index;
        this.isDialogVisible = true;
      },
      handleConfirmDelete() {
        if (this.deleteIndex !== null) {
          this.deleteTodo(this.deleteIndex); 
          this.deleteIndex = null;
        }
        this.isDialogVisible = false;
      },
      handleCancelDelete() {
        this.deleteIndex = null;
        this.isDialogVisible = false;
      }
    }
  };
  </script>
  
  <style scoped>
  .form-container {
    flex: 1;
    max-width: 300px;
    padding: 20px;
  }
  .todos-container {
    flex: 2;
    padding: 20px;
    max-width: 700px;
  }
  .sort-controls {
    margin-bottom: 20px;
  }
  form {
    display: flex;
    flex-direction: column;
    margin-bottom: 20px;
  }
  form input, form textarea {
    margin-bottom: 10px;
    padding: 10px;
    font-size: 16px;
    color: #ffffff; 
    background-color: #2c3e50; 
    border: 1px solid #ddd; 
    border-radius: 4px; 
  }
  form textarea {
    height: 100px;
  }
  </style>