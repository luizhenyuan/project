from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime, timedelta
import json

from app.models import Question, WrongQuestion, Achievement, UserAchievement, StudyReport, Base
from app.schemas import QuestionResponse, AnswerSubmit, AnswerResponse, WrongQuestionResponse, AchievementResponse, WeeklyReportResponse
from app.routes.auth import get_current_user, User

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

questions_data = [
    {"id": 1, "course_id": 1, "question": "哪个字母是单韵母a？", "options": json.dumps(["a", "b", "c", "d"]), "answer": 0, "explanation": "a是单韵母，发音时嘴巴张大", "difficulty": 1},
    {"id": 2, "course_id": 1, "question": "哪个字母是单韵母o？", "options": json.dumps(["a", "o", "e", "i"]), "answer": 1, "explanation": "o是单韵母，发音时嘴唇拢圆", "difficulty": 1},
    {"id": 3, "course_id": 2, "question": "'人'字有几画？", "options": json.dumps(["1画", "2画", "3画", "4画"]), "answer": 1, "explanation": "'人'字由撇和捺两笔组成", "difficulty": 1},
    {"id": 4, "course_id": 2, "question": "'口'字是什么结构？", "options": json.dumps(["上下结构", "左右结构", "全包围结构", "半包围结构"]), "answer": 2, "explanation": "'口'字是全包围结构", "difficulty": 2},
    {"id": 5, "course_id": 3, "question": "数字5后面是几？", "options": json.dumps(["4", "5", "6", "7"]), "answer": 2, "explanation": "数字按顺序是1、2、3、4、5、6...", "difficulty": 1},
    {"id": 6, "course_id": 3, "question": "10以内最大的数字是？", "options": json.dumps(["9", "10", "8", "11"]), "answer": 0, "explanation": "10以内的数字是0-9，最大的是9", "difficulty": 1},
    {"id": 7, "course_id": 4, "question": "2 + 3 = ？", "options": json.dumps(["4", "5", "6", "7"]), "answer": 1, "explanation": "2加3等于5", "difficulty": 1},
    {"id": 8, "course_id": 4, "question": "5 - 2 = ？", "options": json.dumps(["2", "3", "4", "5"]), "answer": 1, "explanation": "5减2等于3", "difficulty": 1},
    {"id": 9, "course_id": 5, "question": "字母A的小写是？", "options": json.dumps(["A", "a", "B", "b"]), "answer": 1, "explanation": "A的小写是a", "difficulty": 1},
    {"id": 10, "course_id": 5, "question": "字母表中第3个字母是？", "options": json.dumps(["A", "B", "C", "D"]), "answer": 2, "explanation": "字母表顺序是A、B、C、D...", "difficulty": 1},
]

achievements_data = [
    {"id": 1, "name": "初学者", "description": "完成第一次学习", "icon": "star", "points": 10, "target_type": "study_count", "target_value": 1},
    {"id": 2, "name": "坚持者", "description": "连续学习7天", "icon": "fire", "points": 50, "target_type": "continuous_days", "target_value": 7},
    {"id": 3, "name": "学霸", "description": "完成100道练习题", "icon": "trophy", "points": 100, "target_type": "practice_count", "target_value": 100},
    {"id": 4, "name": "完美主义者", "description": "连续答对10道题", "icon": "crown", "points": 80, "target_type": "consecutive_correct", "target_value": 10},
]

def init_questions(db):
    if not db.query(Question).first():
        for question in questions_data:
            db.add(Question(**question))
        db.commit()
    
    if not db.query(Achievement).first():
        for achievement in achievements_data:
            db.add(Achievement(**achievement))
        db.commit()

@router.get("/questions", response_model=list[QuestionResponse])
def get_questions(course_id: int = None, limit: int = 10, db = Depends(get_db)):
    init_questions(db)
    query = db.query(Question)
    if course_id:
        query = query.filter(Question.course_id == course_id)
    questions = query.limit(limit).all()
    result = []
    for q in questions:
        result.append(QuestionResponse(
            id=q.id,
            course_id=q.course_id,
            question=q.question,
            options=json.loads(q.options),
            answer=q.answer,
            explanation=q.explanation,
            difficulty=q.difficulty
        ))
    return result

@router.get("/questions/{question_id}", response_model=QuestionResponse)
def get_question(question_id: int, db = Depends(get_db)):
    init_questions(db)
    question = db.query(Question).filter(Question.id == question_id).first()
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")
    return QuestionResponse(
        id=question.id,
        course_id=question.course_id,
        question=question.question,
        options=json.loads(question.options),
        answer=question.answer,
        explanation=question.explanation,
        difficulty=question.difficulty
    )

