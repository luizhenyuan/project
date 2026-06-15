<template>
  <div class="page-container">
    <div class="page-header">
      <h1>家长中心</h1>
      <p>关注孩子的学习成长</p>
    </div>

    <div class="mode-toggle">
      <div 
        :class="['toggle-btn', { active: !isParentMode }]"
        @click="toggleMode"
      >
        👧 孩子模式
      </div>
      <div 
        :class="['toggle-btn', { active: isParentMode }]"
        @click="toggleMode"
      >
        👨‍👩‍👧 家长模式
      </div>
    </div>

    <div class="quick-stats">
      <div class="stat-card">
        <div class="stat-icon">📊</div>
        <div class="stat-info">
          <div class="stat-value">{{ todayStudyTime }}</div>
          <div class="stat-label">今日学习</div>
        </div>
      </div>
      <div class="stat-card">
        <div class="stat-icon">📈</div>
        <div class="stat-info">
          <div class="stat-value">{{ weeklyProgress }}%</div>
          <div class="stat-label">本周进度</div>
        </div>
      </div>
      <div class="stat-card">
        <div class="stat-icon">🏆</div>
        <div class="stat-info">
          <div class="stat-value">{{ achievements }}</div>
          <div class="stat-label">获得成就</div>
        </div>
      </div>
    </div>

    <div class="menu-list">
      <div class="menu-item" @click="goToStudyReport">
        <div class="menu-icon">📋</div>
        <div class="menu-content">
          <h4>学习报告</h4>
          <p>查看详细学习数据</p>
        </div>
        <div class="menu-arrow">→</div>
      </div>

      <div class="menu-item" @click="goToTimeLimit">
        <div class="menu-icon">⏱️</div>
        <div class="menu-content">
          <h4>时长管理</h4>
          <p>设置每日学习时长限制</p>
        </div>
        <div class="menu-arrow">→</div>
      </div>

      <div class="menu-item" @click="goToWrongBook">
        <div class="menu-icon">📝</div>
        <div class="menu-content">
          <h4>错题本</h4>
          <p>复习错题，巩固知识</p>
        </div>
        <div class="menu-arrow">→</div>
      </div>

      <div class="menu-item" @click="goToAchievements">
        <div class="menu-icon">🏅</div>
        <div class="menu-content">
          <h4>成就中心</h4>
          <p>查看孩子获得的成就</p>
        </div>
        <div class="menu-arrow">→</div>
      </div>

      <div class="menu-item" @click="goToNotifications">
        <div class="menu-icon">🔔</div>
        <div class="menu-content">
          <h4>学习提醒</h4>
          <p>设置学习提醒和通知</p>
        </div>
        <div class="menu-arrow">→</div>
      </div>

      <div class="menu-item" @click="goToContentFilter">
        <div class="menu-icon">🎯</div>
        <div class="menu-content">
          <h4>内容筛选</h4>
          <p>选择适合孩子的课程</p>
        </div>
        <div class="menu-arrow">→</div>
      </div>
    </div>

    <div class="tips-card">
      <div class="tips-icon">💡</div>
      <div class="tips-content">
        <h4>育儿小贴士</h4>
        <p>建议每天学习时间控制在30-45分钟，分两次进行，避免孩子疲劳。</p>
      </div>
    </div>

    <div class="bottom-nav">
      <div class="nav-item" @click="goToHome">
        <span class="nav-icon">🏠</span>
        <span class="nav-text">首页</span>
      </div>
      <div class="nav-item" @click="goToCourses">
        <span class="nav-icon">📚</span>
        <span class="nav-text">课程</span>
      </div>
      <div class="nav-item active" @click="goToParentCenter">
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
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useUserStore } from '@/stores/user'

const router = useRouter()
const userStore = useUserStore()

const isParentMode = ref(true)
const todayStudyTime = ref('35分钟')
const weeklyProgress = ref(85)
const achievements = ref(3)

function toggleMode() {
  isParentMode.value = !isParentMode.value
  userStore.toggleMode()
}

function goToStudyReport() {
  router.push('/study-report')
}

function goToTimeLimit() {
  alert('时长管理功能开发中')
}

function goToWrongBook() {
  router.push('/wrong-book')
}

function goToAchievements() {
  router.push('/achievements')
}

function goToNotifications() {
  alert('学习提醒功能开发中')
}

function goToContentFilter() {
  alert('内容筛选功能开发中')
}

function goToHome() { router.push('/') }
function goToCourses() { router.push('/courses') }
function goToParentCenter() { router.push('/parent-center') }
function goToSettings() { router.push('/settings') }
</script>

<style scoped>
.mode-toggle {
  display: flex;
  margin: 15px;
  background: #fff;
  border-radius: 12px;
  overflow: hidden;
}

.toggle-btn {
  flex: 1;
  padding: 15px;
  text-align: center;
  font-size: 14px;
  background: #f5f7fa;
  color: #6c757d;
  cursor: pointer;
  transition: all 0.3s;
}

.toggle-btn.active {
  background: #4a90e2;
  color: #fff;
}

.quick-stats {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 10px;
  padding: 0 15px;
  margin-bottom: 20px;
}

.stat-card {
  background: #fff;
  border-radius: 12px;
  padding: 15px;
  text-align: center;
}

.stat-icon {
  font-size: 24px;
  margin-bottom: 8px;
}

.stat-value {
  font-size: 20px;
  font-weight: 700;
  color: #4a90e2;
}

.stat-label {
  font-size: 11px;
  color: #6c757d;
}

.menu-list {
  background: #fff;
  margin: 0 15px;
  border-radius: 16px;
  overflow: hidden;
}

.menu-item {
  display: flex;
  align-items: center;
  padding: 15px;
  border-bottom: 1px solid #f0f2f5;
  cursor: pointer;
}

.menu-item:last-child {
  border-bottom: none;
}

.menu-icon {
  font-size: 24px;
  margin-right: 15px;
}

.menu-content h4 {
  font-size: 15px;
  font-weight: 600;
  color: #2c3e50;
  margin-bottom: 3px;
}

.menu-content p {
  font-size: 12px;
  color: #6c757d;
}

.menu-arrow {
  margin-left: auto;
  color: #95a5a6;
}

.tips-card {
  display: flex;
  gap: 15px;
  background: linear-gradient(135deg, #fff3cd 0%, #ffeeba 100%);
  margin: 15px;
  padding: 15px;
  border-radius: 12px;
  border: 1px solid #ffeeba;
}

.tips-icon {
  font-size: 28px;
}

.tips-content h4 {
  font-size: 14px;
  font-weight: 600;
  color: #856404;
  margin-bottom: 5px;
}

.tips-content p {
  font-size: 13px;
  color: #856404;
  line-height: 1.5;
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
