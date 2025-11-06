# 🧪 Test4Case Backend

> The backend engine for **Test4Case** — an AI-powered testing and learning platform that helps developers and students understand software testing through **automated, explainable test generation**.

---

## 🚀 Overview

Test4Case bridges the gap between writing code and understanding how to test it.  
This backend, built with **FastAPI (Python)**, serves as the foundation that powers:

- ✅ **AI Test Generation** — automatically generate unit tests and explanations using Claude.
- ⚙️ **Sandboxed Execution** — safely run tests using a subprocess-based runner (PyTest).
- 💾 **Session Management** — optionally save user code, generated tests, and results for future replay.

---

## 🧠 Tech Stack

| Layer | Technology | Purpose |
|-------|-------------|----------|
| **Backend Framework** | FastAPI | REST API endpoints |
| **AI Integration** | Claude API | Intelligent test generation |
| **Test Runner** | PyTest (sandboxed) | Safe test execution |
| **Data Models** | Pydantic | Input/output validation |
| **Deployment** | Uvicorn / Docker | Fast, reliable server runtime |

---

## 🧩 API Endpoints (Planned)

| Endpoint | Method | Description |
|-----------|---------|-------------|
| `/generate-tests` | POST | Generate test cases + explanations from user code |
| `/run-tests` | POST | Execute tests safely and return structured results |
| `/save-session` | POST | (Optional) Save code, tests, and execution history |

---

## ⚙️ Local Setup

```bash
# 1️⃣ Clone the repository
git clone https://github.com/Ehiane/Test4Case.git
cd Test4Case

# 2️⃣ Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows

# 3️⃣ Install dependencies
pip install -r requirements.txt

# 4️⃣ Run the FastAPI server
uvicorn app.main:app --reload