# 🚀 FastAPI + PostgreSQL Boilerplate

A scalable **FastAPI** application with **PostgreSQL**, **SQLAlchemy**, and **async database support**.

## 📑 Features
✅ **FastAPI** - High-performance Python web framework  
✅ **PostgreSQL** - Robust relational database  
✅ **SQLAlchemy ORM** - For seamless database interactions  
✅ **Async Support** - Fully asynchronous DB queries  
✅ **Connection Pooling** - Efficient handling of multiple requests  
✅ **Lifespan Events** - Handles database setup & cleanup  
✅ **Dependency Injection** - Clean and scalable code  

---

## 🔧 Installation

### 1️⃣ **Clone the Repository**

git clone https://github.com/Nithin612/postgres_fastapi.git
cd fastapi-postgresql-boilerplate

---

### Create a Virtual Environment

python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows

### Install Dependencies
pip install -r requirements.txt

### Set Up Environment Variables
DATABASE_URL=postgresql+asyncpg://postgres:password@localhost:5432/mydatabase
SECRET_KEY=your_secret_key


### Run the Server
uvicorn app.main:app --reload

### API Documentation
Swagger UI (Interactive API Testing)
📌 URL: http://127.0.0.1:8000/docs

ReDoc (Structured API Docs)
📌 URL: http://127.0.0.1:8000/redoc
