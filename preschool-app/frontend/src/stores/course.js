import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import { getCourses, getCourseDetail, getLessons, getProgress } from '@/api/course'

export const useCourseStore = defineStore('course', () => {
  const courses = ref([])
  const currentCourse = ref(null)
  const lessons = ref([])
  const progress = ref({})

  const chineseCourses = computed(() => courses.value.filter(c => c.subject === 'chinese'))
  const mathCourses = computed(() => courses.value.filter(c => c.subject === 'math'))
  const thinkingCourses = computed(() => courses.value.filter(c => c.subject === 'thinking'))
  const habitCourses = computed(() => courses.value.filter(c => c.subject === 'habit'))

  async function loadCourses() {
    const result = await getCourses()
    if (result.success) {
      courses.value = result.data
    }
  }

  async function loadCourseDetail(courseId) {
    const result = await getCourseDetail(courseId)
    if (result.success) {
      currentCourse.value = result.data
    }
  }

  async function loadLessons(courseId) {
    const result = await getLessons(courseId)
    if (result.success) {
      lessons.value = result.data
    }
  }

  async function loadProgress() {
    const result = await getProgress()
    if (result.success) {
      progress.value = result.data
    }
  }

  function getLessonProgress(lessonId) {
    return progress.value[lessonId] || 0
  }

  return {
    courses,
    currentCourse,
    lessons,
    progress,
    chineseCourses,
    mathCourses,
    thinkingCourses,
    habitCourses,
    loadCourses,
    loadCourseDetail,
    loadLessons,
    loadProgress,
    getLessonProgress
  }
})
