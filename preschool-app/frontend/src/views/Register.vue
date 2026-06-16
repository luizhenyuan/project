<template>
  <div class="page-container">
    <div class="register-header">
      <div class="back-btn" @click="goBack">←</div>
      <h1>注册账号</h1>
    </div>

    <div class="register-form">
      <div class="form-group">
        <label for="phone">手机号</label>
        <input 
          type="text" 
          id="phone" 
          v-model="phone" 
          placeholder="请输入手机号"
          maxlength="11"
        />
      </div>

      <div class="form-group">
        <label for="username">昵称</label>
        <input 
          type="text" 
          id="username" 
          v-model="username" 
          placeholder="请输入昵称"
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

      <div class="form-group">
        <label for="confirmPassword">确认密码</label>
        <input 
          type="password" 
          id="confirmPassword" 
          v-model="confirmPassword" 
          placeholder="请再次输入密码"
        />
      </div>

      <button class="btn-register" @click="handleRegister">
        {{ loading ? '注册中...' : '注 册' }}
      </button>
    </div>

    <div class="register-tips">
      <p>注册即表示同意</p>
      <p><span>用户协议</span> 和 <span>隐私政策</span></p>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useUserStore } from '@/stores/user'

const router = useRouter()
const userStore = useUserStore()

const phone = ref('')
const username = ref('')
const password = ref('')
const confirmPassword = ref('')
const showPassword = ref(false)
const loading = ref(false)

async function handleRegister() {
  if (!phone.value || !username.value || !password.value || !confirmPassword.value) {
    alert('请填写完整信息')
    return
  }

  if (!/^1[3-9]\d{9}$/.test(phone.value)) {
    alert('请输入正确的手机号')
    return
  }

  if (password.value.length < 6) {
    alert('密码长度不能少于6位')
    return
  }

  if (password.value !== confirmPassword.value) {
    alert('两次输入的密码不一致')
    return
  }

  loading.value = true
  const success = await userStore.registerAction(username.value, password.value, phone.value)
  loading.value = false

  if (success) {
    alert('注册成功，请登录')
    router.push('/login')
  } else {
    alert('注册失败，请重试')
  }
}

function goBack() {
  router.back()
}
</script>

<style scoped>
.page-container {
  min-height: 100vh;
  background: #f5f7fa;
}

.register-header {
  background: linear-gradient(135deg, #4a90e2 0%, #667eea 100%);
  padding: 20px;
  display: flex;
  align-items: center;
  color: #fff;
}

.back-btn {
  font-size: 24px;
  margin-right: 15px;
  cursor: pointer;
}

.register-header h1 {
  font-size: 18px;
  font-weight: 600;
}

.register-form {
  background: #fff;
  margin: 20px;
  padding: 25px;
  border-radius: 16px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
}

.form-group {
  margin-bottom: 18px;
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
  height: 45px;
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

.btn-register {
  width: 100%;
  height: 50px;
  background: linear-gradient(135deg, #4a90e2 0%, #667eea 100%);
  color: #fff;
  border: none;
  border-radius: 10px;
  font-size: 16px;
  font-weight: 600;
  cursor: pointer;
  margin-top: 10px;
}

.register-tips {
  text-align: center;
  padding: 20px;
  color: #6c757d;
  font-size: 12px;
}

.register-tips span {
  color: #4a90e2;
}
</style>
