// src/router.js
import { createRouter, createWebHistory } from 'vue-router';
import Home from './Home.vue'; // 假设您有一个 Home.vue 组件
import Programmer from './Programmer.vue'; // 假设您有一个 Programmer.vue 组件

const routes = [
  { path: '/', component: Home },
  { path: '/programmer', component: Programmer }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;