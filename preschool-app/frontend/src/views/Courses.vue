<template>
  <div class="page-container">
    <div class="page-header">
      <h1>课程中心</h1>
      <p>选择感兴趣的课程开始学习</p>
    </div>

    <div class="category-tabs">
      <div 
        v-for="tab in tabs" 
        :key="tab.key"
        :class="['tab-item', { active: activeTab === tab.key }]"
        @click="activeTab = tab.key"
      >
        {{ tab.icon }} {{ tab.label }}
      </div>
    </div>

    <div class="course-grid">
      <div 
        v-for="course in filteredCourses" 
        :key="course.id" 
        class="course-card"
        @click="goToCourseDetail(course.id)"
      >
        <div class="course-cover">
          <span class="cover-icon">{{ getSubjectIcon(course.subject) }}</span>
        </div>
        <div class="course-content">
          <h3>{{ course.title }}</h3>
          <p>{{ course.description }}</p>
          <div class="course-footer">
            <span>{{ course.lesson_count }}节课</span>
            <span class="progress">
              <span>{{ getProgress(course.id) }}%</span>
            </span>
          </div>
        </div>
        <div 
          v-if="getProgress(course.id) > 0" 
          class="progress-bar"
          :style="{ width: getProgress(course.id) + '%' }"
        ></div>
      </div>
    </div>

    <div class="bottom-nav">
      <div class="nav-item" @click="goToHome">
        <span class="nav-icon">🏠</span>
        <span class="nav-text">首页</span>
      </div>
      <div class="nav-item active" @click="goToCourses">
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
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

const activeTab = ref('all')

const tabs = [
  { key: 'all', label: '全部', icon: '📖' },
  { key: 'chinese', label: '语文', icon: '📝' },
  { key: 'math', label: '数学', icon: '🔢' },
  { key: 'thinking', label: '思维', icon: '🧠' },
  { key: 'habit', label: '习惯', icon: '⭐' }
]

const courses = ref([
  { id: 1, title: '拼音入门', description: '学习声母、韵母和整体认读音节', subject: 'chinese', lesson_count: 10 },
  { id: 2, title: '汉字启蒙', description: '认识常用汉字，学习笔画笔顺', subject: 'chinese', lesson_count: 15 },
  { id: 3, title: '趣味阅读', description: '培养阅读兴趣，理解简单故事', subject: 'chinese', lesson_count: 8 },
  { id: 4, title: '数字认知', description: '认识1-100数字，建立数感', subject: 'math', lesson_count: 8 },
  { id: 5, title: '加减法入门', description: '20以内加减法基础', subject: 'math', lesson_count: 12 },
  { id: 6, title: '图形认知', description: '认识常见图形和立体形状', subject: 'math', lesson_count: 6 },
  { id: 7, title: '专注力训练', description: '提升注意力和观察力', subject: 'thinking', lesson_count: 6 },
  { id: 8, title: '记忆力游戏', description: '通过游戏锻炼记忆力', subject: 'thinking', lesson_count: 5 },
  { id: 9, title: '逻辑推理', description: '培养逻辑思维能力', subject: 'thinking', lesson_count: 6 },
  { id: 10, title: '好习惯养成', description: '培养良好的学习和生活习惯', subject: 'habit', lesson_count: 5 },
  { id: 11, title: '时间管理', description: '学会认识时间和管理时间', subject: 'habit', lesson_count: 4 },
  { id: 12, title: '社交礼仪', description: '学习基本社交礼仪', subject: 'habit', lesson_count: 4 }
])

const progressMap = { 1: 60, 2: 30, 3: 0, 4: 40, 5: 20, 6: 80, 7: 50, 8: 0, 9: 10, 10: 25, 11: 70, 12: 0 }

const filteredCourses = computed(() => {
  if (activeTab.value === 'all') return courses.value
  return courses.value.filter(c => c.subject === activeTab.value)
})

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
function goToParentCenter() { router.push('/parent-center') }
function goToSettings() { router.push('/settings') }
function goToCourseDetail(id) { router.push(`/course/${id}`) }
</script>

<style scoped>
.category-tabs {
  display: flex;
  overflow-x: auto;
  padding: 15px;
  gap: 10px;
  background: #fff;
  border-bottom: 1px solid #e9ecef;
}

.tab-item {
  flex-shrink: 0;
  padding: 10px 16px;
  background: #f5f7fa;
  border-radius: 20px;
  font-size: 14px;
  color: #6c757d;
  white-space: nowrap;
}

.tab-item.active {
  background: #4a90e2;
  color: #fff;
}

.course-grid {
  padding: 15px;
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.course-card {
  background: #fff;
  border-radius: 16px;
  overflow: hidden;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
  position: relative;
}

.course-cover {
  height: 120px;
  background: linear-gradient(135deg, #4a90e2 0%, #667eea 100%);
  display: flex;
  align-items: center;
  justify-content: center;
}

.cover-icon {
  font-size: 50px;
}

.course-content {
  padding: 15px;
}

.course-content h3 {
  font-size: 16px;
  font-weight: 600;
  color: #2c3e50;
  margin-bottom: 5px;
}

.course-content p {
  font-size: 13px;
  color: #6c757d;
  margin-bottom: 10px;
}

.course-footer {
  display: flex;
  justify-content: space-between;
  font-size: 12px;
  color: #95a5a6;
}

.progress {
  color: #4a90e2;
  font-weight: 600;
}

.progress-bar {
  position: absolute;
  bottom: 0;
  left: 0;
  height: 4px;
  background: linear-gradient(90deg, #4a90e2 0%, #667eea 100%);
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
