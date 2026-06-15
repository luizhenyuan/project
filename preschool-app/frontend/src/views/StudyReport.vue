<template>
  <div class="page-container">
    <div class="report-header">
      <div class="back-btn" @click="goBack">←</div>
      <h1>学习报告</h1>
    </div>

    <div class="time-selector">
      <div 
        :class="['time-btn', { active: timeRange === 'week' }]"
        @click="timeRange = 'week'"
      >本周</div>
      <div 
        :class="['time-btn', { active: timeRange === 'month' }]"
        @click="timeRange = 'month'"
      >本月</div>
      <div 
        :class="['time-btn', { active: timeRange === 'year' }]"
        @click="timeRange = 'year'"
      >本年</div>
    </div>

    <div class="summary-card">
      <div class="summary-title">
        <span class="summary-icon">📊</span>
        <span>学习概览</span>
      </div>
      <div class="summary-stats">
        <div class="summary-item">
          <span class="summary-value">{{ totalStudyTime }}</span>
          <span class="summary-label">学习时长</span>
        </div>
        <div class="summary-divider"></div>
        <div class="summary-item">
          <span class="summary-value">{{ completedLessons }}</span>
          <span class="summary-label">完成课程</span>
        </div>
        <div class="summary-divider"></div>
        <div class="summary-item">
          <span class="summary-value">{{ avgAccuracy }}%</span>
          <span class="summary-label">平均正确率</span>
        </div>
      </div>
    </div>

    <div class="chart-card">
      <h3 class="chart-title">📈 学习趋势</h3>
      <div class="chart-container">
        <div class="chart-bars">
          <div v-for="(day, index) in weekDays" :key="index" class="bar-item">
            <div class="bar-wrapper">
              <div class="bar" :style="{ height: getBarHeight(day.hours) + '%' }"></div>
            </div>
            <span class="bar-label">{{ day.name }}</span>
          </div>
        </div>
      </div>
    </div>

    <div class="subject-card">
      <h3 class="subject-title">📚 学科分布</h3>
      <div class="subject-list">
        <div v-for="subject in subjects" :key="subject.name" class="subject-item">
          <div class="subject-header">
            <span class="subject-icon">{{ subject.icon }}</span>
            <span class="subject-name">{{ subject.name }}</span>
          </div>
          <div class="subject-progress">
            <div class="progress-bar-bg">
              <div class="progress-bar-fill" :style="{ width: subject.percentage + '%' }"></div>
            </div>
            <span class="progress-text">{{ subject.hours }}小时</span>
          </div>
        </div>
      </div>
    </div>

    <div class="achievements-card">
      <h3 class="achievements-title">🏆 近期成就</h3>
      <div class="achievements-list">
        <div v-for="achievement in recentAchievements" :key="achievement.id" class="achievement-item">
          <span class="achievement-icon">{{ achievement.icon }}</span>
          <div class="achievement-info">
            <span class="achievement-name">{{ achievement.name }}</span>
            <span class="achievement-date">{{ achievement.date }}</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

const timeRange = ref('week')
const totalStudyTime = ref('12.5小时')
const completedLessons = ref(12)
const avgAccuracy = ref(85)

const weekDays = ref([
  { name: '周一', hours: 2.5 },
  { name: '周二', hours: 1.8 },
  { name: '周三', hours: 3.2 },
  { name: '周四', hours: 2.0 },
  { name: '周五', hours: 1.5 },
  { name: '周六', hours: 3.8 },
  { name: '周日', hours: 2.2 }
])

const subjects = ref([
  { name: '语文', icon: '📖', hours: 4.5, percentage: 36 },
  { name: '数学', icon: '🔢', hours: 3.8, percentage: 30 },
  { name: '思维', icon: '🧠', hours: 2.5, percentage: 20 },
  { name: '习惯', icon: '⭐', hours: 1.7, percentage: 14 }
])

const recentAchievements = ref([
  { id: 1, name: '学习达人', icon: '🔥', date: '2024-01-17' },
  { id: 2, name: '全能王', icon: '⭐', date: '2024-01-15' },
  { id: 3, name: '初学者', icon: '🌱', date: '2024-01-10' }
])

