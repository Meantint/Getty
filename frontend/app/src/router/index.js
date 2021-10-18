import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path: '/bankerLoan',
    name: 'BankerLoan',
    component: () => import('../views/BankerLoan.vue')
  },
  {
    path: '/usercheck',
    name: 'UserCheck',
    component: () => import('../components/Banker/UserCheck.vue')
  },
  {
    path: '/filecheck',
    name: 'FileCheck',
    component: () => import('../components/Banker/FileCheck.vue')
  },
  {
    path: '/applyDetail',
    name: 'ApplyDetail',
    component: () => import('../components/User/ApplyDetail.vue')
  },
  {
    path: '/loanList',
    name: 'LoanList',
    component: () => import('../components/User/LoanList.vue')
  },
  {
    path: '/productApply',
    name: 'ProductApply',
    component: () => import('../components/User/ProductApply.vue')
  },
  {
    path: '/signup',
    name: 'SignupMerge',
    component: () => import('../views/SignupMerge.vue')
  },
  {
    path: '/mypage',
    name: 'Mypage',
    component: () => import('../components/Main/Mypage.vue')
  },
  {
    path: '/submitDoc',
    name: 'SubmitDoc',
    component: () => import('../components/User/Submit.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
