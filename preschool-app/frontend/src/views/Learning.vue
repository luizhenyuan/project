<template>
  <div class="page-container">
    <div class="learning-header">
      <div class="back-btn" @click="goBack">←</div>
      <div class="header-info">
        <h1>{{ lesson.title }}</h1>
        <p>{{ courseTitle }} - 第{{ currentIndex + 1 }}/{{ totalLessons }}节</p>
      </div>
    </div>

    <div class="video-section">
      <div class="video-container">
        <div class="video-placeholder">
          <span class="play-icon">▶</span>
          <p>视频课程</p>
        </div>
        <div class="video-controls">
          <div class="progress-bar">
            <div class="progress-fill" :style="{ width: progress + '%' }"></div>
            <div class="progress-dot" :style="{ left: progress + '%' }"></div>
          </div>
          <div class="control-buttons">
            <span class="control-btn">⏪</span>
            <span class="control-btn play-btn" @click="togglePlay">{{ isPlaying ? '⏸' : '▶' }}</span>
            <span class="control-btn">⏩</span>
            <span class="time-display">{{ formatTime(currentTime) }}/{{ formatTime(duration) }}</span>
          </div>
        </div>
      </div>
    </div>

    <div class="content-section">
      <div class="section-tabs">
        <div 
          :class="['tab', { active: activeTab === 'content' }]"
          @click="activeTab = 'content'"
        >课程内容</div>
        <div 
          :class="['tab', { active: activeTab === 'notes' }]"
          @click="activeTab = 'notes'"
        >课堂笔记</div>
      </div>

      <div v-if="activeTab === 'content'" class="content-content">
        <div class="content-item" v-for="(item, index) in contentItems" :key="index">
          <div class="content-icon">{{ item.icon }}</div>
          <div class="content-text">
            <h4>{{ item.title }}</h4>
            <p>{{ item.text }}</p>
          </div>
        </div>
      </div>

      <div v-else class="notes-content">
        <textarea 
          v-model="notes" 
          placeholder="记录课堂笔记..."
          class="notes-textarea"
        ></textarea>
        <button class="save-notes-btn" @click="saveNotes">保存笔记</button>
      </div>
    </div>

    <div class="action-buttons">
      <button class="btn-secondary" @click="goToPractice">课后练习</button>
      <button class="btn-primary" @click="nextLesson">下一节 →</button>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'

const router = useRouter()
const route = useRoute()

const lesson = ref({
  id: 1,
  title: '认识声母 b p m f',
  duration: 600
})

const courseTitle = ref('拼音入门')
const currentIndex = ref(0)
const totalLessons = ref(10)

const progress = ref(35)
const currentTime = ref(210)
const duration = ref(600)
const isPlaying = ref(false)

const activeTab = ref('content')
const notes = ref('')

const contentItems = ref([
  { icon: '🔊', title: '发音要点', text: 'b：双唇紧闭，突然放开，气流较p弱' },
  { icon: '🔊', title: '发音要点', text: 'p：双唇紧闭，突然放开，气流较强' },
  { icon: '🔊', title: '发音要点', text: 'm：双唇紧闭，把气堵住，然后让气流从鼻腔出来' },
  { icon: '🔊', title: '发音要点', text: 'f：上齿接触下唇，形成窄缝，让气流从缝中摩擦而出' },
  { icon: '📝', title: '书写指导', text: 'b：先写竖，再写右下半圆' },
  { icon: '📝', title: '书写指导', text: 'p：先写竖，再写右上半圆' },
  { icon: '📝', title: '书写指导', text: 'm：先写竖，再写两个弯' },
  { icon: '📝', title: '书写指导', text: 'f：先写右弯竖，再写横' }
])

function formatTime(seconds) {
  const mins = Math.floor(seconds / 60)
  const secs = seconds % 60
  return `${mins}:${secs.toString().padStart(2, '0')}`
}

function togglePlay() {
  isPlaying.value = !isPlaying.value
}

function goBack() {
  router.back()
}

function goToPractice() {
  const courseId = route.params.courseId
  router.push(`/practice/${courseId}`)
}

