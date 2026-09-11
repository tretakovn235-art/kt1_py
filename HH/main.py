from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os
from routers.students import router as students_router
from routers.teachers import router as teachers_router

load_dotenv()

FRONTEND_URL = os.getenv("FRONTEND_URL", "http://localhost:8080")

app = FastAPI(title="Student API")
app.include_router(students_router)
app.include_router(teachers_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[FRONTEND_URL],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Welcome to API"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", reload=True)