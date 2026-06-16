<template>
  <div class="page-container">
    <div class="practice-header">
      <div class="back-btn" @click="goBack">←</div>
      <h1>课后练习</h1>
    </div>

    <div class="progress-section">
      <div class="progress-info">
        <span>第 {{ currentIndex + 1 }}/{{ questions.length }} 题</span>
        <span>{{ score }} 分</span>
      </div>
      <div class="progress-bar">
        <div class="progress-fill" :style="{ width: ((currentIndex + 1) / questions.length * 100) + '%' }"></div>
      </div>
    </div>

    <div v-if="!showResult" class="question-section">
      <div class="question-card">
        <div class="question-number">{{ currentIndex + 1 }}</div>
        <div class="question-content">
          <h3>{{ currentQuestion.question }}</h3>
          <div v-if="currentQuestion.image" class="question-image">
            <img :src="currentQuestion.image" alt="题目图片" />
          </div>
        </div>
      </div>

      <div class="options-list">
        <div 
          v-for="(option, index) in currentQuestion.options" 
          :key="index"
          :class="['option-item', { selected: selectedAnswer === index, correct: showAnswer && index === currentQuestion.answer, wrong: showAnswer && selectedAnswer === index && index !== currentQuestion.answer }]"
          @click="selectAnswer(index)"
        >
          <span class="option-letter">{{ ['A', 'B', 'C', 'D'][index] }}</span>
          <span class="option-text">{{ option }}</span>
          <span v-if="showAnswer && index === currentQuestion.answer" class="option-icon">✓</span>
          <span v-if="showAnswer && selectedAnswer === index && index !== currentQuestion.answer" class="option-icon wrong-icon">✗</span>
        </div>
      </div>

      <button 
        v-if="showAnswer" 
        class="btn-next" 
        @click="nextQuestion"
      >
        {{ currentIndex < questions.length - 1 ? '下一题' : '查看结果' }}
      </button>
    </div>

    <div v-else class="result-section">
      <div class="result-card">
        <div class="result-icon">{{ getResultIcon() }}</div>
        <h2>练习完成！</h2>
        <div class="result-score">
          <span class="score-value">{{ score }}</span>
          <span class="score-label">分</span>
        </div>
        <div class="result-stats">
          <div class="stat-item">
            <span class="stat-value correct">{{ correctCount }}</span>
            <span class="stat-label">答对</span>
          </div>
          <div class="stat-item">
            <span class="stat-value wrong">{{ questions.length - correctCount }}</span>
            <span class="stat-label">答错</span>
          </div>
          <div class="stat-item">
            <span class="stat-value">{{ Math.round(correctCount / questions.length * 100) }}%</span>
            <span class="stat-label">正确率</span>
          </div>
        </div>
      </div>

      <div class="action-buttons">
        <button class="btn-secondary" @click="goBack">返回课程</button>
        <button class="btn-primary" @click="restart">再练一次</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

const questions = ref([
  {
    id: 1,
    question: '下列哪个是声母 "b" 的正确发音？',
    options: ['波', '摸', '佛', '坡'],
    answer: 0
  },
  {
    id: 2,
    question: '下列哪个是声母 "p" 的正确发音？',
    options: ['波', '摸', '佛', '坡'],
    answer: 3
  },
  {
    id: 3,
    question: 'b 的正确书写顺序是？',
    options: ['先写圆再写竖', '先写竖再写右下半圆', '先写横再写竖', '先写撇再写捺'],
    answer: 1
  },
  {
    id: 4,
    question: 'm 由几笔组成？',
    options: ['1笔', '2笔', '3笔', '4笔'],
    answer: 2
  },
  {
    id: 5,
    question: '下列哪个字的声母是 "f"？',
    options: ['巴', '妈', '发', '趴'],
    answer: 2
  }
])

const currentIndex = ref(0)
const selectedAnswer = ref(null)
const showAnswer = ref(false)
const showResult = ref(false)
const score = ref(0)
const correctCount = ref(0)

const currentQuestion = computed(() => questions.value[currentIndex.value])

function selectAnswer(index) {
  if (showAnswer.value) return
  selectedAnswer.value = index
  showAnswer.value = true
  if (index === currentQuestion.value.answer) {
    score.value += 20
    correctCount.value++
  }
}

function nextQuestion() {
  if (currentIndex.value < questions.value.length - 1) {
    currentIndex.value++
    selectedAnswer.value = null
    showAnswer.value = false
  } else {
    showResult.value = true
  }
}

