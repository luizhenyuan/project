<template>
  <div class="page-container">
    <div class="course-header">
      <div class="back-btn" @click="goBack">←</div>
      <h1>{{ course.title }}</h1>
    </div>

    <div class="course-hero">
      <div class="hero-bg"></div>
      <div class="hero-content">
        <span class="hero-icon">{{ getSubjectIcon(course.subject) }}</span>
        <h2>{{ course.title }}</h2>
        <p>{{ course.description }}</p>
        <div class="hero-stats">
          <span>{{ course.lesson_count }}节课</span>
          <span>{{ totalProgress }}%完成</span>
        </div>
      </div>
    </div>

    <div class="lesson-section">
      <div class="section-header">
        <h3>课程目录</h3>
        <span>{{ completedCount }}/{{ course.lesson_count }}</span>
      </div>

      <div class="progress-bar-container">
        <div class="progress-bar-bg">
          <div class="progress-bar-fill" :style="{ width: totalProgress + '%' }"></div>
        </div>
      </div>

      <div class="lesson-list">
        <div 
          v-for="(lesson, index) in lessons" 
          :key="lesson.id"
          :class="['lesson-item', { completed: lesson.completed, current: index === 0 && !lesson.completed }]"
          @click="goToLearning(course.id, lesson.id)"
        >
          <div class="lesson-status">
            <span v-if="lesson.completed">✓</span>
            <span v-else-if="index === 0 && !lessons[0].completed">▶</span>
            <span v-else>{{ index + 1 }}</span>
          </div>
          <div class="lesson-info">
            <h4>{{ lesson.title }}</h4>
            <p>{{ lesson.duration }}分钟</p>
          </div>
          <div class="lesson-action">
            <span v-if="lesson.completed">已完成</span>
            <span v-else>开始学习</span>
          </div>
        </div>
      </div>
    </div>

    <button class="btn-start" @click="startCourse">
      {{ hasProgress ? '继续学习' : '开始学习' }}
    </button>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'

const router = useRouter()
const route = useRoute()

const course = ref({
  id: 1,
  title: '拼音入门',
  description: '学习声母、韵母和整体认读音节，掌握拼音规则',
  subject: 'chinese',
  lesson_count: 10
})

const lessons = ref([
  { id: 1, title: '认识声母 b p m f', duration: 10, completed: true },
  { id: 2, title: '认识声母 d t n l', duration: 10, completed: true },
  { id: 3, title: '认识声母 g k h', duration: 10, completed: true },
  { id: 4, title: '认识声母 j q x', duration: 10, completed: false },
  { id: 5, title: '认识韵母 a o e', duration: 10, completed: false },
  { id: 6, title: '认识韵母 i u ü', duration: 10, completed: false },
  { id: 7, title: '复韵母学习', duration: 12, completed: false },
  { id: 8, title: '整体认读音节', duration: 12, completed: false },
  { id: 9, title: '声调练习', duration: 10, completed: false },
  { id: 10, title: '拼音综合练习', duration: 15, completed: false }
])

const completedCount = computed(() => lessons.value.filter(l => l.completed).length)
const totalProgress = computed(() => Math.round((completedCount.value / lessons.value.length) * 100))
const hasProgress = computed(() => completedCount.value > 0)

function getSubjectIcon(subject) {
  const icons = {
    chinese: '📖',
    math: '🔢',
    thinking: '🧠',
    habit: '⭐'
  }
  return icons[subject] || '📚'
}

function goBack() {
  router.back()
}

function goToLearning(courseId, lessonId) {
  router.push(`/learning/${courseId}/${lessonId}`)
}

function startCourse() {
  const nextLesson = lessons.value.find(l => !l.completed) || lessons.value[0]
  goToLearning(course.value.id, nextLesson.id)
}

onMounted(() => {
  const courseId = parseInt(route.params.id)
  if (courseId) {
    course.value.id = courseId
  }
})
</script>

<style scoped>
.course-header {
  background: linear-gradient(135deg, #4a90e2 0%, #667eea 100%);
  padding: 15px 20px;
  display: flex;
  align-items: center;
  color: #fff;
}

.back-btn {
  font-size: 24px;
  margin-right: 15px;
  cursor: pointer;
}

.course-header h1 {
  font-size: 18px;
  font-weight: 600;
}

.course-hero {
  position: relative;
  padding: 30px 20px;
  color: #fff;
}

.hero-bg {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(135deg, #4a90e2 0%, #667eea 100%);
  border-radius: 0 0 30px 30px;
}

.hero-content {
  position: relative;
  z-index: 1;
  text-align: center;
}

.hero-icon {
  font-size: 60px;
  margin-bottom: 15px;
}

.hero-content h2 {
  font-size: 22px;
  font-weight: 600;
  margin-bottom: 8px;
}

.hero-content p {
  font-size: 14px;
  opacity: 0.9;
  margin-bottom: 15px;
}

.hero-stats {
  display: flex;
  justify-content: center;
  gap: 20px;
  font-size: 13px;
}

.lesson-section {
  background: #fff;
  margin: -20px 15px 15px;
  padding: 20px;
  border-radius: 20px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.section-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 15px;
}

.section-header h3 {
  font-size: 16px;
  font-weight: 600;
  color: #2c3e50;
}

.section-header span {
  font-size: 13px;
  color: #4a90e2;
}

.progress-bar-container {
  margin-bottom: 20px;
}

.progress-bar-bg {
  height: 8px;
  background: #f0f2f5;
  border-radius: 4px;
  overflow: hidden;
}

.progress-bar-fill {
  height: 100%;
  background: linear-gradient(90deg, #4a90e2 0%, #667eea 100%);
  border-radius: 4px;
  transition: width 0.3s;
}

.lesson-list {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.lesson-item {
  display: flex;
  align-items: center;
  padding: 15px;
  background: #f8f9fa;
  border-radius: 12px;
  cursor: pointer;
  transition: all 0.3s;
}

.lesson-item:hover {
  background: #e9ecef;
}

.lesson-item.completed {
  opacity: 0.7;
}

.lesson-item.current {
  background: linear-gradient(135deg, #e8f0fe 0%, #e0e7ff 100%);
  border: 1px solid #4a90e2;
}

.lesson-status {
  width: 36px;
  height: 36px;
  border-radius: 50%;
  background: #4a90e2;
  color: #fff;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 14px;
  font-weight: 600;
  margin-right: 15px;
}

.lesson-item.completed .lesson-status {
  background: #27ae60;
}

.lesson-item.current .lesson-status {
  background: #f39c12;
}

.lesson-info {
  flex: 1;
}

.lesson-info h4 {
  font-size: 15px;
  font-weight: 500;
  color: #2c3e50;
  margin-bottom: 3px;
}

.lesson-info p {
  font-size: 12px;
  color: #6c757d;
}

.lesson-action {
  font-size: 12px;
  color: #4a90e2;
}

.btn-start {
  position: fixed;
  bottom: 20px;
  left: 15px;
  right: 15px;
  height: 55px;
  background: linear-gradient(135deg, #4a90e2 0%, #667eea 100%);
  color: #fff;
  border: none;
  border-radius: 16px;
  font-size: 18px;
  font-weight: 600;
  cursor: pointer;
  box-shadow: 0 4px 12px rgba(74, 144, 226, 0.3);
}
</style>
