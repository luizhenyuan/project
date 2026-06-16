<template>
  <div class="page-container">
    <div class="login-header">
      <div class="logo">📚</div>
      <h1>幼小衔接</h1>
      <p>快乐学习，轻松成长</p>
    </div>

    <div class="login-form">
      <div class="form-group">
        <label for="username">手机号</label>
        <input 
          type="text" 
          id="username" 
          v-model="username" 
          placeholder="请输入手机号"
          maxlength="11"
        />
      </div>

      <div class="form-group">
        <label for="password">密码</label>
        <div class="password-input">
          <input 
            :type="showPassword ? 'text' : 'password'" 
            id="password" 
            v-model="password" 
            placeholder="请输入密码"
          />
          <span class="password-toggle" @click="showPassword = !showPassword">
            {{ showPassword ? '🙈' : '👁️' }}
          </span>
        </div>
      </div>

      <button class="btn-login" @click="handleLogin">
        {{ loading ? '登录中...' : '登 录' }}
      </button>

      <div class="form-links">
        <span @click="goToRegister">注册账号</span>
        <span @click="goToForgotPassword">忘记密码?</span>
      </div>
    </div>

    <div class="login-tips">
      <p>首次使用请先注册</p>
      <p>支持手机号快速登录</p>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useUserStore } from '@/stores/user'

const router = useRouter()
const userStore = useUserStore()

const username = ref('')
const password = ref('')
const showPassword = ref(false)
const loading = ref(false)

async function handleLogin() {
  if (!username.value || !password.value) {
    alert('请输入手机号和密码')
    return
  }

  loading.value = true
  const success = await userStore.loginAction(username.value, password.value)
  loading.value = false

  if (success) {
    router.push('/')
  } else {
    alert('登录失败，请检查账号密码')
  }
}

function goToRegister() {
  router.push('/register')
}

function goToForgotPassword() {
  alert('密码找回功能开发中')
}
</script>

<style scoped>
.page-container {
  min-height: 100vh;
  background: linear-gradient(180deg, #4a90e2 0%, #667eea 50%, #f5f7fa 50%);
  display: flex;
  flex-direction: column;
}

.login-header {
  text-align: center;
  padding: 60px 20px 40px;
  color: #fff;
}

.logo {
  font-size: 60px;
  margin-bottom: 15px;
}

.login-header h1 {
  font-size: 28px;
  font-weight: 700;
  margin-bottom: 5px;
}

.login-header p {
  font-size: 14px;
  opacity: 0.9;
}

.login-form {
  background: #fff;
  margin: 0 20px;
  padding: 30px 25px;
  border-radius: 20px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
}

.form-group {
  margin-bottom: 20px;
}

.form-group label {
  display: block;
  font-size: 14px;
  font-weight: 500;
  color: #2c3e50;
  margin-bottom: 8px;
}

.form-group input {
  width: 100%;
  height: 48px;
  padding: 0 15px;
  border: 1px solid #e9ecef;
  border-radius: 10px;
  font-size: 15px;
  background: #f8f9fa;
  transition: border-color 0.3s;
}

.form-group input:focus {
  outline: none;
  border-color: #4a90e2;
}

.password-input {
  position: relative;
}

.password-toggle {
  position: absolute;
  right: 15px;
  top: 50%;
  transform: translateY(-50%);
  font-size: 18px;
  cursor: pointer;
}

.btn-login {
  width: 100%;
  height: 50px;
  background: linear-gradient(135deg, #4a90e2 0%, #667eea 100%);
  color: #fff;
  border: none;
  border-radius: 10px;
  font-size: 16px;
  font-weight: 600;
  cursor: pointer;
  margin-bottom: 20px;
}

.form-links {
  display: flex;
  justify-content: space-between;
  font-size: 14px;
}

.form-links span {
  color: #4a90e2;
  cursor: pointer;
}

.login-tips {
  text-align: center;
  padding: 30px 20px;
  color: #6c757d;
  font-size: 13px;
}

.login-tips p {
  margin-bottom: 5px;
}
</style>
