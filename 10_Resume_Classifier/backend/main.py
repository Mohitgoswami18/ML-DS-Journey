from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from PyPDF2 import PdfReader
import pickle 
import re
import string

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins="http://localhost:5173",
    allow_credentials=True,
    allow_methods=["*"],    
    allow_headers=["*"],
)

loader = pickle.load(open("model.pkl", "rb"))

@app.get("/")
def homeRoute(): 
    return "this is the home route of your application"

@app.post("/classify")
async def classify(file_path: str = Form(...)):
    # Just for testing: print or use the file path
    print("📁 Received file path:", file_path)
    return {"message": f"Received file path: {file_path}"}

    
