import { createStore } from 'vuex';

const store = createStore({
  state() {
    return {
      todos: []
    };
  },
  mutations: {
    addTodo(state, todo) {
      state.todos.push(todo);
    },
    deleteTodo(state, index) {
      state.todos.splice(index, 1);
    }
  },
  getters: {
    totalPosts(state) {
      return state.todos.length;
    },
    totalAuthors(state) {
      const authors = state.todos.map(todo => todo.author);
      return new Set(authors).size;
    },
    totalTags(state) {
      const tags = state.todos.flatMap(todo => todo.tag.split(',').map(tag => tag.trim()));
      return new Set(tags).size;
    }
  },
  actions: {
    addTodo({ commit }, todo) {
      commit('addTodo', todo);
    },
    deleteTodo({ commit }, index) {
      commit('deleteTodo', index);
    }
  }
});

export default store;