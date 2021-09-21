from fastapi import FastAPI
from routes.student import student_router
from fastapi.middleware.cors import CORSMiddleware

client_apps = ["http://localhost:3000"] # React Frontend App

# Create App
app = FastAPI()

# Register the routers
app.include_router(student_router)

# Register App with CORS middleware to allow resource sharing betwen different domains
app.add_middleware(
    CORSMiddleware,
    allow_origins=client_apps,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)