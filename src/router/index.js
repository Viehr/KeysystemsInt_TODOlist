import { createRouter, createWebHistory } from 'vue-router';
import Home from '../views/Home.vue';
import Info from '../views/Info.vue';
import Login from '../views/Login.vue';
import { authService } from '../services/authService';

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
    meta: { requiresAuth: true },
  },
  {
    path: '/info',
    name: 'Info',
    component: Info,
    meta: { requiresAuth: true },
  },
  {
    path: '/login',
    name: 'Login',
    component: Login,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

router.beforeEach((to, from, next) => {
  const user = authService.getCurrentUser();

 
  const isAuthenticated = user !== null;

  
  if (to.matched.some((record) => record.meta.requiresAuth)) {
    if (!isAuthenticated) {
      next('/login'); 
    } else {
      next(); 
    }
  } else {
    next(); 
  }
});

export default router;