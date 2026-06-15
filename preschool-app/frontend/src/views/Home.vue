<template>
  <div class="page-container">
    <div class="hero-section">
      <div class="hero-content">
        <h1>幼小衔接</h1>
        <p>快乐学习，轻松成长</p>
        <div class="hero-avatar">📚</div>
      </div>
    </div>

    <div class="stats-section">
      <div class="stat-item">
        <div class="stat-value">{{ totalCourses }}</div>
        <div class="stat-label">课程总数</div>
      </div>
      <div class="stat-item">
        <div class="stat-value">{{ completedLessons }}</div>
        <div class="stat-label">已学课程</div>
      </div>
      <div class="stat-item">
        <div class="stat-value">{{ studyDays }}</div>
        <div class="stat-label">学习天数</div>
      </div>
    </div>

    <div class="quick-actions">
      <div class="action-card" @click="goToCourses">
        <div class="action-icon">📖</div>
        <div class="action-text">开始学习</div>
      </div>
      <div class="action-card" @click="goToPractice">
        <div class="action-icon">✏️</div>
        <div class="action-text">在线练习</div>
      </div>
      <div class="action-card" @click="goToParentCenter">
        <div class="action-icon">👨‍👩‍👧</div>
        <div class="action-text">家长中心</div>
      </div>
      <div class="action-card" @click="goToAchievements">
        <div class="action-icon">🏆</div>
        <div class="action-text">成就中心</div>
      </div>
    </div>

    <div class="section">
      <div class="section-header">
        <h2>推荐课程</h2>
        <span class="section-more" @click="goToCourses">查看全部 →</span>
      </div>
      <div class="course-list">
        <div 
          v-for="course in recommendCourses" 
          :key="course.id" 
          class="course-item"
          @click="goToCourseDetail(course.id)"
        >
          <div class="course-cover">{{ getSubjectIcon(course.subject) }}</div>
          <div class="course-info">
            <h3>{{ course.title }}</h3>
            <p>{{ course.description }}</p>
            <div class="course-meta">
              <span>{{ course.lesson_count }}节课</span>
              <span>{{ getProgress(course.id) }}%完成</span>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="section">
      <div class="section-header">
        <h2>学习统计</h2>
      </div>
      <div class="study-stats">
        <div class="study-card">
          <div class="study-icon">⏱️</div>
          <div class="study-info">
            <div class="study-value">{{ todayStudyTime }}</div>
            <div class="study-label">今日学习</div>
          </div>
        </div>
        <div class="study-card">
          <div class="study-icon">📊</div>
          <div class="study-info">
            <div class="study-value">{{ weeklyProgress }}</div>
            <div class="study-label">本周进度</div>
          </div>
        </div>
      </div>
    </div>

    <div class="bottom-nav">
      <div class="nav-item active" @click="goToHome">
        <span class="nav-icon">🏠</span>
        <span class="nav-text">首页</span>
      </div>
      <div class="nav-item" @click="goToCourses">
        <span class="nav-icon">📚</span>
        <span class="nav-text">课程</span>
      </div>
      <div class="nav-item" @click="goToParentCenter">
        <span class="nav-icon">👨‍👩‍👧</span>
        <span class="nav-text">家长</span>
      </div>
      <div class="nav-item" @click="goToSettings">
        <span class="nav-icon">⚙️</span>
        <span class="nav-text">设置</span>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useCourseStore } from '@/stores/course'

const router = useRouter()
const courseStore = useCourseStore()

const totalCourses = ref(40)
const completedLessons = ref(12)
const studyDays = ref(15)
const todayStudyTime = ref('35分钟')
const weeklyProgress = ref('85%')

const recommendCourses = ref([
  { id: 1, title: '拼音入门', description: '学习声母、韵母和整体认读音节', subject: 'chinese', lesson_count: 10 },
  { id: 2, title: '数字认知', description: '认识1-100数字，建立数感', subject: 'math', lesson_count: 8 },
  { id: 3, title: '专注力训练', description: '提升注意力和观察力', subject: 'thinking', lesson_count: 6 },
  { id: 4, title: '好习惯养成', description: '培养良好的学习和生活习惯', subject: 'habit', lesson_count: 5 }
])

