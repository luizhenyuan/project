<template>
  <div class="page-container">
    <div class="page-header">
      <h1>错题本</h1>
      <p>复习错题，巩固知识</p>
    </div>

    <div v-if="wrongQuestions.length === 0" class="empty-state">
      <div class="empty-icon">🎉</div>
      <h2>太棒了！</h2>
      <p>暂无错题，继续保持！</p>
    </div>

    <div v-else class="wrong-list">
      <div 
        v-for="(item, index) in wrongQuestions" 
        :key="item.id"
        class="wrong-item"
        @click="reviewQuestion(index)"
      >
        <div class="wrong-header">
          <span class="subject-tag">{{ getSubjectName(item.subject) }}</span>
          <span class="wrong-count">错{{ item.wrong_count }}次</span>
        </div>
        <div class="wrong-content">
          <p>{{ item.question }}</p>
        </div>
        <div class="wrong-footer">
          <span>{{ item.last_wrong_time }}</span>
          <span class="action-text">去练习 →</span>
        </div>
      </div>
    </div>

    <div v-if="wrongQuestions.length > 0" class="action-area">
      <button class="btn-primary" @click="practiceAll">练习全部错题</button>
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
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

const wrongQuestions = ref([
  {
    id: 1,
    question: '下列哪个是声母 "b" 的正确发音？',
    subject: 'chinese',
    wrong_count: 2,
    last_wrong_time: '2024-01-15 14:30'
  },
  {
    id: 2,
    question: 'b 的正确书写顺序是？',
    subject: 'chinese',
    wrong_count: 1,
    last_wrong_time: '2024-01-14 10:20'
  },
  {
    id: 3,
    question: '5 + 7 = ?',
    subject: 'math',
    wrong_count: 3,
    last_wrong_time: '2024-01-15 16:45'
  },
  {
    id: 4,
    question: '请找出不同类的物品：苹果、香蕉、橘子、铅笔',
    subject: 'thinking',
    wrong_count: 1,
    last_wrong_time: '2024-01-13 09:15'
  }
])

function getSubjectName(subject) {
  const names = {
    chinese: '语文',
    math: '数学',
    thinking: '思维',
    habit: '习惯'
  }
  return names[subject] || '其他'
}

function reviewQuestion(index) {
  alert(`复习第${index + 1}题`)
}

function practiceAll() {
  alert('开始练习所有错题')
}

function goToHome() { router.push('/') }
function goToCourses() { router.push('/courses') }
function goToParentCenter() { router.push('/parent-center') }
function goToSettings() { router.push('/settings') }
</script>

<style scoped>
.empty-state {
  text-align: center;
  padding: 60px 20px;
}

.empty-icon {
  font-size: 80px;
  margin-bottom: 20px;
}

.empty-state h2 {
  font-size: 22px;
  font-weight: 600;
  color: #2c3e50;
  margin-bottom: 10px;
}

.empty-state p {
  font-size: 14px;
  color: #6c757d;
}

.wrong-list {
  padding: 15px;
}

.wrong-item {
  background: #fff;
  border-radius: 16px;
  padding: 15px;
  margin-bottom: 12px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
}

.wrong-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 10px;
}

.subject-tag {
  padding: 4px 12px;
  background: #4a90e2;
  color: #fff;
  border-radius: 12px;
  font-size: 12px;
}

.wrong-count {
  font-size: 12px;
  color: #e74c3c;
  font-weight: 600;
}

.wrong-content p {
  font-size: 15px;
  color: #2c3e50;
  line-height: 1.6;
  margin-bottom: 10px;
}

.wrong-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 12px;
  color: #6c757d;
}

.action-text {
  color: #4a90e2;
}

.action-area {
  padding: 0 15px 100px;
}

.btn-primary {
  width: 100%;
  height: 50px;
  background: linear-gradient(135deg, #4a90e2 0%, #667eea 100%);
  color: #fff;
  border: none;
  border-radius: 12px;
  font-size: 16px;
  font-weight: 600;
  cursor: pointer;
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
