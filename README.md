# FastAPI for Machine Learning

A practical and structured learning repository for mastering **FastAPI** and its application in **Machine Learning model serving**.

This repository covers FastAPI fundamentals, REST APIs, HTTP methods, request validation with Pydantic, Machine Learning API development, Docker containerization, and AWS deployment through hands-on examples and projects.

---

## 📌 Course Overview

**FastAPI** is a modern, high-performance Python web framework for building APIs.

For Machine Learning engineers, FastAPI provides a practical way to expose trained ML models as APIs so that other applications, websites, mobile applications, or services can send input data and receive predictions.

This course focuses on both:

* **FastAPI fundamentals**
* **Production-oriented Machine Learning model serving**

---

## 🎯 Learning Objectives

By completing this repository, I aim to learn how to:

* Understand APIs and REST architecture
* Understand the role of FastAPI in Machine Learning
* Build FastAPI applications from scratch
* Work with HTTP methods
* Handle path and query parameters
* Validate API input using Pydantic
* Build POST, PUT, and DELETE endpoints
* Serve trained Machine Learning models through APIs
* Improve API structure and reliability
* Containerize FastAPI applications with Docker
* Deploy FastAPI applications using AWS
* Build an end-to-end ML inference API

---

## 🛠️ Technologies

* Python
* FastAPI
* Uvicorn
* Pydantic
* REST API
* HTTP / JSON
* Scikit-learn
* Pandas
* NumPy
* Joblib
* Pytest
* Docker
* Docker Compose
* AWS

---

# 📚 Course Agenda

## 01. Introduction to APIs and FastAPI for Machine Learning

Learn:

* What is an API?
* What is a REST API?
* Client-server architecture
* Request and response
* JSON
* HTTP status codes
* Why APIs are important in Machine Learning
* Why FastAPI is useful for ML model deployment

---

## 02. FastAPI Philosophy | Setup | Installation | Code Demo

Learn:

* FastAPI architecture
* FastAPI philosophy
* Installing FastAPI
* Installing Uvicorn
* Creating the first FastAPI application
* Running a development server
* Automatic API documentation
* Swagger UI
* ReDoc

---

## 03. HTTP Methods in FastAPI

Learn and implement:

* `GET`
* `POST`
* `PUT`
* `DELETE`

Understand when each HTTP method is used in an API.

---

## 04. Path & Query Parameters

Learn:

* Path parameters
* Query parameters
* Optional parameters
* Parameter type validation
* Combining path and query parameters
* FastAPI automatic validation

Example:

```text
/items/{item_id}?search=python
```

---

## 05. Pydantic Crash Course

Learn:

* Pydantic models
* Data validation
* Type hints
* Required fields
* Optional fields
* Nested models
* Request schemas
* Response schemas

Pydantic will be used extensively when building Machine Learning APIs.

---

## 06. POST Request in FastAPI

Learn:

* POST requests
* Request body
* JSON payload
* Pydantic request models
* Input validation
* Returning structured responses

---

## 07. PUT & DELETE in FastAPI

Learn:

* Updating resources using `PUT`
* Deleting resources using `DELETE`
* Path parameters with PUT/DELETE
* API response design

---

# 🤖 08. Serving ML Models with FastAPI

This is the main Machine Learning-focused section of the repository.

Learn how to transform a trained Machine Learning model into an API.

### Workflow

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
Save Model Artifact
   │
   ▼
FastAPI Application
   │
   ▼
Prediction Endpoint
   │
   ▼
Client Request
   │
   ▼
ML Prediction
```

### Example Architecture

```text
                    ┌──────────────────┐
                    │   Client / User  │
                    └────────┬─────────┘
                             │
                             │ HTTP Request
                             ▼
                    ┌──────────────────┐
                    │     FastAPI     │
                    │      API        │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ Pydantic Schema  │
                    │ Input Validation │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ Preprocessing    │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ Trained ML Model │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │    Prediction    │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ JSON Response    │
                    └──────────────────┘
