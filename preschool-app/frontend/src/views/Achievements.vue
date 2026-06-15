<template>
  <div class="page-container">
    <div class="page-header">
      <h1>成就中心</h1>
      <p>收集徽章，记录成长</p>
    </div>

    <div class="stats-card">
      <div class="stats-header">
        <span class="stats-icon">🏆</span>
        <span class="stats-title">我的成就</span>
      </div>
      <div class="stats-content">
        <div class="stat-item">
          <span class="stat-value">{{ unlockedCount }}</span>
          <span class="stat-label">已解锁</span>
        </div>
        <div class="stat-divider"></div>
        <div class="stat-item">
          <span class="stat-value">{{ totalCount }}</span>
          <span class="stat-label">总计</span>
        </div>
        <div class="stat-divider"></div>
        <div class="stat-item">
          <span class="stat-value">{{ totalPoints }}</span>
          <span class="stat-label">积分</span>
        </div>
      </div>
    </div>

    <div class="achievement-grid">
      <div 
        v-for="achievement in achievements" 
        :key="achievement.id"
        :class="['achievement-card', { locked: !achievement.unlocked }]"
      >
        <div class="achievement-icon">
          {{ achievement.unlocked ? achievement.icon : '🔒' }}
        </div>
        <div class="achievement-info">
          <h4>{{ achievement.name }}</h4>
          <p>{{ achievement.description }}</p>
          <div v-if="achievement.unlocked" class="achievement-date">
            {{ achievement.unlocked_date }}
          </div>
          <div v-else class="achievement-progress">
            {{ achievement.progress }}/{{ achievement.target }}
          </div>
        </div>
        <div v-if="achievement.unlocked" class="achievement-badge">
          ✓
        </div>
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
      <div class="nav-item" @click="goToParentCenter">
        <span class="nav-icon">👨‍👩‍👧</span>
        <span class="nav-text">家长</span>
      </div>
      <div class="nav-item active" @click="goToSettings">
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

const achievements = ref([
  {
    id: 1,
    name: '初学者',
    description: '完成第一节课程',
    icon: '🌱',
    unlocked: true,
    unlocked_date: '2024-01-10',
    progress: 1,
    target: 1,
    points: 10
  },
  {
    id: 2,
    name: '学习达人',
    description: '连续学习7天',
    icon: '🔥',
    unlocked: true,
    unlocked_date: '2024-01-17',
    progress: 7,
    target: 7,
    points: 50
  },
  {
    id: 3,
    name: '学霸',
    description: '完成全部课程',
    icon: '👑',
    unlocked: false,
    unlocked_date: '',
    progress: 12,
    target: 40,
    points: 200
  },
  {
    id: 4,
    name: '全能王',
    description: '各科目都学一遍',
    icon: '⭐',
    unlocked: true,
    unlocked_date: '2024-01-15',
    progress: 4,
    target: 4,
    points: 100
  },
  {
    id: 5,
    name: '细心宝贝',
    description: '连续答对10道题',
    icon: '🎯',
    unlocked: false,
    unlocked_date: '',
    progress: 7,
    target: 10,
    points: 30
  },
  {
    id: 6,
    name: '阅读之星',
    description: '阅读10篇文章',
    icon: '📖',
    unlocked: false,
    unlocked_date: '',
    progress: 3,
    target: 10,
    points: 40
  },
  {
    id: 7,
    name: '数学天才',
    description: '数学练习正确率100%',
    icon: '🧮',
    unlocked: false,
    unlocked_date: '',
    progress: 0,
    target: 1,
    points: 80
  },
  {
    id: 8,
    name: '持之以恒',
    description: '累计学习100小时',
    icon: '⏰',
    unlocked: false,
    unlocked_date: '',
    progress: 35,
    target: 100,
    points: 150
  }
])

const unlockedCount = computed(() => achievements.value.filter(a => a.unlocked).length)
const totalCount = computed(() => achievements.value.length)
const totalPoints = computed(() => achievements.value.filter(a => a.unlocked).reduce((sum, a) => sum + a.points, 0))

function goToHome() { router.push('/') }
function goToCourses() { router.push('/courses') }
function goToParentCenter() { router.push('/parent-center') }
function goToSettings() { router.push('/settings') }
</script>

<style scoped>
.stats-card {
  background: linear-gradient(135deg, #4a90e2 0%, #667eea 100%);
  margin: 15px;
  padding: 20px;
  border-radius: 16px;
  color: #fff;
}

.stats-header {
  display: flex;
  align-items: center;
  margin-bottom: 15px;
}

.stats-icon {
  font-size: 28px;
  margin-right: 10px;
}

.stats-title {
  font-size: 16px;
  font-weight: 600;
}

.stats-content {
  display: flex;
  justify-content: space-around;
}

.stat-item {
  text-align: center;
}

.stat-value {
  font-size: 32px;
  font-weight: 700;
}

.stat-label {
  font-size: 12px;
  opacity: 0.9;
}

.stat-divider {
  width: 1px;
  background: rgba(255, 255, 255, 0.3);
}

.achievement-grid {
  padding: 0 15px 100px;
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.achievement-card {
  background: #fff;
  border-radius: 16px;
  padding: 15px;
  display: flex;
  gap: 15px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
}

.achievement-card.locked {
  opacity: 0.6;
}

.achievement-icon {
  width: 50px;
  height: 50px;
  background: linear-gradient(135deg, #4a90e2 0%, #667eea 100%);
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 26px;
  flex-shrink: 0;
}

.achievement-card.locked .achievement-icon {
  background: #e9ecef;
}

.achievement-info {
  flex: 1;
}

.achievement-info h4 {
  font-size: 15px;
  font-weight: 600;
  color: #2c3e50;
  margin-bottom: 4px;
}

.achievement-info p {
  font-size: 12px;
  color: #6c757d;
  margin-bottom: 6px;
}

.achievement-date {
  font-size: 11px;
  color: #4a90e2;
}

.achievement-progress {
  font-size: 11px;
  color: #f39c12;
}

.achievement-badge {
  width: 28px;
  height: 28px;
  background: #27ae60;
  color: #fff;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 14px;
  font-weight: 600;
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
