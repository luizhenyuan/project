import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('@/views/Home.vue')
  },
  {
    path: '/login',
    name: 'Login',
    component: () => import('@/views/Login.vue')
  },
  {
    path: '/register',
    name: 'Register',
    component: () => import('@/views/Register.vue')
  },
  {
    path: '/courses',
    name: 'Courses',
    component: () => import('@/views/Courses.vue')
  },
  {
    path: '/course/:id',
    name: 'CourseDetail',
    component: () => import('@/views/CourseDetail.vue')
  },
  {
    path: '/learning/:courseId/:lessonId',
    name: 'Learning',
    component: () => import('@/views/Learning.vue')
  },
  {
    path: '/practice/:courseId',
    name: 'Practice',
    component: () => import('@/views/Practice.vue')
  },
  {
    path: '/wrong-book',
    name: 'WrongBook',
    component: () => import('@/views/WrongBook.vue')
  },
  {
    path: '/achievements',
    name: 'Achievements',
    component: () => import('@/views/Achievements.vue')
  },
  {
    path: '/parent-center',
    name: 'ParentCenter',
    component: () => import('@/views/ParentCenter.vue')
  },
  {
    path: '/study-report',
    name: 'StudyReport',
    component: () => import('@/views/StudyReport.vue')
  },
  {
    path: '/settings',
    name: 'Settings',
    component: () => import('@/views/Settings.vue')
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
