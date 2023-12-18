// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router';
import Home from '../components/Home.vue';
import About from '../components/About.vue';
import Signin from '../components/Signin.vue';
import Signup from '../components/Signup.vue';
import Mainpage from '../components/Mainpage.vue'; 

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    component: About
  },
  {
    path: '/signin',
    name: 'Signin',
    component: Signin
  },
  {
    path: '/signup',
    name: 'Signup',
    component: Signup
  },
  {
    path: '/mainpage',
    component: Mainpage
  }
  // 可以添加更多的路由规则
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

router.onError((error) => {
  console.error('Router Error:', error.message)
})


export default router;
