import axios from './axios'

export async function login(username, password) {
  try {
    const response = await axios.post('/auth/login', { username, password })
    return { success: true, data: response.data }
  } catch (error) {
    return { success: false, message: error.response?.data?.detail || '登录失败' }
  }
}

export async function register(username, password, phone) {
  try {
    const response = await axios.post('/auth/register', { username, password, phone })
    return { success: true, data: response.data }
  } catch (error) {
    return { success: false, message: error.response?.data?.detail || '注册失败' }
  }
}

export async function getUserInfo() {
  try {
    const response = await axios.get('/auth/me')
    return { success: true, data: response.data }
  } catch (error) {
    return { success: false, message: error.response?.data?.detail || '获取用户信息失败' }
  }
}

export async function updateUserInfo(data) {
  try {
    const response = await axios.put('/auth/me', data)
    return { success: true, data: response.data }
  } catch (error) {
    return { success: false, message: error.response?.data?.detail || '更新用户信息失败' }
  }
}