```

### Module Structure

```text
08_Serving_ML_Models/
│
├── README.md
├── main.py
│
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
│   └── .gitkeep
│
└── tests/
    └── test_prediction.py
```

The goal is to eventually build a reusable ML inference API that can accept new input data and return model predictions.

---

# 09. Improving the FastAPI API

Learn how to make an API more structured and production-oriented.

Topics include:

* API metadata
* Response models
* Error handling
* HTTP status codes
* Input validation
* Project organization
* API documentation
* Testing
* Separation of responsibilities

---

# 🐳 10. Docker for Machine Learning

Learn the fundamentals of Docker and why containerization is useful for Machine Learning applications.

Topics:

* What is Docker?
* Containers vs virtual machines
* Docker images
* Docker containers
* Dockerfile
* Docker commands
* `.dockerignore`
* Containerizing Python applications
* Containerizing ML applications

---

# 🐳 11. FastAPI + Docker

Build and containerize a FastAPI application.

Learn:

* Creating a Dockerfile
* Installing dependencies inside containers
* Running Uvicorn inside Docker
* Port mapping
* Docker Compose
* Building Docker images
* Running FastAPI containers

Example:

```text
FastAPI Application
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
   FastAPI API
```

---

# ☁️ 12. Deploying FastAPI on AWS

Learn the fundamentals of deploying a FastAPI application to AWS.

Topics include:

* Cloud deployment concepts
* Preparing FastAPI for deployment
* Production server configuration
* Docker-based deployment
* AWS infrastructure basics
* Environment variables
* Application security considerations
* Monitoring and troubleshooting

---

# 🚀 13. FastAPI Course Project

The final section will combine the concepts learned throughout the course into an end-to-end FastAPI application.

The project will demonstrate:

```text
Client
  │
  ▼
FastAPI
  │
  ├── Request Validation
  │
  ├── Business Logic
  │
  ├── ML Model
  │
  └── Prediction
  │
  ▼
JSON Response
```

The project may later be extended with:

* Machine Learning model inference
* Docker
* Automated testing
* API documentation
* Cloud deployment
* Database integration
* Authentication
* Monitoring

---

# 📂 Repository Structure

```text
FastAPI-for-Machine-Learning/
│
├── README.md
├── requirements.txt
├── .gitignore
├── LICENSE
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
└── docs/
    ├── api_notes.md
    ├── ml_model_serving.md
    ├── docker_notes.md
    └── aws_deployment.md
```

---

# ⚙️ Installation

## 1. Clone the repository

```bash
git clone <your-repository-url>
```

## 2. Navigate to the project

```bash
cd FastAPI-for-Machine-Learning
```

## 3. Create a virtual environment

Using Python:

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

## 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Running a FastAPI Application

Navigate to the relevant module.

For example:

```bash
cd 02_FastAPI_Setup
```

Run:

```bash
uvicorn main:app --reload
```

The API will normally be available at:

```text
http://127.0.0.1:8000
```

FastAPI automatically provides interactive API documentation.

### Swagger UI

```text
http://127.0.0.1:8000/docs
```

### ReDoc

```text
http://127.0.0.1:8000/redoc
```

---

# 🧪 Testing

Testing examples are maintained inside the relevant modules.

The ML API tests can be found in:

```text
08_Serving_ML_Models/tests/
```

Run tests using:

```bash
pytest
```

---

# 🐳 Docker

Build a Docker image:

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




## 🧑‍💻 Author

**Md Kamruzzaman**

Computer Science & Engineering
Machine Learning | Deep Learning | Generative AI

---

## Repository Topics

```text
FastAPI
Python
REST-API
Machine-Learning
ML-Model-Deployment
Model-Serving
Pydantic
Docker
AWS
MLOps
API-Development
```

---

## 📄 License

This project is intended for educational and learning purposes.
