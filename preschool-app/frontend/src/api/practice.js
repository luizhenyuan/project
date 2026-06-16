import axios from './axios'

export async function getQuestions(courseId) {
  try {
    const response = await axios.get(`/practice/${courseId}/questions`)
    return { success: true, data: response.data }
  } catch (error) {
    return { success: false, message: error.response?.data?.detail || '获取练习题失败' }
  }
}

export async function submitAnswer(questionId, answer) {
  try {
    const response = await axios.post(`/practice/questions/${questionId}/answer`, { answer })
    return { success: true, data: response.data }
  } catch (error) {
    return { success: false, message: error.response?.data?.detail || '提交答案失败' }
  }
}

export async function getWrongBook() {
  try {
    const response = await axios.get('/practice/wrong-book')
    return { success: true, data: response.data }
  } catch (error) {
    return { success: false, message: error.response?.data?.detail || '获取错题本失败' }
  }
}

export async function removeWrongQuestion(questionId) {
  try {
    const response = await axios.delete(`/practice/wrong-book/${questionId}`)
    return { success: true, data: response.data }
  } catch (error) {
    return { success: false, message: error.response?.data?.detail || '移除错题失败' }
  }
}

export async function getAchievements() {
  try {
    const response = await axios.get('/achievements')
    return { success: true, data: response.data }
  } catch (error) {
    return { success: false, message: error.response?.data?.detail || '获取成就失败' }
  }
}

export async function getStudyReport() {
  try {
    const response = await axios.get('/parent/report')
    return { success: true, data: response.data }
  } catch (error) {
    return { success: false, message: error.response?.data?.detail || '获取学习报告失败' }
  }
}

export async function getStudyTime() {
  try {
    const response = await axios.get('/parent/study-time')
    return { success: true, data: response.data }
  } catch (error) {
    return { success: false, message: error.response?.data?.detail || '获取学习时长失败' }
  }
}

export async function setTimeLimit(hours) {
  try {
    const response = await axios.post('/parent/time-limit', { hours })
    return { success: true, data: response.data }
  } catch (error) {
    return { success: false, message: error.response?.data?.detail || '设置时长限制失败' }
  }
}
