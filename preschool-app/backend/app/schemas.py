from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional, List

class UserCreate(BaseModel):
    username: str
    password: str
    phone: Optional[str] = None
    nickname: Optional[str] = None

class UserLogin(BaseModel):
    username: str
    password: str

class UserResponse(BaseModel):
    id: int
    username: str
    phone: Optional[str]
    nickname: Optional[str]
    avatar: Optional[str]
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True

class CourseResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    subject: str
    lesson_count: int
    cover_image: Optional[str]
    created_at: datetime

    class Config:
        from_attributes = True

class LessonResponse(BaseModel):
    id: int
    course_id: int
    title: str
    description: Optional[str]
    video_url: Optional[str]
    audio_url: Optional[str]
    content: Optional[str]
    duration: Optional[int]
    order: int

    class Config:
        from_attributes = True

class QuestionResponse(BaseModel):
    id: int
    course_id: int
    question: str
    options: List[str]
    answer: int
    explanation: Optional[str]
    difficulty: int

    class Config:
        from_attributes = True

class AnswerSubmit(BaseModel):
    answer: int

class AnswerResponse(BaseModel):
    correct: bool
    correct_answer: int
    explanation: Optional[str]

class WrongQuestionResponse(BaseModel):
    id: int
    question_id: int
    question: str
    subject: str
    wrong_count: int
    last_wrong_at: Optional[datetime]

    class Config:
        from_attributes = True

class AchievementResponse(BaseModel):
    id: int
    name: str
    description: Optional[str]
    icon: Optional[str]
    points: int
    unlocked: bool
    unlocked_at: Optional[datetime]
    progress: int
    target: int

    class Config:
        from_attributes = True

class StudyReportResponse(BaseModel):
    date: datetime
    study_time: int
    completed_lessons: int
    correct_count: int
    wrong_count: int

    class Config:
        from_attributes = True

class WeeklyReportResponse(BaseModel):
    total_study_time: int
    completed_lessons: int
    avg_accuracy: float
    daily_data: List[StudyReportResponse]

class ProgressUpdate(BaseModel):
    progress: float
