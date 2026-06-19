# 🛡️ E-KYC Verification System

> **Production-Ready AI-Powered Electronic Know Your Customer (E-KYC) Verification Platform**

A scalable and secure E-KYC verification system built using **FastAPI**, **EasyOCR**, **DeepFace**, **JWT Authentication**, **SQLAlchemy**, and **Docker**. The platform automates customer onboarding by extracting identity information from Aadhaar documents, verifying facial identity through AI-powered face recognition, and securely storing verified customer records.

---

# 🏆 Key Achievements

### ✅ Developed a Modern Interactive Frontend

Built a responsive and user-friendly web interface using **Streamlit** to simplify the E-KYC verification workflow. The frontend provides intuitive pages for user authentication, customer registration, document upload, AI-powered identity verification, and customer management.

### ✅ Integrated Frontend with Secure REST APIs

Connected the Streamlit frontend with FastAPI REST endpoints using authenticated HTTP requests. Implemented JWT token management, session handling, protected navigation, and seamless communication between the presentation layer and backend services.

### ✅ Built an End-to-End AI-Powered E-KYC Verification Platform

Designed and developed a complete identity verification workflow that automates customer onboarding through OCR, facial recognition, secure authentication, and database management.

### ✅ Developed a Production-Ready Backend Architecture

Implemented a modular and scalable FastAPI backend following industry-standard software engineering principles including layered architecture, dependency injection, centralized configuration, and service-oriented design.

### ✅ Integrated Computer Vision for Identity Verification

Leveraged **EasyOCR** and **DeepFace (ArcFace)** to automatically extract Aadhaar information and perform facial verification between document images and user selfies.

### ✅ Implemented Enterprise-Grade Security

Secured APIs using JWT Authentication, bcrypt password hashing, protected routes, environment-based configuration management, and centralized exception handling.

### ✅ Automated Customer Verification Workflow

Reduced manual verification effort by automating data extraction, customer validation, duplicate detection, and face verification.

### ✅ Built Monitoring & Observability Features

Implemented structured logging, rotating log files, request tracking middleware, global error handling, and health monitoring endpoints.

### ✅ Containerized for Consistent Deployment

Dockerized the application for easy deployment, portability, and environment consistency across development and production systems.

### ✅ Designed for Enterprise Scalability

Architected the system to support future migration to PostgreSQL, Redis caching, CI/CD pipelines, Kubernetes deployment, and microservice expansion.

---

# 🚀 Features

## Authentication & Security

* JWT Authentication
* Secure Password Hashing (bcrypt)
* Token-Based Authorization
* Protected API Endpoints
* Environment Variable Management
* Centralized Exception Handling

## OCR-Based Data Extraction

* Aadhaar Number Extraction
* Name Extraction
* DOB Extraction
* Gender Extraction
* OCR Text Processing
* Data Validation

## AI Face Verification

* DeepFace Integration
* ArcFace Recognition Model
* Selfie vs Aadhaar Photo Matching
* Face Similarity Scoring
* Fraud Detection Support

## Database Management

* SQLAlchemy ORM
* SQLite Database
* Customer Record Management
* Duplicate Aadhaar Detection
* User Management

## Monitoring & Logging

* Rotating Log Files
* Request Logging Middleware
* Error Tracking
* Audit-Friendly Logs
* Health Monitoring API

## Deployment

* Docker Support
* Docker Compose Support
* Environment Configuration
* Production-Ready Structure

## 🎨 Frontend Features

The application includes a modern Streamlit-based web interface that provides an intuitive experience for administrators and operators.

### User Authentication

* User Registration
* Secure Login
* JWT Session Management
* Logout Functionality

### Dashboard

* Simple Navigation Sidebar
* Quick Access to Verification Features
* Responsive Layout
* Status Notifications

### Customer Registration

* Upload Aadhaar Document
* Upload Selfie Image
* Real-time Form Validation
* Instant Verification Results

### Customer Management

* View Verified Customers
* Search Customer Records
* Customer Details Page
* Duplicate Detection Feedback

### User Experience

* Custom CSS Styling
* Interactive Forms
* Progress Indicators
* Success & Error Notifications
* Mobile-Friendly Layout


---

# 🏗️ System Architecture

