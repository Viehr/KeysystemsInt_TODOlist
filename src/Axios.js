import axios from 'axios';
import { authService } from './services/authService';

const instance = axios.create({
  baseURL: 'http://Viehr.pythonanywhere.com/',
});

instance.interceptors.request.use(
  (config) => {
    const user = authService.getCurrentUser();
    if (user && user.access) {
      if (user.access === 'admin-token') {
        config.headers.Authorization = `Bearer fake-admin-token`;
      } else {
        config.headers.Authorization = `Bearer ${user.access}`;
      }
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

export default instance;