@router.post("/questions/{question_id}/answer", response_model=AnswerResponse)
def submit_answer(question_id: int, answer: AnswerSubmit, 
                  current_user: User = Depends(get_current_user), db = Depends(get_db)):
    init_questions(db)
    question = db.query(Question).filter(Question.id == question_id).first()
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")
    
    correct = answer.answer == question.answer
    
    if not correct:
        existing = db.query(WrongQuestion).filter(
            WrongQuestion.user_id == current_user.id,
            WrongQuestion.question_id == question_id
        ).first()
        if existing:
            existing.wrong_count += 1
            existing.last_wrong_at = datetime.utcnow()
        else:
            new_wrong = WrongQuestion(
                user_id=current_user.id,
                question_id=question_id,
                last_wrong_at=datetime.utcnow()
            )
            db.add(new_wrong)
    
    update_study_report(current_user.id, correct, db)
    check_achievements(current_user.id, db)
    
    db.commit()
    
    return AnswerResponse(
        correct=correct,
        correct_answer=question.answer,
        explanation=question.explanation
    )

def update_study_report(user_id: int, correct: bool, db):
    today = datetime.utcnow().date()
    report = db.query(StudyReport).filter(
        StudyReport.user_id == user_id,
        StudyReport.date >= datetime(today.year, today.month, today.day),
        StudyReport.date < datetime(today.year, today.month, today.day) + timedelta(days=1)
    ).first()
    
    if report:
        if correct:
            report.correct_count += 1
        else:
            report.wrong_count += 1
    else:
        new_report = StudyReport(
            user_id=user_id,
            date=datetime.utcnow(),
            correct_count=1 if correct else 0,
            wrong_count=1 if not correct else 0
        )
        db.add(new_report)

def check_achievements(user_id: int, db):
    achievements = db.query(Achievement).all()
    for achievement in achievements:
        ua = db.query(UserAchievement).filter(
            UserAchievement.user_id == user_id,
            UserAchievement.achievement_id == achievement.id
        ).first()
        
        if not ua:
            ua = UserAchievement(
                user_id=user_id,
                achievement_id=achievement.id,
                progress=0
            )
            db.add(ua)
        
        if achievement.target_type == "practice_count":
            reports = db.query(StudyReport).filter(StudyReport.user_id == user_id).all()
            total = sum(r.correct_count + r.wrong_count for r in reports)
            ua.progress = total
            if total >= achievement.target_value and not ua.unlocked:
                ua.unlocked = True
                ua.unlocked_at = datetime.utcnow()
        
        elif achievement.target_type == "consecutive_correct":
            pass

@router.get("/wrong-questions", response_model=list[WrongQuestionResponse])
def get_wrong_questions(current_user: User = Depends(get_current_user), db = Depends(get_db)):
    wrongs = db.query(WrongQuestion).filter(WrongQuestion.user_id == current_user.id).all()
    result = []
    for w in wrongs:
        question = db.query(Question).filter(Question.id == w.question_id).first()
        course = db.query(Question).filter(Question.id == w.question_id).first()
        result.append(WrongQuestionResponse(
            id=w.id,
            question_id=w.question_id,
            question=question.question if question else "",
            subject="",
            wrong_count=w.wrong_count,
            last_wrong_at=w.last_wrong_at
        ))
    return result

@router.delete("/wrong-questions/{wrong_id}")
def remove_wrong_question(wrong_id: int, current_user: User = Depends(get_current_user), db = Depends(get_db)):
    wrong = db.query(WrongQuestion).filter(
        WrongQuestion.id == wrong_id,
        WrongQuestion.user_id == current_user.id
    ).first()
    if not wrong:
        raise HTTPException(status_code=404, detail="Wrong question not found")
    db.delete(wrong)
    db.commit()
    return {"message": "Wrong question removed successfully"}

@router.get("/achievements", response_model=list[AchievementResponse])
def get_achievements(current_user: User = Depends(get_current_user), db = Depends(get_db)):
    init_questions(db)
    achievements = db.query(Achievement).all()
    result = []
    for achievement in achievements:
        ua = db.query(UserAchievement).filter(
            UserAchievement.user_id == current_user.id,
            UserAchievement.achievement_id == achievement.id
        ).first()
        result.append(AchievementResponse(
            id=achievement.id,
            name=achievement.name,
            description=achievement.description,
            icon=achievement.icon,
            points=achievement.points,
            unlocked=ua.unlocked if ua else False,
            unlocked_at=ua.unlocked_at if ua else None,
            progress=ua.progress if ua else 0,
            target=achievement.target_value
        ))
    return result

@router.get("/weekly-report", response_model=WeeklyReportResponse)
def get_weekly_report(current_user: User = Depends(get_current_user), db = Depends(get_db)):
    today = datetime.utcnow()
    seven_days_ago = today - timedelta(days=7)
    
    reports = db.query(StudyReport).filter(
        StudyReport.user_id == current_user.id,
        StudyReport.date >= seven_days_ago
    ).all()
    
    total_study_time = sum(r.study_time for r in reports)
    completed_lessons = sum(r.completed_lessons for r in reports)
    total_correct = sum(r.correct_count for r in reports)
    total_wrong = sum(r.wrong_count for r in reports)
    avg_accuracy = total_correct / (total_correct + total_wrong) * 100 if (total_correct + total_wrong) > 0 else 0
    
    daily_data = [StudyReportResponse.from_orm(r) for r in reports]
    
    return WeeklyReportResponse(
        total_study_time=total_study_time,
        completed_lessons=completed_lessons,
        avg_accuracy=avg_accuracy,
        daily_data=daily_data
    )
