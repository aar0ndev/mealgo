import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/views/Home.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/login',
      name: 'login',
      component: () => import(/* webpackChunkName: "login" */ './views/Login.vue')
    },
    {
      path: '/signup',
      name: 'signup',
      component: () => import(/* webpackChunkName: "signup" */ './views/SignUp.vue')
    },
    {
      path: '/planner',
      name: 'planner',
      component: () => import(/* webpackChunkName: "planner" */ './views/Planner.vue')
    },
    {
      path: '/recipes',
      name: 'recipes',
      component: () => import(/* webpackChunkName: "recipes" */ './views/Recipes.vue')
    },
    {
      path: '/shopping',
      name: 'shopping',
      component: () => import(/* webpackChunkName: "shopping" */ './views/Shopping.vue')
    }
  ]
})