```text
                         ┌──────────────────────┐
                         │     Streamlit UI     │
                         │  (Frontend Client)   │
                         └──────────┬───────────┘
                                    │
                           REST API Calls (JWT)
                                    │
                                    ▼
                     ┌─────────────────────────┐
                     │       FastAPI API       │
                     └─────────┬───────────────┘
                               │
      ┌────────────────────────┼────────────────────────┐
      ▼                        ▼                        ▼

┌──────────────┐     ┌────────────────┐      ┌────────────────┐
│ Auth Service │     │ OCR Service    │      │ Face Service   │
└──────────────┘     └────────────────┘      └────────────────┘
      │                       │                        │
      ▼                       ▼                        ▼

 JWT Tokens            EasyOCR Engine         DeepFace ArcFace

                               │
                               ▼

                     ┌────────────────────┐
                     │ Customer Service   │
                     └─────────┬──────────┘
                               │
                               ▼

                     ┌────────────────────┐
                     │ SQLite Database    │
                     └────────────────────┘
```


---

# 📁 Project Structure

```text
e_kyc/
│
├── app/                            # FastAPI Backend
│   │
│   ├── api/                        # API Routes
│   │   ├── auth.py
│   │   ├── health.py
│   │   └── kyc.py
│   │
│   ├── core/                       # Core Configuration & Security
│   │   ├── auth_dependency.py
│   │   ├── config.py
│   │   ├── exception_handler.py
│   │   ├── logger.py
│   │   ├── request_logger.py
│   │   └── security.py
│   │
│   ├── db/                         # Database Layer
│   │   ├── database.py
│   │   ├── db_health.py
│   │   ├── init_db.py
│   │   └── models.py
│   │
│   ├── schemas/                    # Pydantic Schemas
│   │   ├── auth.py
│   │   └── customer.py
│   │
│   ├── services/                   # Business Logic
│   │   ├── aadhaar_service.py
│   │   ├── customer_service.py
│   │   ├── face_service.py
│   │   └── ocr_service.py
│   │
│   └── main.py                     # FastAPI Entry Point
│
├── frontend/                       # Streamlit Frontend
│   │
│   ├── Home.py                     # Landing Page
│   │
│   ├── pages/                      # Application Pages
│   │   ├── 0_Register.py
│   │   ├── 1_Login.py
│   │   ├── 2_Dashboard.py
│   │   ├── 3_Verify_Customer.py
│   │   └── 4_Customers.py
│   │
│   ├── assets/                     # Static Assets
│   │   ├── styles.css
│   │   ├── logo.png
│   │   └── images/
│   │
│   └── utils/                      # Frontend Utilities
│
├── uploads/
│   ├── documents/
│   └── selfies/
│
├── logs/
│   ├── app.log
│   └── error.log
│
├── Dockerfile
├── docker-compose.yml
├── start.sh
├── requirements.txt
├── .env
├── kyc.db
└── README.md
```
---

# ⚙️ Technology Stack

| Category          | Technology         |
| ----------------- | ------------------ |
| Backend Framework | FastAPI            |
| OCR Engine        | EasyOCR            |
| Face Recognition  | DeepFace (ArcFace) |
| Authentication    | JWT                |
| Password Security | bcrypt             |
| ORM               | SQLAlchemy         |
| Database          | SQLite             |
| API Documentation | Swagger UI         |
| Containerization  | Docker             |
| Logging           | Python Logging     |

---
# 🖥️ Frontend Architecture

The frontend is developed using **Streamlit** and communicates with the FastAPI backend through RESTful APIs.

```text
User
 │
 ▼
Streamlit Interface
 │
 ├── Authentication Pages
 ├── Customer Registration
 ├── Document Upload
 ├── Customer Dashboard
 └── Customer Management
 │
 ▼
HTTP Requests (JWT)
 │
 ▼
FastAPI Backend
```

### Frontend Responsibilities

* User authentication
* Session management
* Aadhaar and selfie uploads
* Display OCR results
* Display face verification results
* Customer management
* API error handling
* Interactive notifications

---

# 🔄 E-KYC Workflow

```text
Upload Aadhaar Image
          │
          ▼
      EasyOCR
          │
          ▼
 Extract Aadhaar Details
          │
          ▼
Duplicate Aadhaar Check
          │
          ▼
Upload Selfie
          │
          ▼
DeepFace Verification
          │
          ▼
Identity Match?
      │         │
     No        Yes
      │         │
      ▼         ▼
 Reject    Store Customer
                 │
                 ▼
        Successful Registration
```