function getBarHeight(hours) {
  const maxHours = Math.max(...weekDays.value.map(d => d.hours))
  return (hours / maxHours) * 100
}

function goBack() {
  router.back()
}
</script>

<style scoped>
.report-header {
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

.report-header h1 {
  font-size: 18px;
  font-weight: 600;
}

.time-selector {
  display: flex;
  gap: 10px;
  padding: 15px;
  background: #fff;
}

.time-btn {
  flex: 1;
  padding: 12px;
  text-align: center;
  background: #f5f7fa;
  border-radius: 10px;
  font-size: 14px;
  color: #6c757d;
  cursor: pointer;
}

.time-btn.active {
  background: #4a90e2;
  color: #fff;
}

.summary-card {
  background: linear-gradient(135deg, #4a90e2 0%, #667eea 100%);
  margin: 15px;
  padding: 20px;
  border-radius: 16px;
  color: #fff;
}

.summary-title {
  display: flex;
  align-items: center;
  margin-bottom: 15px;
}

.summary-icon {
  font-size: 24px;
  margin-right: 10px;
}

.summary-title span:last-child {
  font-size: 16px;
  font-weight: 600;
}

.summary-stats {
  display: flex;
  justify-content: space-around;
}

.summary-item {
  text-align: center;
}

.summary-value {
  font-size: 28px;
  font-weight: 700;
}

.summary-label {
  font-size: 12px;
  opacity: 0.9;
}

.summary-divider {
  width: 1px;
  background: rgba(255, 255, 255, 0.3);
}

.chart-card {
  background: #fff;
  margin: 15px;
  padding: 20px;
  border-radius: 16px;
}

.chart-title {
  font-size: 16px;
  font-weight: 600;
  color: #2c3e50;
  margin-bottom: 20px;
}

.chart-bars {
  display: flex;
  justify-content: space-between;
  align-items: flex-end;
  height: 150px;
  padding: 0 10px;
}

.bar-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  flex: 1;
}

.bar-wrapper {
  width: 24px;
  height: 120px;
  background: #f0f2f5;
  border-radius: 12px;
  display: flex;
  align-items: flex-end;
  overflow: hidden;
}

.bar {
  width: 100%;
  background: linear-gradient(180deg, #4a90e2 0%, #667eea 100%);
  border-radius: 12px;
  transition: height 0.3s;
}

.bar-label {
  font-size: 11px;
  color: #6c757d;
  margin-top: 8px;
}

.subject-card {
  background: #fff;
  margin: 15px;
  padding: 20px;
  border-radius: 16px;
}

.subject-title {
  font-size: 16px;
  font-weight: 600;
  color: #2c3e50;
  margin-bottom: 15px;
}

.subject-list {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.subject-item {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.subject-header {
  display: flex;
  align-items: center;
}

.subject-icon {
  font-size: 20px;
  margin-right: 10px;
}

.subject-name {
  font-size: 14px;
  font-weight: 500;
  color: #2c3e50;
}

.subject-progress {
  display: flex;
  align-items: center;
  gap: 10px;
}

.progress-bar-bg {
  flex: 1;
  height: 8px;
  background: #f0f2f5;
  border-radius: 4px;
  overflow: hidden;
}

.progress-bar-fill {
  height: 100%;
  background: linear-gradient(90deg, #4a90e2 0%, #667eea 100%);
  border-radius: 4px;
}

.progress-text {
  font-size: 12px;
  color: #6c757d;
  white-space: nowrap;
}

.achievements-card {
  background: #fff;
  margin: 15px 15px 100px;
  padding: 20px;
  border-radius: 16px;
}

.achievements-title {
  font-size: 16px;
  font-weight: 600;
  color: #2c3e50;
  margin-bottom: 15px;
}

.achievements-list {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.achievement-item {
  display: flex;
  align-items: center;
  gap: 12px;
}

.achievement-icon {
  font-size: 28px;
}

.achievement-info {
  display: flex;
  flex-direction: column;
}

.achievement-name {
  font-size: 14px;
  font-weight: 500;
  color: #2c3e50;
}

.achievement-date {
  font-size: 11px;
  color: #6c757d;
}
</style>
