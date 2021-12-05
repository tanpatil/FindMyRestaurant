import Vue from 'vue';
import VueRouter from 'vue-router';

import Landing from '../pages/Landing.vue';
import Onboarding from '../pages/Onboarding.vue';
import Recs from '../pages/Recs.vue'
import About from '../pages/About.vue';



Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'landing',
    component: Landing
  },
  {
    path: '/eat',
    name: 'onboarding',
    component: Onboarding
  },
  {
    path: '/recs',
    name: 'recs',
    component: Recs
  },
  {
    path: '/about',
    name: 'about',
    component: About
  }
];

const router = new VueRouter({
  mode: 'history',
  routes
});


  
export default router;