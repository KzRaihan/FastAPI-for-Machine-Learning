# ⚡ FastAPI for Machine Learning

### The Complete Hands-On Course: From API Fundamentals to ML Model Deployment

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge\&logo=python\&logoColor=white)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-Latest-009688?style=for-the-badge\&logo=fastapi\&logoColor=white)](https://fastapi.tiangolo.com/)
[![Pydantic](https://img.shields.io/badge/Pydantic-Latest-E92063?style=for-the-badge\&logo=pydantic\&logoColor=white)](https://docs.pydantic.dev/)
[![Docker](https://img.shields.io/badge/Docker-Latest-2496ED?style=for-the-badge\&logo=docker\&logoColor=white)](https://www.docker.com/)
[![AWS](https://img.shields.io/badge/AWS-Cloud-232F3E?style=for-the-badge\&logo=amazon-aws\&logoColor=white)](https://aws.amazon.com/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-brightgreen?style=for-the-badge)](CONTRIBUTING.md)

**Build production-oriented APIs for Machine Learning models — from your first FastAPI endpoint to Dockerized and cloud-deployed ML services.**

---

# 🎯 Learning Objectives

By completing this repository, the main objectives are to understand:

* What APIs are and how they work
* REST API architecture
* HTTP methods and status codes
* FastAPI architecture and philosophy
* FastAPI application structure
* Path and query parameters
* Request and response handling
* Pydantic data validation
* POST, PUT, and DELETE operations
* Automatic API documentation
* Serving Machine Learning models through FastAPI
* Designing ML inference APIs
* API validation and error handling
* Testing FastAPI applications
* Docker fundamentals
* Dockerizing FastAPI applications
* Deploying FastAPI applications to AWS
* Building an end-to-end Machine Learning API

---

# 🧠 Curriculum

The curriculum is divided into thirteen progressive modules.

```text
API Fundamentals
       ↓
FastAPI Fundamentals
       ↓
HTTP Methods
       ↓
Path & Query Parameters
       ↓
Pydantic
       ↓
POST Requests
       ↓
PUT & DELETE
       ↓
ML Model Serving
       ↓
API Improvement
       ↓
Docker for ML
       ↓
FastAPI + Docker
       ↓
AWS Deployment
       ↓
Final FastAPI Project
```

---

# 🌐 Module 01 — Introduction to APIs and FastAPI for Machine Learning

This module establishes the fundamental concepts required before building FastAPI applications.

### Topics

* What is an API?
* Why APIs are required
* Client-server architecture
* REST API
* Request and response
* JSON
* HTTP
* HTTP status codes
* API endpoints
* APIs in Machine Learning
* Why ML models need APIs
* FastAPI for Machine Learning

### ML API Concept

```text
Client
   │
   │ Request
   ▼
API
   │
   ▼
ML Model
   │
   ▼
Prediction
   │
   │ Response
   ▼
Client
```

---

# ⚡ Module 02 — FastAPI Philosophy | Setup | Installation | Code Demo

This module introduces FastAPI and the development environment.

### Topics

* What is FastAPI?
* FastAPI philosophy
* FastAPI architecture
* FastAPI vs traditional web frameworks
* Installing FastAPI
* Installing Uvicorn
* Creating the first FastAPI application
* Running a FastAPI server
* `uvicorn`
* Automatic API documentation
* Swagger UI
* ReDoc

### First FastAPI Application

```text
FastAPI Application
        │
        ├── Application
        │
        ├── Routes
        │
        ├── Request
        │
        └── Response
```

---

# 🔄 Module 03 — HTTP Methods in FastAPI

This module focuses on the fundamental HTTP operations used when developing APIs.

### Topics

* GET
* POST
* PUT
* DELETE
* HTTP request
* HTTP response
* Status codes
* API endpoints

### HTTP Workflow

```text
GET     → Retrieve data
POST    → Create data
PUT     → Update data
DELETE  → Delete data
```

---

# 📍 Module 04 — Path & Query Parameters

This module explains how FastAPI receives parameters from client requests.

### Topics

* Path parameters
* Query parameters
* Required parameters
* Optional parameters
* Type conversion
* Type validation
* Combining path and query parameters

### Example

```text
/items/{item_id}?search=python
```

FastAPI automatically validates and converts typed parameters.

---

# 🧩 Module 05 — Pydantic Crash Course

Pydantic provides structured data validation and is one of the most important components when building FastAPI applications.

### Topics

* What is Pydantic?
* Pydantic models
* BaseModel
* Type hints
* Required fields
* Optional fields
* Field validation
* Nested models
* Request schemas
* Response schemas

### Pydantic Workflow

```text
Client JSON
     │
     ▼
Pydantic Model
     │
     ▼
Validation
     │
 ┌───┴────┐
 │        │
Valid   Invalid
 │        │
 ▼        ▼
API     Error
```

---

# 📤 Module 06 — POST Request in FastAPI

This module focuses on receiving structured data from clients.

### Topics

* POST requests
* Request body
* JSON payload
* Pydantic request models
* Input validation
* Structured responses
* HTTP status codes

### Request Flow

```text
Client
  │
  │ POST + JSON
  ▼
FastAPI
  │
  ▼
Pydantic
  │
  ▼
Validation
  │
  ▼
Business Logic
  │
  ▼
Response
```

---

# 🔧 Module 07 — PUT & DELETE in FastAPI

This module introduces resource modification and deletion.

### Topics

* PUT requests
* Updating resources
* DELETE requests
* Deleting resources
* Path parameters
* Status codes
* API response design

### CRUD Concept

```text
Create  → POST
Read    → GET
Update  → PUT
Delete  → DELETE
```

---

# 🤖 Module 08 — Serving ML Models with FastAPI

This is the primary Machine Learning-focused module of the course.

The goal is to learn how to expose a trained Machine Learning model through a REST API.

### Topics

* Loading trained ML models
* Model serialization
* Joblib
* Model preprocessing
* Pydantic prediction schemas
* Prediction endpoints
* Input validation
* ML inference
* Returning predictions
* Separating training and inference
* Testing ML APIs

### ML Model Serving Architecture

```text
                 ┌─────────────────┐
                 │     Client      │
                 └────────┬────────┘
                          │
                          │ HTTP Request
                          ▼
                 ┌─────────────────┐
                 │    FastAPI      │
                 │      API        │
                 └────────┬────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │    Pydantic     │
                 │    Validation   │
                 └────────┬────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │ Preprocessing   │
                 └────────┬────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │  Trained Model  │
                 └────────┬────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │   Prediction    │
                 └────────┬────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │  JSON Response  │
                 └─────────────────┘
```

### Project Structure

```text
08_Serving_ML_Models/

├── notebooks/
│   └── model_experimentation.ipynb
│
├── src/
│   ├── __init__.py
│   ├── train_model.py
│   ├── predict.py
│   └── schemas.py
│
├── artifacts/
│
├── tests/
│   └── test_prediction.py
│
├── main.py
└── README.md
```

### Major Project

**Build an ML Prediction API**

The project will demonstrate:

1. Train a Machine Learning model
2. Evaluate the model
3. Save the trained model
4. Load the model inside FastAPI
5. Create a prediction schema
6. Receive input from a client
7. Validate the input
8. Generate a prediction
9. Return the prediction as JSON
10. Test the API

---

# 🚀 Module 09 — Improving the FastAPI API

This module focuses on improving the quality and maintainability of FastAPI applications.

### Topics

* API metadata
* Response models
* Error handling
* HTTP exceptions
* Status codes
* Input validation
* Response validation
* API documentation
* Testing
* Project organization
* Separation of responsibilities

### Goal

Move from:

```text
Simple FastAPI Application
```

to:

```text
Structured
     ↓
Validated
     ↓
Tested
     ↓
Maintainable
     ↓
Production-Oriented API
```

---

# 🐳 Module 10 — Docker for Machine Learning

This module introduces Docker and containerization concepts.

### Topics

* What is Docker?
* Why Docker?
* Containers
* Images
* Containers vs Virtual Machines
* Dockerfile
* Docker commands
* `.dockerignore`
* Installing dependencies inside containers
* Containerizing Python applications
* Docker for Machine Learning

### Docker Workflow

```text
Application
    │
    ▼
Dockerfile
    │
    ▼
Docker Image
    │
    ▼
Docker Container
    │
    ▼
Running Application
```

---

# 🐳 Module 11 — FastAPI + Docker

This module combines FastAPI and Docker to create a containerized API application.

### Topics

* Creating a Dockerfile
* FastAPI inside Docker
* Uvicorn inside Docker
* Port mapping
* Docker image creation
* Docker containers
* Docker Compose
* Environment configuration
* Containerized ML APIs

### Architecture

```text
                 ┌─────────────────┐
                 │     Client      │
                 └────────┬────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │ Docker Container│
                 │                 │
                 │    FastAPI      │
                 │       │         │
                 │       ▼         │
                 │    ML Model     │
                 └─────────────────┘
```

---

# ☁️ Module 12 — How to Deploy a FastAPI API on AWS

This module introduces cloud deployment for FastAPI applications.

### Topics

* Cloud deployment fundamentals
* AWS basics
* Preparing FastAPI for production
* Environment variables
* Production server
* Docker-based deployment
* AWS deployment workflow
* Application configuration
* Security considerations
* Monitoring
* Troubleshooting

### Deployment Workflow

```text
Local FastAPI
      │
      ▼
Dockerize
      │
      ▼
Docker Image
      │
      ▼
AWS
      │
      ▼
Cloud Application
      │
      ▼
Public API
```

---

# 🚀 Module 13 — FastAPI Course Project

The final module combines the concepts learned throughout the course.

### Final Project

Build an end-to-end **Machine Learning Prediction API** using:

* FastAPI
* Pydantic
* Machine Learning
* Model serialization
* API validation
* Testing
* Docker
* AWS

### Complete Workflow

```text
Dataset
   │
   ▼
Data Preprocessing
   │
   ▼
Model Training
   │
   ▼
Model Evaluation
   │
   ▼
Model Serialization
   │
   ▼
FastAPI
   │
   ▼
Pydantic Validation
   │
   ▼
Prediction Endpoint
   │
   ▼
Docker
   │
   ▼
AWS
   │
   ▼
Production API
```

---

# 🛠️ Technology Stack

The implementation will primarily use:

* **Python**
* **FastAPI**
* **Uvicorn**
* **Pydantic**
* **REST API**
* **HTTP / JSON**
* **Pandas**
* **NumPy**
* **Scikit-learn**
* **Joblib**
* **Pytest**
* **Docker**
* **Docker Compose**
* **AWS**
* **Git & GitHub**

The exact Machine Learning models and supporting libraries may vary between individual projects.

---

# 📁 Repository Structure

```text
FastAPI-for-Machine-Learning/
│
├── 01_Introduction_to_APIs/
│   ├── README.md
│   └── api_basics.py
│
├── 02_FastAPI_Setup/
│   ├── README.md
│   └── main.py
│
├── 03_HTTP_Methods/
│   ├── README.md
│   └── main.py
│
├── 04_Path_and_Query_Params/
│   ├── README.md
│   └── main.py
│
├── 05_Pydantic/
│   ├── README.md
│   ├── main.py
│   └── schemas.py
│
├── 06_POST_Request/
│   ├── README.md
│   └── main.py
│
├── 07_PUT_and_DELETE/
│   ├── README.md
│   └── main.py
│
├── 08_Serving_ML_Models/
│   ├── README.md
│   ├── main.py
│   │
│   ├── notebooks/
│   │   └── model_experimentation.ipynb
│   │
│   ├── src/
│   │   ├── __init__.py
│   │   ├── train_model.py
│   │   ├── predict.py
│   │   └── schemas.py
│   │
│   ├── artifacts/
│   │   └── .gitkeep
│   │
│   └── tests/
│       └── test_prediction.py
│
├── 09_Improving_FastAPI_API/
│   ├── README.md
│   └── main.py
│
├── 10_Docker_for_Machine_Learning/
│   ├── README.md
│   ├── Dockerfile
│   └── .dockerignore
│
├── 11_FastAPI_Docker/
│   ├── README.md
│   ├── main.py
│   ├── Dockerfile
│   ├── .dockerignore
│   └── docker-compose.yml
│
├── 12_AWS_Deployment/
│   ├── README.md
│   └── deployment_notes.md
│
├── 13_FastAPI_Course_Project/
│   ├── README.md
│   └── main.py
│
├── assets/
│
├── notebooks/
│
├── docs/
│   ├── api_notes.md
│   ├── ml_model_serving.md
│   ├── docker_notes.md
│   └── aws_deployment.md
│
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md
```

---

# 🚀 How to Run the Application

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/KzRaihan/FastAPI-for-Machine-Learning.git
```

### 2️⃣ Navigate to the Repository

```bash
cd FastAPI-for-Machine-Learning
```

### 3️⃣ Create a Virtual Environment

Using Conda:

```bash
conda create -n FastAPI python=3.11
```

### 4️⃣ Activate the Environment

```bash
conda activate FastAPI
```

### 5️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 6️⃣ Run a FastAPI Application

For example:

```bash
cd 02_FastAPI_Setup
```

Then:

```bash
uvicorn main:app --reload
```

### 7️⃣ Open the API

```text
http://127.0.0.1:8000
```

### Swagger UI

```text
http://127.0.0.1:8000/docs
```

### ReDoc

```text
http://127.0.0.1:8000/redoc
```

---

# 🐳 Run with Docker

Build the Docker image:

```bash
docker build -t fastapi-ml-api .
```

Run the container:

```bash
docker run -p 8000:8000 fastapi-ml-api
```

For Docker Compose:

```bash
docker compose up --build
```

---

# 📚 References

* [FastAPI Course — YouTube Playlist](https://www.youtube.com/watch?v=WJKsPchji0Q&list=PLKnIA16_RmvZ41tjbKB2ZnwchfniNsMuQ)
* [FastAPI Official Documentation](https://fastapi.tiangolo.com/)
* [Pydantic Documentation](https://docs.pydantic.dev/)
* [Uvicorn Documentation](https://www.uvicorn.org/)
* [Docker Documentation](https://docs.docker.com/)
* [Scikit-learn Documentation](https://scikit-learn.org/)
* [AWS Documentation](https://docs.aws.amazon.com/)


---

# 👨‍💻 Author

**Md Kamruzzaman**

Computer Science & Engineering Graduate

Interested in **AI/ML, Deep Learning, Generative AI, Computer Vision, Agentic AI, and Intelligent AI Systems**.

* GitHub: [@KzRaihan](https://github.com/KzRaihan)
* LinkedIn: [@kzraihan](https://www.linkedin.com/in/kzraihan/)
