import axios from './axios'

export async function getCourses() {
  try {
    const response = await axios.get('/courses')
    return { success: true, data: response.data }
  } catch (error) {
    return { success: false, message: error.response?.data?.detail || '获取课程列表失败' }
  }
}

export async function getCourseDetail(courseId) {
  try {
    const response = await axios.get(`/courses/${courseId}`)
    return { success: true, data: response.data }
  } catch (error) {
    return { success: false, message: error.response?.data?.detail || '获取课程详情失败' }
  }
}

export async function getLessons(courseId) {
  try {
    const response = await axios.get(`/courses/${courseId}/lessons`)
    return { success: true, data: response.data }
  } catch (error) {
    return { success: false, message: error.response?.data?.detail || '获取课程章节失败' }
  }
}

export async function getLessonDetail(lessonId) {
  try {
    const response = await axios.get(`/lessons/${lessonId}`)
    return { success: true, data: response.data }
  } catch (error) {
    return { success: false, message: error.response?.data?.detail || '获取章节详情失败' }
  }
}

export async function updateProgress(lessonId, progress) {
  try {
    const response = await axios.post(`/lessons/${lessonId}/progress`, { progress })
    return { success: true, data: response.data }
  } catch (error) {
    return { success: false, message: error.response?.data?.detail || '更新进度失败' }
  }
}

export async function getProgress() {
  try {
    const response = await axios.get('/progress')
    return { success: true, data: response.data }
  } catch (error) {
    return { success: false, message: error.response?.data?.detail || '获取学习进度失败' }
  }
}
