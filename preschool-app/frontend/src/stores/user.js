import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import { login, register, getUserInfo } from '@/api/user'

export const useUserStore = defineStore('user', () => {
  const userInfo = ref(null)
  const token = ref(localStorage.getItem('token') || '')
  const isParentMode = ref(true)

  const isLoggedIn = computed(() => !!token.value && !!userInfo.value)

  async function loginAction(username, password) {
    const result = await login(username, password)
    if (result.success) {
      token.value = result.data.token
      localStorage.setItem('token', token.value)
      userInfo.value = result.data.user
      return true
    }
    return false
  }

  async function registerAction(username, password, phone) {
    const result = await register(username, password, phone)
    if (result.success) {
      return true
    }
    return false
  }

  async function getUserInfoAction() {
    if (token.value) {
      const result = await getUserInfo()
      if (result.success) {
        userInfo.value = result.data
      }
    }
  }

  function logout() {
    token.value = ''
    userInfo.value = null
    localStorage.removeItem('token')
  }

  function toggleMode() {
    isParentMode.value = !isParentMode.value
  }

  return {
    userInfo,
    token,
    isParentMode,
    isLoggedIn,
    loginAction,
    registerAction,
    getUserInfoAction,
    logout,
    toggleMode
  }
})