const progressMap = { 1: 60, 2: 40, 3: 80, 4: 20 }

function getSubjectIcon(subject) {
  const icons = {
    chinese: '📖',
    math: '🔢',
    thinking: '🧠',
    habit: '⭐'
  }
  return icons[subject] || '📚'
}

function getProgress(courseId) {
  return progressMap[courseId] || 0
}

function goToHome() { router.push('/') }
function goToCourses() { router.push('/courses') }
function goToPractice() { router.push('/practice/1') }
function goToParentCenter() { router.push('/parent-center') }
function goToAchievements() { router.push('/achievements') }
function goToSettings() { router.push('/settings') }
function goToCourseDetail(id) { router.push(`/course/${id}`) }

onMounted(async () => {
  await courseStore.loadCourses()
})
</script>

<style scoped>
.hero-section {
  background: linear-gradient(135deg, #4a90e2 0%, #667eea 100%);
  padding: 40px 20px;
  border-radius: 0 0 30px 30px;
  color: #fff;
}

.hero-content {
  text-align: center;
}

.hero-content h1 {
  font-size: 28px;
  font-weight: 700;
  margin-bottom: 5px;
}

.hero-content p {
  font-size: 14px;
  opacity: 0.9;
  margin-bottom: 20px;
}

.hero-avatar {
  width: 80px;
  height: 80px;
  margin: 0 auto;
  background: rgba(255, 255, 255, 0.2);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 40px;
}

.stats-section {
  display: flex;
  justify-content: space-around;
  background: #fff;
  margin: -25px 15px 15px;
  padding: 20px;
  border-radius: 16px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.stat-item {
  text-align: center;
}

.stat-value {
  font-size: 24px;
  font-weight: 700;
  color: #4a90e2;
}

.stat-label {
  font-size: 12px;
  color: #6c757d;
  margin-top: 4px;
}

.quick-actions {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 10px;
  padding: 0 15px;
  margin-bottom: 20px;
}

.action-card {
  background: #fff;
  border-radius: 12px;
  padding: 15px 10px;
  text-align: center;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
}

.action-icon {
  font-size: 28px;
  margin-bottom: 5px;
}

.action-text {
  font-size: 12px;
  color: #2c3e50;
}

.section {
  padding: 0 15px;
  margin-bottom: 20px;
}

.section-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 15px;
}

.section-header h2 {
  font-size: 16px;
  font-weight: 600;
  color: #2c3e50;
}

.section-more {
  font-size: 13px;
  color: #4a90e2;
}

.course-list {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.course-item {
  background: #fff;
  border-radius: 12px;
  padding: 15px;
  display: flex;
  gap: 15px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
}

.course-cover {
  width: 60px;
  height: 60px;
  border-radius: 12px;
  background: linear-gradient(135deg, #4a90e2 0%, #667eea 100%);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 28px;
  flex-shrink: 0;
}

.course-info {
  flex: 1;
  min-width: 0;
}

.course-info h3 {
  font-size: 15px;
  font-weight: 600;
  color: #2c3e50;
  margin-bottom: 4px;
}

.course-info p {
  font-size: 12px;
  color: #6c757d;
  margin-bottom: 8px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.course-meta {
  display: flex;
  gap: 15px;
  font-size: 11px;
  color: #95a5a6;
}

.study-stats {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 10px;
}

.study-card {
  background: #fff;
  border-radius: 12px;
  padding: 15px;
  display: flex;
  align-items: center;
  gap: 15px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
}

.study-icon {
  font-size: 28px;
}

.study-value {
  font-size: 20px;
  font-weight: 700;
  color: #4a90e2;
}

.study-label {
  font-size: 12px;
  color: #6c757d;
}

.bottom-nav {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  background: #fff;
  display: flex;
  justify-content: space-around;
  padding: 10px 0 20px;
  box-shadow: 0 -2px 10px rgba(0, 0, 0, 0.05);
}

.nav-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 3px;
}

.nav-icon {
  font-size: 22px;
}

.nav-text {
  font-size: 11px;
  color: #6c757d;
}

.nav-item.active .nav-text {
  color: #4a90e2;
}
</style>
