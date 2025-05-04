from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from .utils import analyze_log
from .rally import create_rally_ticket

app = FastAPI()

# Allow frontend to access backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/analyze/")
async def analyze(file: UploadFile = File(...)):
    content = await file.read()
    decoded = content.decode('utf-8', errors='ignore')
    lines = decoded.splitlines()
    issue_detected, details = analyze_log(lines)

    response = {
        "filename": file.filename,
        "lines": len(lines),
        "message": "No issues found."
    }

    if issue_detected:
        ticket_info = create_rally_ticket(file.filename, details)
        response["message"] = "Issue detected. Rally ticket created."
        response["rally_ticket"] = ticket_info

    return response