function nextLesson() {
  const courseId = route.params.courseId
  const currentLessonId = parseInt(route.params.lessonId)
  router.push(`/learning/${courseId}/${currentLessonId + 1}`)
}

function saveNotes() {
  alert('笔记已保存')
}

onMounted(() => {
  const lessonId = parseInt(route.params.lessonId)
  if (lessonId) {
    lesson.value.id = lessonId
    currentIndex.value = lessonId - 1
  }
})
</script>

<style scoped>
.learning-header {
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

.header-info h1 {
  font-size: 16px;
  font-weight: 600;
  margin-bottom: 3px;
}

.header-info p {
  font-size: 12px;
  opacity: 0.9;
}

.video-section {
  background: #000;
}

.video-container {
  position: relative;
}

.video-placeholder {
  height: 200px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  color: #fff;
}

.play-icon {
  font-size: 48px;
  margin-bottom: 10px;
}

.video-placeholder p {
  font-size: 14px;
  opacity: 0.8;
}

.video-controls {
  padding: 15px;
  background: rgba(0, 0, 0, 0.8);
}

.progress-bar {
  position: relative;
  height: 6px;
  background: rgba(255, 255, 255, 0.3);
  border-radius: 3px;
  margin-bottom: 10px;
  cursor: pointer;
}

.progress-fill {
  height: 100%;
  background: #4a90e2;
  border-radius: 3px;
}

.progress-dot {
  position: absolute;
  top: 50%;
  transform: translate(-50%, -50%);
  width: 14px;
  height: 14px;
  background: #fff;
  border-radius: 50%;
}

.control-buttons {
  display: flex;
  align-items: center;
  gap: 15px;
}

.control-btn {
  font-size: 20px;
  cursor: pointer;
}

.play-btn {
  font-size: 28px;
}

.time-display {
  margin-left: auto;
  font-size: 13px;
  opacity: 0.8;
}

.content-section {
  background: #fff;
  margin: 15px;
  border-radius: 16px;
  overflow: hidden;
}

.section-tabs {
  display: flex;
  border-bottom: 1px solid #e9ecef;
}

.tab {
  flex: 1;
  padding: 15px;
  text-align: center;
  font-size: 15px;
  color: #6c757d;
  cursor: pointer;
}

.tab.active {
  color: #4a90e2;
  border-bottom: 2px solid #4a90e2;
}

.content-content {
  padding: 15px;
}

.content-item {
  display: flex;
  gap: 15px;
  padding: 15px 0;
  border-bottom: 1px solid #f0f2f5;
}

.content-item:last-child {
  border-bottom: none;
}

.content-icon {
  font-size: 24px;
  width: 40px;
  height: 40px;
  background: #f5f7fa;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.content-text h4 {
  font-size: 15px;
  font-weight: 600;
  color: #2c3e50;
  margin-bottom: 5px;
}

.content-text p {
  font-size: 13px;
  color: #6c757d;
  line-height: 1.6;
}

.notes-content {
  padding: 15px;
}

.notes-textarea {
  width: 100%;
  height: 150px;
  padding: 15px;
  border: 1px solid #e9ecef;
  border-radius: 12px;
  font-size: 14px;
  resize: none;
  margin-bottom: 15px;
}

.save-notes-btn {
  width: 100%;
  height: 45px;
  background: #4a90e2;
  color: #fff;
  border: none;
  border-radius: 10px;
  font-size: 15px;
  cursor: pointer;
}

.action-buttons {
  position: fixed;
  bottom: 20px;
  left: 15px;
  right: 15px;
  display: flex;
  gap: 15px;
}

.btn-secondary {
  flex: 1;
  height: 50px;
  background: #fff;
  color: #4a90e2;
  border: 1px solid #4a90e2;
  border-radius: 12px;
  font-size: 16px;
  font-weight: 500;
  cursor: pointer;
}

.btn-primary {
  flex: 1;
  height: 50px;
  background: linear-gradient(135deg, #4a90e2 0%, #667eea 100%);
  color: #fff;
  border: none;
  border-radius: 12px;
  font-size: 16px;
  font-weight: 500;
  cursor: pointer;
}
</style>
