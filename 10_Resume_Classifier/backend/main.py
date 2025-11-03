from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins="http://localhost:5173",
    allow_credentials=True,
    allow_methods=["*"],    
    allow_headers=["*"],
)

@app.get("/")
def homeRoute(): 
    return "this is the home route of your application"

@app.get("/classify")
def classify_resume(): 
    #  Perform the main function here. 