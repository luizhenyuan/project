from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import or_

from app.models import Course, Lesson, StudyProgress, Base
from app.schemas import CourseResponse, LessonResponse, ProgressUpdate
from app.routes.auth import get_current_user, User

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://preschool:password123@localhost:3306/preschool_app"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

subjects = ["语文", "数学", "英语", "艺术", "科学"]

courses_data = [
    {"id": 1, "title": "拼音启蒙", "description": "学习汉语拼音，打好语文基础", "subject": "语文", "lesson_count": 12, "cover_image": "https://example.com/pinyin.jpg"},
    {"id": 2, "title": "汉字认知", "description": "认识常用汉字，培养识字能力", "subject": "语文", "lesson_count": 15, "cover_image": "https://example.com/hanzi.jpg"},
    {"id": 3, "title": "数字乐园", "description": "认识数字0-100，建立数感", "subject": "数学", "lesson_count": 10, "cover_image": "https://example.com/math1.jpg"},
    {"id": 4, "title": "加减法入门", "description": "学习100以内加减法", "subject": "数学", "lesson_count": 18, "cover_image": "https://example.com/math2.jpg"},
    {"id": 5, "title": "英语字母", "description": "学习26个英文字母及发音", "subject": "英语", "lesson_count": 14, "cover_image": "https://example.com/english1.jpg"},
    {"id": 6, "title": "英语单词", "description": "学习日常英语单词", "subject": "英语", "lesson_count": 20, "cover_image": "https://example.com/english2.jpg"},
    {"id": 7, "title": "绘画基础", "description": "培养绘画兴趣和创造力", "subject": "艺术", "lesson_count": 8, "cover_image": "https://example.com/art.jpg"},
    {"id": 8, "title": "科学小实验", "description": "有趣的科学实验探索", "subject": "科学", "lesson_count": 12, "cover_image": "https://example.com/science.jpg"},
]

lessons_data = [
    {"id": 1, "course_id": 1, "title": "认识单韵母a", "description": "学习单韵母a的发音和写法", "video_url": "https://example.com/video1.mp4", "duration": 180, "order": 1},
    {"id": 2, "course_id": 1, "title": "认识单韵母o", "description": "学习单韵母o的发音和写法", "video_url": "https://example.com/video2.mp4", "duration": 180, "order": 2},
    {"id": 3, "course_id": 1, "title": "认识单韵母e", "description": "学习单韵母e的发音和写法", "video_url": "https://example.com/video3.mp4", "duration": 180, "order": 3},
    {"id": 4, "course_id": 2, "title": "认识汉字'人'", "description": "学习汉字'人'的写法和含义", "video_url": "https://example.com/video4.mp4", "duration": 240, "order": 1},
    {"id": 5, "course_id": 2, "title": "认识汉字'口'", "description": "学习汉字'口'的写法和含义", "video_url": "https://example.com/video5.mp4", "duration": 240, "order": 2},
    {"id": 6, "course_id": 3, "title": "数字1-10", "description": "认识数字1到10", "video_url": "https://example.com/video6.mp4", "duration": 200, "order": 1},
    {"id": 7, "course_id": 3, "title": "数字11-20", "description": "认识数字11到20", "video_url": "https://example.com/video7.mp4", "duration": 200, "order": 2},
    {"id": 8, "course_id": 4, "title": "5以内加法", "description": "学习5以内的加法", "video_url": "https://example.com/video8.mp4", "duration": 220, "order": 1},
    {"id": 9, "course_id": 4, "title": "5以内减法", "description": "学习5以内的减法", "video_url": "https://example.com/video9.mp4", "duration": 220, "order": 2},
    {"id": 10, "course_id": 5, "title": "字母A-H", "description": "学习字母A到H", "video_url": "https://example.com/video10.mp4", "duration": 260, "order": 1},
    {"id": 11, "course_id": 5, "title": "字母I-P", "description": "学习字母I到P", "video_url": "https://example.com/video11.mp4", "duration": 260, "order": 2},
    {"id": 12, "course_id": 6, "title": "动物单词", "description": "学习动物相关单词", "video_url": "https://example.com/video12.mp4", "duration": 240, "order": 1},
]

def init_courses(db):
    if not db.query(Course).first():
        for course in courses_data:
            db.add(Course(**course))
        db.commit()
    
    if not db.query(Lesson).first():
        for lesson in lessons_data:
            db.add(Lesson(**lesson))
        db.commit()

@router.get("/", response_model=list[CourseResponse])
def get_courses(subject: str = None, db = Depends(get_db)):
    init_courses(db)
    query = db.query(Course)
    if subject and subject != "全部":
        query = query.filter(Course.subject == subject)
    return query.all()

@router.get("/subjects")
def get_subjects():
    return subjects

@router.get("/{course_id}", response_model=CourseResponse)
def get_course(course_id: int, db = Depends(get_db)):
    init_courses(db)
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return course

@router.get("/{course_id}/lessons", response_model=list[LessonResponse])
def get_lessons(course_id: int, db = Depends(get_db)):
    init_courses(db)
    lessons = db.query(Lesson).filter(Lesson.course_id == course_id).order_by(Lesson.order).all()
    return lessons

@router.get("/{course_id}/lessons/{lesson_id}", response_model=LessonResponse)
def get_lesson(course_id: int, lesson_id: int, db = Depends(get_db)):
    init_courses(db)
    lesson = db.query(Lesson).filter(Lesson.id == lesson_id, Lesson.course_id == course_id).first()
    if not lesson:
        raise HTTPException(status_code=404, detail="Lesson not found")
    return lesson

@router.put("/{course_id}/lessons/{lesson_id}/progress")
def update_progress(course_id: int, lesson_id: int, progress: ProgressUpdate, 
                    current_user: User = Depends(get_current_user), db = Depends(get_db)):
    init_courses(db)
    existing = db.query(StudyProgress).filter(
        StudyProgress.user_id == current_user.id,
        StudyProgress.lesson_id == lesson_id
    ).first()
    
    if existing:
        existing.progress = progress.progress
        existing.completed = progress.progress >= 100
    else:
        new_progress = StudyProgress(
            user_id=current_user.id,
            lesson_id=lesson_id,
            progress=progress.progress,
            completed=progress.progress >= 100
        )
        db.add(new_progress)
    
    db.commit()
    return {"message": "Progress updated successfully"}

@router.get("/{course_id}/progress")
def get_course_progress(course_id: int, current_user: User = Depends(get_current_user), db = Depends(get_db)):
    init_courses(db)
    lessons = db.query(Lesson).filter(Lesson.course_id == course_id).all()
    progress_list = []
    
    for lesson in lessons:
        progress = db.query(StudyProgress).filter(
            StudyProgress.user_id == current_user.id,
            StudyProgress.lesson_id == lesson.id
        ).first()
        progress_list.append({
            "lesson_id": lesson.id,
            "lesson_title": lesson.title,
            "progress": progress.progress if progress else 0,
            "completed": progress.completed if progress else False
        })
    
    return {"course_id": course_id, "progress": progress_list}
