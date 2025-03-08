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
| React-based Frontend                           | 🚧 Yet to Start                                           |

## 🛠️ Tech Stack
| **Component**  | **Technology**         | **Status**                         |
|----------------|------------------------|------------------------------------|
| Frontend       | React (JS)             | 🚧 Not Started                     |
| Backend        | Flask/FastAPI (Python) | ✅ API Implemented & Tested Locally |
| Database       | PostgreSQL (AWS RDS)   | 🚧 Pending AWS Setup (Local DB ✅)  |
| Storage        | AWS S3                 | 🚧 Pending Integration             |
| Hosting        | AWS EC2 (Ubuntu)       | 🚧 Pending Deployment              |
| Authentication | JWT (JSON Web Token)   | ✅ Implemented with RBAC            |

## 📂 Project Structure (Work in Progress 🚧)
```
store-my-docs/
│── backend/                 # Backend (Flask/FastAPI) ✅ Implemented
│   ├── routes/              # API route handlers ✅ Implemented & Secured
│   ├── models/              # Database models ✅ Implemented
│   ├── app.py               # Main backend application ✅ Implemented
│   ├── db.py                # Database connection setup ✅ Implemented
│   ├── config.py            # Configuration settings ✅ Implemented
│   ├── .env                 # Environment variables 🚧 Pending AWS Setup
│   ├── .env                 # Centralizes and initializes Flask extensions ✅ Implemented
│── frontend/                # Frontend (React) 🚧 Not Started
│   ├── src/                 # Main frontend files 🚧 Not Started
│   ├── public/              # Static assets 🚧 Not Started
│   ├── package.json         # Frontend dependencies 🚧 Not Started
│── .gitignore               # Ignore unnecessary files ✅ Updated
│── README.md                # Project documentation ✅ Updated

```

## 🔧 Setup Instructions (Work in Progress 🚧)
🚀 We are currently setting up the backend in stages. Once local testing is complete, we will proceed with AWS deployment.

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/store-my-docs.git
cd store-my-docs
```

- ✅ Repository Setup Done
- ✅ Backend Implemented & Tested Locally
- 🚧 Frontend Setup Not Started Yet

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

### 3️⃣ Frontend Setup (React)
- 🚧 Not Started Yet
```bash
cd frontend
npm install
npm start
```

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

## 📌 Future Scope
### 🚀 Planned Features (Not Started Yet 🚧)
- 📄 File Preview: Preview PDFs before downloading
- 🔗 File Sharing: Generate shareable links
- 📂 Folder Organization: Create folders to manage documents

## ©️ Credits
- Markdown tables: https://www.tablesgenerator.com/markdown_tables
- Deploy flask app with nginx using gunicorn and supervisor - https://medium.com/ymedialabs-innovation/deploy-flask-app-with-nginx-using-gunicorn-and-supervisor-d7a93aa07c18