function getResultIcon() {
  const rate = correctCount.value / questions.value.length
  if (rate >= 0.9) return '🏆'
  if (rate >= 0.7) return '🎉'
  if (rate >= 0.5) return '💪'
  return '📚'
}

function restart() {
  currentIndex.value = 0
  selectedAnswer.value = null
  showAnswer.value = false
  showResult.value = false
  score.value = 0
  correctCount.value = 0
}

function goBack() {
  router.back()
}
</script>

<style scoped>
.practice-header {
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

.practice-header h1 {
  font-size: 18px;
  font-weight: 600;
}

.progress-section {
  background: #fff;
  padding: 15px 20px;
}

.progress-info {
  display: flex;
  justify-content: space-between;
  margin-bottom: 10px;
  font-size: 14px;
  color: #6c757d;
}

.progress-info span:last-child {
  color: #4a90e2;
  font-weight: 600;
}

.progress-bar {
  height: 6px;
  background: #f0f2f5;
  border-radius: 3px;
  overflow: hidden;
}

.progress-fill {
  height: 100%;
  background: linear-gradient(90deg, #4a90e2 0%, #667eea 100%);
  transition: width 0.3s;
}

.question-section {
  padding: 20px;
}

.question-card {
  background: #fff;
  border-radius: 16px;
  padding: 20px;
  margin-bottom: 20px;
  display: flex;
  gap: 15px;
}

.question-number {
  width: 36px;
  height: 36px;
  background: #4a90e2;
  color: #fff;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 14px;
  font-weight: 600;
  flex-shrink: 0;
}

.question-content h3 {
  font-size: 16px;
  font-weight: 600;
  color: #2c3e50;
  line-height: 1.6;
}

.options-list {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.option-item {
  display: flex;
  align-items: center;
  padding: 15px;
  background: #fff;
  border-radius: 12px;
  border: 2px solid #e9ecef;
  cursor: pointer;
  transition: all 0.3s;
}

.option-item:hover {
  border-color: #4a90e2;
}

.option-item.selected {
  border-color: #4a90e2;
  background: #e8f0fe;
}

.option-item.correct {
  border-color: #27ae60;
  background: #e8f8ed;
}

.option-item.wrong {
  border-color: #e74c3c;
  background: #fdecea;
}

.option-letter {
  width: 28px;
  height: 28px;
  background: #f5f7fa;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 14px;
  font-weight: 600;
  color: #6c757d;
  margin-right: 12px;
}

.option-item.selected .option-letter {
  background: #4a90e2;
  color: #fff;
}

.option-item.correct .option-letter {
  background: #27ae60;
  color: #fff;
}

.option-item.wrong .option-letter {
  background: #e74c3c;
  color: #fff;
}

.option-text {
  flex: 1;
  font-size: 15px;
  color: #2c3e50;
}

.option-icon {
  font-size: 18px;
  color: #27ae60;
}

.wrong-icon {
  color: #e74c3c;
}

.btn-next {
  width: 100%;
  height: 50px;
  background: linear-gradient(135deg, #4a90e2 0%, #667eea 100%);
  color: #fff;
  border: none;
  border-radius: 12px;
  font-size: 16px;
  font-weight: 600;
  cursor: pointer;
  margin-top: 20px;
}

.result-section {
  padding: 20px;
}

.result-card {
  background: #fff;
  border-radius: 20px;
  padding: 30px;
  text-align: center;
  margin-bottom: 20px;
}

.result-icon {
  font-size: 60px;
  margin-bottom: 15px;
}

.result-card h2 {
  font-size: 22px;
  font-weight: 600;
  color: #2c3e50;
  margin-bottom: 20px;
}

.result-score {
  margin-bottom: 25px;
}

.score-value {
  font-size: 56px;
  font-weight: 700;
  color: #4a90e2;
}

.score-label {
  font-size: 20px;
  color: #6c757d;
  margin-left: 5px;
}

.result-stats {
  display: flex;
  justify-content: space-around;
}

.stat-item {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.stat-value {
  font-size: 24px;
  font-weight: 700;
  color: #2c3e50;
}

.stat-value.correct {
  color: #27ae60;
}

.stat-value.wrong {
  color: #e74c3c;
}

.stat-label {
  font-size: 12px;
  color: #6c757d;
  margin-top: 5px;
}

.action-buttons {
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
