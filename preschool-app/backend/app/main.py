from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import auth, course, practice

app = FastAPI(title="幼小衔接课程应用 API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/api/auth", tags=["auth"])
app.include_router(course.router, prefix="/api/courses", tags=["courses"])
app.include_router(practice.router, prefix="/api/practice", tags=["practice"])

@app.get("/api/health")
async def health_check():
    return {"status": "ok", "message": "幼小衔接课程应用 API 运行正常"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
