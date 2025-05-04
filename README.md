# AI-powered Jenkins Log Analyzer (Stage 1)
ai-log-chatbot/
├── backend/
│   ├── app/
│   ├── Dockerfile
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   ├── Dockerfile
│   ├── package.json
│   └── tsconfig.json
│
├── docker-compose.yml
├── .env.example
└── README.md

🚀 Key Features
📤 Upload Jenkins log files (.log, .txt)

🧠 Detects errors/exceptions automatically

🎟️ Creates Rally defect ticket if issues found

⚡ FastAPI backend + React (TypeScript) frontend

🐳 Simple Docker Compose setup (local, secure)


⚙️ Setup & Run (Step by Step)
git clone <repo_url>
cd latest-chatbot

2️⃣ Configure Rally Credentials
cp .env.example .env
nano .env

RALLY_API_KEY=your_rally_api_key
RALLY_PROJECT=your_project_oid
RALLY_WORKSPACE=your_workspace_oid

3️⃣ Build & Run (Docker Compose)
docker compose up --build

🌐 Access App
Frontend (React) → http://localhost:3000
Backend API (FastAPI) → http://localhost:8000/docs

🖥️ Usage Guide
Open browser → http://localhost:3000

Select a .log or .txt Jenkins log file

Click Upload & Analyze

See results:

✅ No issues → Safe

❌ Issues found → Rally ticket auto-created

🔐 Security Notes
Rally API Key is securely loaded from .env (never hardcoded)

No data leaves on-prem server (Stage 1 is fully local)

All sensitive info stays within Docker network

🛠️ Tech Stack
| Layer     | Technology              |
| --------- | ----------------------- |
| Frontend  | React + TypeScript      |
| Backend   | FastAPI + Python        |
| Rally API | REST (ZSESSIONID token) |
| DevOps    | Docker + Docker Compose |






