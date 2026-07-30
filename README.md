# 📚 Course Management System

A simple **Course Management System** built using **FastAPI** (Backend) and **Streamlit** (Frontend). This project demonstrates how a frontend application communicates with a REST API to perform basic CRUD (Create, Read, Update, Delete) operations.

> This project is intended for beginners who want to understand the workflow of connecting a FastAPI backend with a Streamlit frontend and deploying them separately.

---

## 🚀 Live Demo

### 🔹 Frontend (Streamlit)
https://coursemanager-ktnd2z9gzkfrealj58fqdb.streamlit.app/

### 🔹 Backend API (FastAPI)
https://course-manager-s5bk.onrender.com

### 🔹 API Documentation (Swagger UI)
https://course-manager-s5bk.onrender.com/docs

---

# 📖 Project Overview

The application allows users to:

- 📋 View all available courses
- ➕ Add a new course
- ✏️ Update an existing course
- ❌ Delete a course

The frontend sends HTTP requests to the FastAPI backend, which processes the request and returns a JSON response.

---

# 🛠️ Tech Stack

### Frontend
- Streamlit
- Requests

### Backend
- FastAPI
- Uvicorn

### Deployment
- Render (Backend)
- Streamlit Community Cloud (Frontend)

---

# 📂 Project Structure

```text
Course-Management-System/
│
├── app.py              # Streamlit Frontend
├── main.py             # FastAPI Backend
├── requirements.txt
├── README.md
```

---

# 🔄 Application Workflow

```text
              User
                │
                ▼
      Streamlit Frontend
                │
      HTTP Requests (GET/POST/PUT/DELETE)
                │
                ▼
        FastAPI Backend
                │
      Process Request
                │
                ▼
       JSON Response
                │
                ▼
      Streamlit Displays Result
```

---

# 📌 REST API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/` | Redirect to Swagger UI |
| GET | `/courses` | View all courses |
| POST | `/add_course/{course_name}` | Add a new course |
| PUT | `/update_course/{old}/{new}` | Update a course |
| DELETE | `/delete_course/{course_name}` | Delete a course |

---

# ⚙️ Installation

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/course-management-system.git

cd course-management-system
```

---

## 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 3️⃣ Run FastAPI Backend

```bash
uvicorn main:app --reload
```

Backend runs on:

```
http://127.0.0.1:8000
```

Swagger Documentation:

```
http://127.0.0.1:8000/docs
```

---

## 4️⃣ Run Streamlit Frontend

```bash
streamlit run app.py
```

Frontend runs on:

```
http://localhost:8501
```

---

# 🌐 Deployment

## Backend

**Platform:** Render

Deployed FastAPI API:

```
https://course-manager-s5bk.onrender.com
```

---

## Frontend

**Platform:** Streamlit Community Cloud

Deployed Streamlit App:

```
https://coursemanager-e6as4gafpj5sgtjvcw5nks.streamlit.app/
```

---

# 📷 Features

- ✅ FastAPI REST API
- ✅ Streamlit User Interface
- ✅ CRUD Operations
- ✅ Swagger API Documentation
- ✅ Separate Frontend & Backend Deployment
- ✅ Beginner-Friendly Project Structure

---

# 📦 Requirements

```txt
fastapi
uvicorn
streamlit
requests
```

> **Note:** If deploying only the backend, `requirements.txt` can include:
>
> ```txt
> fastapi
> uvicorn
> ```
>
> For running the Streamlit frontend locally, install:
>
> ```txt
> streamlit
> requests
> ```

---

# 📚 Learning Outcomes

This project helps understand:

- REST APIs
- HTTP Methods (GET, POST, PUT, DELETE)
- FastAPI Basics
- Streamlit Basics
- Frontend–Backend Communication
- JSON Responses
- API Deployment using Render
- Streamlit Deployment
- Building a simple full-stack Python application

---

# 👨‍💻 Author

**K. J. M. B. Balaji**

- GitHub: https://github.com/BalajiKundula
- LinkedIn: https://www.linkedin.com/in/k-j-m-b-balaji-572160358

---

## ⭐ If you found this project helpful, consider giving it a Star on GitHub!
