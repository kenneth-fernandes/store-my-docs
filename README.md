# 📄 ☁ Store My Docs - Online Document Storage Web App
A simple document storage web application where users can upload, view, delete, and manage documents securely online. Built using Flask/FastAPI for backend, React for frontend, and AWS (EC2, RDS, S3) for hosting & storage.

## 🏗️ System Architecture
![System Architecture](https://github.com/kenneth-fernandes/store-my-docs/blob/main/backend/docs/system-architecture.png)

The diagram above represents the full system design, showing how the frontend, backend, and AWS services interact.
## 🚀 Features (Work in Progress 🚧)
| Feature                                        | Status                                                   |
|------------------------------------------------|----------------------------------------------------------|
| User Registration & Login (JWT Authentication) | ✅ Implemented & Secure with RBAC                         |
| Upload, View & Delete Documents                | ✅ Backend API Implemented & Ownership Restrictions Added |
| Secure Document Storage using AWS S3           | 🚧 Pending Integration                                    |
| PostgreSQL Database (AWS RDS)                  | 🚧 Pending Setup (Local DB Working ✅)                     |
| REST API for Backend                           | ✅ Implemented & Secure (Rate Limiting Added)             |
| React-based Frontend (Login & Register)        | ✅ Implemented & Tested Locally                           |
| Dashboard UI (Upload/View/Delete Docs)         | 🚧 In Progress                                            |

## 🛠️ Tech Stack
| Component | Technology           | Status                             |
|-----------|----------------------|------------------------------------|
| Frontend  | React (JS)           | ✅ Authentication UI Implemented    |
| Backend   | Flask (Python)       | ✅ API Implemented & Tested Locally |
| Database  | PostgreSQL (AWS RDS) | 🚧 Pending AWS Setup (Local DB ✅)   |
| Storage   | AWS S3               | 🚧 Pending Integration              |
| Hosting   | AWS EC2 (Ubuntu)     | 🚧 Pending Deployment               |
| Auth      | JWT (JSON Web Token) | ✅ Implemented with RBAC            |

## 📂 Project Structure (Work in Progress 🚧)
```
store-my-docs/
│── backend/                 # Backend (Flask) ✅ Implemented
│   ├── routes/              # API route handlers ✅ Implemented & Secured
│   ├── models/              # Database models ✅ Implemented
│   ├── tests/               # Unit & Integration Tests ✅ Implemented
│   ├── app.py               # Main backend application ✅ Implemented
│   ├── db.py                # Database connection setup ✅ Implemented
│   ├── config.py            # Configuration settings ✅ Implemented
│   ├── extensions.py        # Centralized Flask extensions ✅ Implemented
│   ├── .env                 # Environment variables 🚧 Pending AWS Setup
│── frontend/                # Frontend (React) ✅ In Progress
│   ├── src/                 # Main frontend files ✅ Implemented
│   │   ├── pages/           # React Pages (Login, Register, Dashboard) ✅ Implemented
│   │   ├── api/             # API calls to backend ✅ Implemented
│   │   ├── context/         # Global Authentication State ✅ Implemented
│   │   ├── components/      # Reusable UI Components ✅ Implemented
│   ├── public/              # Static assets 🚧 Not Started
│   ├── package.json         # Frontend dependencies ✅ Implemented
│── .gitignore               # Ignore unnecessary files ✅ Updated
│── README.md                # Project documentation ✅ Updated


```

## 🔧 Setup Instructions (Work in Progress 🚧)
🚀 We are currently setting up the frontend in stages.  Once local testing is complete, we will proceed with AWS deployment.

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/store-my-docs.git
cd store-my-docs
```

- ✅ Repository Setup Done
- ✅ Backend Implemented & Tested Locally
- ✅ Frontend Authentication Implemented

### 2️⃣ Backend Setup (Flask/FastAPI)
```bash
cd backend
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

- ✅ Virtual Environment Created
- ✅ Database (Local PostgreSQL) Connected
- ✅ API Routes Implemented & Tested
- ✅ Security Added (Rate Limiting, RBAC, JWT, Security Headers)
- 🚧 Pending AWS RDS Setup

### 3️⃣ Test API Locally
- 📌 Start Backend
```bash
python backend/app.py
```

- 📌 Test API Endpoints Using Swagger
- 📍 Open: http://127.0.0.1:5001/apidocs/
- ✅ All API routes are documented here!

### 4️⃣ Run Unit & Integration Tests
Run all unit tests:
``` bash
pytest tests/
```
📌 Expected Output:
```bash
======== test session starts ========
collected 10 items

tests/test_auth.py .... [100%]
tests/test_documents.py .... [100%]
tests/test_models.py .... [100%]
tests/test_db.py . [100%]
tests/test_app.py . [100%]

======== All tests passed! ========
```
✅ Unit tests ensure the backend is functioning correctly before deployment.

### 5️⃣ Frontend Setup (React)
Now that authentication UI is ready, run:
```bash
cd frontend
npm install
npm start
```
📌 Go to http://localhost:3000/
- ✅ Register new users
- ✅ Login with credentials
- ✅ Redirects to Dashboard after login
- ✅ Logout button works correctly

---
## 🌍 Deployment (AWS) (Work in Progress 🚧)
We will deploy the application after local testing is complete.

### AWS Components (Planned)
| Component                       | Status                   |
|---------------------------------|--------------------------|
| ☑️ EC2 (Ubuntu Server)           | 🚧 Created, Pending Setup |
| ☑️ AWS S3 (File Storage)         | 🚧 Pending Integration    |
| ☑️ AWS RDS (PostgreSQL Database) | 🚧 Pending Setup          |
| ☑️ Nginx & Gunicorn              | 🚧 Pending Configuration  |
| ☑️ GitHub Actions for CI/CD      | 🚧 Planned, Not Started   |

---
## 📌 Future Scope
### 🚀 Planned Features (Not Started Yet 🚧)
- 📄 File Preview: Preview PDFs before downloading
- 🔗 File Sharing: Generate shareable links
- 📂 Folder Organization: Create folders to manage documents
- 🔑 OAuth Integration: Allow login via Google & GitHub 
- 📊 Admin Dashboard: Track user activity and storage usage
---

### 📌 Next Steps
| Task                                               | Status               |
|----------------------------------------------------|----------------------|
| 🚀 Implement Dashboard UI (Upload/View/Delete Docs) | 🔜 Next Step          |
| 🎨 Finalize Frontend Design & UX                    | 🔜 Upcoming           |
| 🔗 Connect Frontend with Backend APIs               | 🔜 After Dashboard UI |
| 🔄 Automate CI/CD Pipeline (GitHub Actions)         | 🔜 Planned            |
---
## ©️ Credits
- Markdown tables: https://www.tablesgenerator.com/markdown_tables
- Deploy flask app with nginx using gunicorn and supervisor - https://medium.com/ymedialabs-innovation/deploy-flask-app-with-nginx-using-gunicorn-and-supervisor-d7a93aa07c18