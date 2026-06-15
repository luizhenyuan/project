<template>
  <div class="page-container">
    <div class="page-header">
      <h1>设置</h1>
      <p>个性化您的学习体验</p>
    </div>

    <div class="user-card">
      <div class="user-avatar">👤</div>
      <div class="user-info">
        <h3>{{ userInfo.nickname }}</h3>
        <p>{{ userInfo.phone }}</p>
      </div>
      <div class="user-arrow">→</div>
    </div>

    <div class="settings-section">
      <div class="section-title">账号与安全</div>
      <div class="settings-list">
        <div class="settings-item" @click="editProfile">
          <div class="item-icon">👤</div>
          <span class="item-text">编辑资料</span>
          <span class="item-arrow">→</span>
        </div>
        <div class="settings-item" @click="changePassword">
          <div class="item-icon">🔑</div>
          <span class="item-text">修改密码</span>
          <span class="item-arrow">→</span>
        </div>
        <div class="settings-item" @click="bindPhone">
          <div class="item-icon">📱</div>
          <span class="item-text">绑定手机</span>
          <span class="item-arrow">→</span>
        </div>
      </div>
    </div>

    <div class="settings-section">
      <div class="section-title">学习设置</div>
      <div class="settings-list">
        <div class="settings-item">
          <div class="item-icon">🔔</div>
          <span class="item-text">学习提醒</span>
          <div class="item-switch" :class="{ active: notificationsEnabled }" @click="toggleNotifications">
            <div class="switch-dot"></div>
          </div>
        </div>
        <div class="settings-item">
          <div class="item-icon">🔊</div>
          <span class="item-text">声音效果</span>
          <div class="item-switch" :class="{ active: soundEnabled }" @click="toggleSound">
            <div class="switch-dot"></div>
          </div>
        </div>
        <div class="settings-item">
          <div class="item-icon">🌙</div>
          <span class="item-text">夜间模式</span>
          <div class="item-switch" :class="{ active: darkMode }" @click="toggleDarkMode">
            <div class="switch-dot"></div>
          </div>
        </div>
        <div class="settings-item" @click="timeLimit">
          <div class="item-icon">⏱️</div>
          <span class="item-text">时长限制</span>
          <span class="item-arrow">→</span>
        </div>
      </div>
    </div>

    <div class="settings-section">
      <div class="section-title">其他</div>
      <div class="settings-list">
        <div class="settings-item" @click="about">
          <div class="item-icon">ℹ️</div>
          <span class="item-text">关于我们</span>
          <span class="item-arrow">→</span>
        </div>
        <div class="settings-item" @click="help">
          <div class="item-icon">❓</div>
          <span class="item-text">帮助与反馈</span>
          <span class="item-arrow">→</span>
        </div>
        <div class="settings-item" @click="privacy">
          <div class="item-icon">🔒</div>
          <span class="item-text">隐私政策</span>
          <span class="item-arrow">→</span>
        </div>
        <div class="settings-item" @click="terms">
          <div class="item-icon">📋</div>
          <span class="item-text">用户协议</span>
          <span class="item-arrow">→</span>
        </div>
      </div>
    </div>

    <button class="btn-logout" @click="logout">退出登录</button>

    <div class="version-info">
      <span>版本号：v1.0.0</span>
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
import { useUserStore } from '@/stores/user'

const router = useRouter()
const userStore = useUserStore()

const userInfo = ref({
  nickname: '小明妈妈',
  phone: '138****8888'
})

const notificationsEnabled = ref(true)
const soundEnabled = ref(true)
const darkMode = ref(false)

function toggleNotifications() {
  notificationsEnabled.value = !notificationsEnabled.value
}

function toggleSound() {
  soundEnabled.value = !soundEnabled.value
}

function toggleDarkMode() {
  darkMode.value = !darkMode.value
}

function editProfile() {
  alert('编辑资料功能开发中')
}

function changePassword() {
  alert('修改密码功能开发中')
}

function bindPhone() {
  alert('绑定手机功能开发中')
}

function timeLimit() {
  alert('时长限制功能开发中')
}

function about() {
  alert('关于我们：幼小衔接学习平台 v1.0.0')
}

function help() {
  alert('帮助与反馈功能开发中')
}

function privacy() {
  alert('隐私政策功能开发中')
}

function terms() {
  alert('用户协议功能开发中')
}

function logout() {
  if (confirm('确定要退出登录吗？')) {
    userStore.logout()
    router.push('/login')
  }
}

function goToHome() { router.push('/') }
function goToCourses() { router.push('/courses') }
function goToParentCenter() { router.push('/parent-center') }
function goToSettings() { router.push('/settings') }
</script>

<style scoped>
.user-card {
  background: linear-gradient(135deg, #4a90e2 0%, #667eea 100%);
  margin: 15px;
  padding: 20px;
  border-radius: 16px;
  display: flex;
  align-items: center;
  color: #fff;
}

.user-avatar {
  width: 60px;
  height: 60px;
  background: rgba(255, 255, 255, 0.2);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 30px;
  margin-right: 15px;
}

.user-info h3 {
  font-size: 18px;
  font-weight: 600;
  margin-bottom: 3px;
}

.user-info p {
  font-size: 14px;
  opacity: 0.9;
}

.user-arrow {
  margin-left: auto;
  font-size: 18px;
}

.settings-section {
  background: #fff;
  margin: 15px;
  border-radius: 16px;
  overflow: hidden;
}

.section-title {
  padding: 15px 20px;
  font-size: 12px;
  color: #95a5a6;
  background: #f8f9fa;
}

.settings-list {
  padding: 5px 0;
}

.settings-item {
  display: flex;
  align-items: center;
  padding: 15px 20px;
  border-bottom: 1px solid #f0f2f5;
  cursor: pointer;
}

.settings-item:last-child {
  border-bottom: none;
}

.item-icon {
  font-size: 22px;
  margin-right: 12px;
}

.item-text {
  flex: 1;
  font-size: 15px;
  color: #2c3e50;
}

.item-arrow {
  color: #95a5a6;
}

.item-switch {
  width: 44px;
  height: 24px;
  background: #e9ecef;
  border-radius: 12px;
  position: relative;
  transition: background 0.3s;
}

.item-switch.active {
  background: #4a90e2;
}

.switch-dot {
  position: absolute;
  left: 2px;
  top: 2px;
  width: 20px;
  height: 20px;
  background: #fff;
  border-radius: 50%;
  transition: left 0.3s;
}

.item-switch.active .switch-dot {
  left: 22px;
}

.btn-logout {
  width: calc(100% - 30px);
  margin: 15px;
  height: 48px;
  background: #fff;
  color: #e74c3c;
  border: 1px solid #e74c3c;
  border-radius: 12px;
  font-size: 16px;
  cursor: pointer;
}

.version-info {
  text-align: center;
  padding: 20px;
  font-size: 12px;
  color: #95a5a6;
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
