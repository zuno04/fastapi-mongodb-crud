from fastapi import FastAPI
from routes.student import student_router

# Create App
app = FastAPI()

# Register the routers
app.include_router(student_router)