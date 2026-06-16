from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)
    phone = Column(String(20), unique=True, index=True)
    hashed_password = Column(String(255))
    nickname = Column(String(50))
    avatar = Column(String(255))
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    study_progress = relationship("StudyProgress", back_populates="user")
    wrong_questions = relationship("WrongQuestion", back_populates="user")
    achievements = relationship("UserAchievement", back_populates="user")

class Course(Base):
    __tablename__ = "courses"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    description = Column(Text)
    subject = Column(String(20), nullable=False)
    lesson_count = Column(Integer, default=0)
    cover_image = Column(String(255))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    lessons = relationship("Lesson", back_populates="course")

class Lesson(Base):
    __tablename__ = "lessons"
    
    id = Column(Integer, primary_key=True, index=True)
    course_id = Column(Integer, ForeignKey("courses.id"))
    title = Column(String(100), nullable=False)
    description = Column(Text)
    video_url = Column(String(255))
    audio_url = Column(String(255))
    content = Column(Text)
    duration = Column(Integer)
    order = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    course = relationship("Course", back_populates="lessons")

class StudyProgress(Base):
    __tablename__ = "study_progress"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    lesson_id = Column(Integer, ForeignKey("lessons.id"))
    progress = Column(Float, default=0.0)
    completed = Column(Boolean, default=False)
    last_studied_at = Column(DateTime)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    user = relationship("User", back_populates="study_progress")

class Question(Base):
    __tablename__ = "questions"
    
    id = Column(Integer, primary_key=True, index=True)
    course_id = Column(Integer, ForeignKey("courses.id"))
    question = Column(Text, nullable=False)
    options = Column(Text)
    answer = Column(Integer, nullable=False)
    explanation = Column(Text)
    difficulty = Column(Integer, default=1)
    created_at = Column(DateTime, default=datetime.utcnow)

class WrongQuestion(Base):
    __tablename__ = "wrong_questions"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    question_id = Column(Integer, ForeignKey("questions.id"))
    wrong_count = Column(Integer, default=1)
    last_wrong_at = Column(DateTime)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    user = relationship("User", back_populates="wrong_questions")

class Achievement(Base):
    __tablename__ = "achievements"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    description = Column(String(200))
    icon = Column(String(50))
    points = Column(Integer, default=10)
    target_type = Column(String(20))
    target_value = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)

class UserAchievement(Base):
    __tablename__ = "user_achievements"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    achievement_id = Column(Integer, ForeignKey("achievements.id"))
    unlocked = Column(Boolean, default=False)
    unlocked_at = Column(DateTime)
    progress = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    user = relationship("User", back_populates="achievements")

class StudyReport(Base):
    __tablename__ = "study_reports"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    date = Column(DateTime, nullable=False)
    study_time = Column(Integer, default=0)
    completed_lessons = Column(Integer, default=0)
    correct_count = Column(Integer, default=0)
    wrong_count = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)