---

# 🔐 Authentication Flow

```text
Register User
      │
      ▼
Password Hashing (bcrypt)
      │
      ▼
Store User
      │
      ▼
Login
      │
      ▼
Generate JWT Token
      │
      ▼
Access Protected APIs
```

---

# 📖 API Endpoints

## Authentication

### Register User

```http
POST /auth/register
```

Request:

```json
{
  "username": "admin",
  "email": "admin@gmail.com",
  "password": "admin123"
}
```

Response:

```json
{
  "message": "User created"
}
```

---

### Login

```http
POST /auth/login
```

Request:

```json
{
  "username": "admin",
  "password": "admin123"
}
```

Response:

```json
{
  "access_token": "JWT_TOKEN",
  "token_type": "bearer"
}
```

---

## Health Check

### Check Application Health

```http
GET /health
```

Response:

```json
{
  "status": "healthy",
  "database": true
}
```

---

## KYC Verification

### Verify Customer Identity

```http
POST /kyc/verify
```

Form Data:

```text
document : Aadhaar Image
selfie   : Selfie Image
```

Response:

```json
{
  "status": "success",
  "customer_id": 1,
  "details": {
    "name": "Pranav Gupta",
    "dob": "15/05/2001",
    "gender": "Male"
  }
}
```

---

# 🚀 Local Development Setup

## 1. Clone Repository

```bash
git clone https://github.com/your-username/e_kyc.git
cd e_kyc
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Linux/Mac

```bash
python -m venv .venv
source .venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure Environment Variables

Create `.env`

```env
APP_NAME=E-KYC Verification

DATABASE_URL=sqlite:///./kyc.db

SECRET_KEY=your-super-secret-key

ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=60

UPLOAD_DOC_DIR=uploads/documents

UPLOAD_SELFIE_DIR=uploads/selfies

LOG_LEVEL=INFO
```

---

## 5. Initialize Database

```bash
python -m app.db.init_db
```

---

## 6. Run Application

```Bash
# Terminal 1
uvicorn app.main:app --reload

# Terminal 2
streamlit run frontend/Home.py
```
Server:

```text
Frontend:
http://127.0.0.1:8501

Backend API:
http://127.0.0.1:8000

Swagger UI:
http://127.0.0.1:8000/docs
```
---

# 🐳 Docker Setup

## Build

```bash
docker compose build
```

## Run

```bash
docker compose up
```

## Stop

```bash
docker compose down
```

---

# 📊 Logging & Monitoring

### Application Logs

```text
logs/app.log
```

### Error Logs

```text
logs/error.log
```

### Request Tracking

Captures:

* Endpoint Access
* Request Method
* Status Codes
* Processing Time
* Exceptions

---

# 🔒 Security Features

* JWT Authentication
* bcrypt Password Hashing
* Protected Routes
* Centralized Error Handling
* Secure Configuration Management
* Request Monitoring
* Structured Logging
* Audit-Friendly Architecture

---

# 📈 Future Enhancements

* PostgreSQL Integration
* Redis Caching
* OTP Verification
* Face Liveness Detection
* Aadhaar Masking
* Rate Limiting
* Alembic Migrations
* CI/CD Pipeline
* Kubernetes Deployment
* Automated Testing
* Cloud Deployment (AWS/Azure/GCP)

---

# 🎯 Learning Outcomes

This project demonstrates expertise in:

* FastAPI Development
* REST API Design
* Authentication & Authorization
* Computer Vision Applications
* OCR Systems
* Face Recognition Systems
* SQLAlchemy ORM
* Database Design
* Docker & Containerization
* Logging & Monitoring
* Software Architecture
* Production-Grade Backend Engineering

---

# 👨‍💻 Author

**Pranav Gupta**

AI Engineer | Data Scientist | Data Analyst

GitHub: https://github.com/Pranav-Gupta-ji

LinkedIn:  https://www.linkedin.com/in/pranavguptaji/

### Skills Demonstrated

* Python
* FastAPI
* Computer Vision
* Deep Learning Integration
* SQLAlchemy
* JWT Authentication
* Docker
* API Development
* System Design

---

# ⭐ Project Impact

This project showcases the development of a **real-world AI-powered identity verification system** that combines **Computer Vision, Secure Backend Engineering, Authentication, and DevOps practices** to automate customer onboarding while maintaining security, scalability, and maintainability.
