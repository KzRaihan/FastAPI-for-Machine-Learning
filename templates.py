from pathlib import Path


# ============================================================
# FastAPI for Machine Learning
# Repository Template Generator
# ============================================================

# Root repository name
PROJECT_NAME = "FastAPI-for-Machine-Learning"


# ============================================================
# Folder Structure
# ============================================================

folders = [
    # --------------------------------------------------------
    # 01. Introduction
    # --------------------------------------------------------
    f"{PROJECT_NAME}/01_Introduction_to_APIs",

    # --------------------------------------------------------
    # 02. FastAPI Setup
    # --------------------------------------------------------
    f"{PROJECT_NAME}/02_FastAPI_Setup",

    # --------------------------------------------------------
    # 03. HTTP Methods
    # --------------------------------------------------------
    f"{PROJECT_NAME}/03_HTTP_Methods",

    # --------------------------------------------------------
    # 04. Path and Query Parameters
    # --------------------------------------------------------
    f"{PROJECT_NAME}/04_Path_and_Query_Params",

    # --------------------------------------------------------
    # 05. Pydantic
    # --------------------------------------------------------
    f"{PROJECT_NAME}/05_Pydantic",

    # --------------------------------------------------------
    # 06. POST Request
    # --------------------------------------------------------
    f"{PROJECT_NAME}/06_POST_Request",

    # --------------------------------------------------------
    # 07. PUT and DELETE
    # --------------------------------------------------------
    f"{PROJECT_NAME}/07_PUT_and_DELETE",

    # --------------------------------------------------------
    # 08. Serving ML Models
    # --------------------------------------------------------
    f"{PROJECT_NAME}/08_Serving_ML_Models",
    f"{PROJECT_NAME}/08_Serving_ML_Models/notebooks",
    f"{PROJECT_NAME}/08_Serving_ML_Models/src",
    f"{PROJECT_NAME}/08_Serving_ML_Models/artifacts",
    f"{PROJECT_NAME}/08_Serving_ML_Models/tests",

    # --------------------------------------------------------
    # 09. Improving FastAPI API
    # --------------------------------------------------------
    f"{PROJECT_NAME}/09_Improving_FastAPI_API",

    # --------------------------------------------------------
    # 10. Docker
    # --------------------------------------------------------
    f"{PROJECT_NAME}/10_Docker_for_Machine_Learning",

    # --------------------------------------------------------
    # 11. FastAPI + Docker
    # --------------------------------------------------------
    f"{PROJECT_NAME}/11_FastAPI_Docker",

    # --------------------------------------------------------
    # 12. AWS Deployment
    # --------------------------------------------------------
    f"{PROJECT_NAME}/12_AWS_Deployment",

    # --------------------------------------------------------
    # 13. Course Project
    # --------------------------------------------------------
    f"{PROJECT_NAME}/13_FastAPI_Course_Project",

    # --------------------------------------------------------
    # Documentation
    # --------------------------------------------------------
    f"{PROJECT_NAME}/docs",
]


# ============================================================
# Files to Create
# ============================================================

files = [
    # --------------------------------------------------------
    # Root files
    # --------------------------------------------------------
    f"{PROJECT_NAME}/README.md",
    f"{PROJECT_NAME}/requirements.txt",
    f"{PROJECT_NAME}/.gitignore",
    f"{PROJECT_NAME}/LICENSE",

    # --------------------------------------------------------
    # 01. Introduction
    # --------------------------------------------------------
    f"{PROJECT_NAME}/01_Introduction_to_APIs/README.md",
    f"{PROJECT_NAME}/01_Introduction_to_APIs/api_basics.py",

    # --------------------------------------------------------
    # 02. FastAPI Setup
    # --------------------------------------------------------
    f"{PROJECT_NAME}/02_FastAPI_Setup/README.md",
    f"{PROJECT_NAME}/02_FastAPI_Setup/main.py",

    # --------------------------------------------------------
    # 03. HTTP Methods
    # --------------------------------------------------------
    f"{PROJECT_NAME}/03_HTTP_Methods/README.md",
    f"{PROJECT_NAME}/03_HTTP_Methods/main.py",

    # --------------------------------------------------------
    # 04. Path and Query Params
    # --------------------------------------------------------
    f"{PROJECT_NAME}/04_Path_and_Query_Params/README.md",
    f"{PROJECT_NAME}/04_Path_and_Query_Params/main.py",

    # --------------------------------------------------------
    # 05. Pydantic
    # --------------------------------------------------------
    f"{PROJECT_NAME}/05_Pydantic/README.md",
    f"{PROJECT_NAME}/05_Pydantic/main.py",
    f"{PROJECT_NAME}/05_Pydantic/schemas.py",

    # --------------------------------------------------------
    # 06. POST Request
    # --------------------------------------------------------
    f"{PROJECT_NAME}/06_POST_Request/README.md",
    f"{PROJECT_NAME}/06_POST_Request/main.py",

    # --------------------------------------------------------
    # 07. PUT and DELETE
    # --------------------------------------------------------
    f"{PROJECT_NAME}/07_PUT_and_DELETE/README.md",
    f"{PROJECT_NAME}/07_PUT_and_DELETE/main.py",

    # --------------------------------------------------------
    # 08. Serving ML Models
    # --------------------------------------------------------
    f"{PROJECT_NAME}/08_Serving_ML_Models/README.md",
    f"{PROJECT_NAME}/08_Serving_ML_Models/main.py",
    f"{PROJECT_NAME}/08_Serving_ML_Models/notebooks/model_experimentation.ipynb",
    f"{PROJECT_NAME}/08_Serving_ML_Models/src/__init__.py",
    f"{PROJECT_NAME}/08_Serving_ML_Models/src/train_model.py",
    f"{PROJECT_NAME}/08_Serving_ML_Models/src/predict.py",
    f"{PROJECT_NAME}/08_Serving_ML_Models/src/schemas.py",
    f"{PROJECT_NAME}/08_Serving_ML_Models/artifacts/.gitkeep",
    f"{PROJECT_NAME}/08_Serving_ML_Models/tests/test_prediction.py",

    # --------------------------------------------------------
    # 09. Improving FastAPI
    # --------------------------------------------------------
    f"{PROJECT_NAME}/09_Improving_FastAPI_API/README.md",
    f"{PROJECT_NAME}/09_Improving_FastAPI_API/main.py",

    # --------------------------------------------------------
    # 10. Docker
    # --------------------------------------------------------
    f"{PROJECT_NAME}/10_Docker_for_Machine_Learning/README.md",
    f"{PROJECT_NAME}/10_Docker_for_Machine_Learning/Dockerfile",
    f"{PROJECT_NAME}/10_Docker_for_Machine_Learning/.dockerignore",

    # --------------------------------------------------------
    # 11. FastAPI + Docker
    # --------------------------------------------------------
    f"{PROJECT_NAME}/11_FastAPI_Docker/README.md",
    f"{PROJECT_NAME}/11_FastAPI_Docker/main.py",
    f"{PROJECT_NAME}/11_FastAPI_Docker/Dockerfile",
    f"{PROJECT_NAME}/11_FastAPI_Docker/.dockerignore",
    f"{PROJECT_NAME}/11_FastAPI_Docker/docker-compose.yml",

    # --------------------------------------------------------
    # 12. AWS Deployment
    # --------------------------------------------------------
    f"{PROJECT_NAME}/12_AWS_Deployment/README.md",
    f"{PROJECT_NAME}/12_AWS_Deployment/deployment_notes.md",

    # --------------------------------------------------------
    # 13. Course Project
    # --------------------------------------------------------
    f"{PROJECT_NAME}/13_FastAPI_Course_Project/README.md",
    f"{PROJECT_NAME}/13_FastAPI_Course_Project/main.py",

    # --------------------------------------------------------
    # Documentation
    # --------------------------------------------------------
    f"{PROJECT_NAME}/docs/api_notes.md",
    f"{PROJECT_NAME}/docs/ml_model_serving.md",
    f"{PROJECT_NAME}/docs/docker_notes.md",
    f"{PROJECT_NAME}/docs/aws_deployment.md",
]


# ============================================================
# Initial File Content
# ============================================================

file_contents = {
    f"{PROJECT_NAME}/README.md": """# FastAPI for Machine Learning

A practical FastAPI learning repository covering REST APIs,
Pydantic, HTTP methods, Machine Learning model serving,
Docker containerization, and AWS deployment.

## Course Topics

1. Introduction to APIs and FastAPI
2. FastAPI Setup
3. HTTP Methods
4. Path and Query Parameters
5. Pydantic
6. POST Requests
7. PUT and DELETE
8. Serving ML Models
9. Improving FastAPI APIs
10. Docker for Machine Learning
11. FastAPI + Docker
12. AWS Deployment
13. FastAPI Course Project

## Technologies

- Python
- FastAPI
- Pydantic
- Uvicorn
- Scikit-learn
- Pandas
- NumPy
- Docker
- AWS
""",

    f"{PROJECT_NAME}/requirements.txt": """fastapi
uvicorn[standard]
pydantic
scikit-learn
pandas
numpy
joblib
pytest
httpx
""",

    f"{PROJECT_NAME}/.gitignore": """__pycache__/
*.py[cod]

.venv/
venv/
env/

.env

.ipynb_checkpoints/
.pytest_cache/

artifacts/*
!artifacts/.gitkeep

*.pkl
*.joblib

.DS_Store
""",

    f"{PROJECT_NAME}/LICENSE": """MIT License

Copyright (c) 2026

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files...
""",

    f"{PROJECT_NAME}/08_Serving_ML_Models/main.py": """from fastapi import FastAPI


app = FastAPI(
    title="ML Model Prediction API",
    description="FastAPI application for serving a Machine Learning model.",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Machine Learning Prediction API is running."
    }
""",

    f"{PROJECT_NAME}/08_Serving_ML_Models/src/__init__.py": "",

    f"{PROJECT_NAME}/08_Serving_ML_Models/src/train_model.py": """# Train and save your Machine Learning model here.

def train_model():
    print("Model training will be implemented here.")


if __name__ == "__main__":
    train_model()
""",

    f"{PROJECT_NAME}/08_Serving_ML_Models/src/predict.py": """# Load the trained model and generate predictions here.

def predict(input_data):
    # Load model
    # Preprocess input
    # Generate prediction
    # Return prediction
    pass
""",

    f"{PROJECT_NAME}/08_Serving_ML_Models/src/schemas.py": """from pydantic import BaseModel


class PredictionRequest(BaseModel):
    # Add your ML model input features here.
    pass
""",

    f"{PROJECT_NAME}/08_Serving_ML_Models/tests/test_prediction.py": """def test_prediction_api():
    # Add API prediction tests here.
    assert True
""",

    f"{PROJECT_NAME}/08_Serving_ML_Models/notebooks/model_experimentation.ipynb":
        """""",

    f"{PROJECT_NAME}/08_Serving_ML_Models/artifacts/.gitkeep": "",

    f"{PROJECT_NAME}/02_FastAPI_Setup/main.py": """from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Hello FastAPI!"
    }
""",

    f"{PROJECT_NAME}/03_HTTP_Methods/main.py": """from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def get_method():
    return {"method": "GET"}


@app.post("/")
def post_method():
    return {"method": "POST"}


@app.put("/")
def put_method():
    return {"method": "PUT"}


@app.delete("/")
def delete_method():
    return {"method": "DELETE"}
""",

    f"{PROJECT_NAME}/04_Path_and_Query_Params/main.py": """from fastapi import FastAPI


app = FastAPI()


@app.get("/items/{item_id}")
def get_item(item_id: int, search: str | None = None):

    return {
        "item_id": item_id,
        "search": search
    }
""",

    f"{PROJECT_NAME}/05_Pydantic/main.py": """from fastapi import FastAPI
from schemas import User


app = FastAPI()


@app.post("/users")
def create_user(user: User):

    return {
        "message": "User created successfully",
        "user": user
    }
""",

    f"{PROJECT_NAME}/05_Pydantic/schemas.py": """from pydantic import BaseModel


class User(BaseModel):
    name: str
    age: int
    email: str
""",

    f"{PROJECT_NAME}/06_POST_Request/main.py": """from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class Item(BaseModel):
    name: str
    price: float


@app.post("/items")
def create_item(item: Item):

    return {
        "message": "Item created successfully",
        "item": item
    }
""",

    f"{PROJECT_NAME}/07_PUT_and_DELETE/main.py": """from fastapi import FastAPI


app = FastAPI()


@app.put("/items/{item_id}")
def update_item(item_id: int):

    return {
        "message": "Item updated",
        "item_id": item_id
    }


@app.delete("/items/{item_id}")
def delete_item(item_id: int):

    return {
        "message": "Item deleted",
        "item_id": item_id
    }
""",

    f"{PROJECT_NAME}/09_Improving_FastAPI_API/main.py": """from fastapi import FastAPI


app = FastAPI(
    title="Improved FastAPI Application",
    description="Example of a more structured FastAPI application.",
    version="1.0.0"
)


@app.get("/")
def home():

    return {
        "status": "success",
        "message": "API is running."
    }
""",

    f"{PROJECT_NAME}/11_FastAPI_Docker/main.py": """from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def home():

    return {
        "message": "FastAPI application running inside Docker."
    }
""",

    f"{PROJECT_NAME}/11_FastAPI_Docker/Dockerfile": """FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
""",

    f"{PROJECT_NAME}/11_FastAPI_Docker/.dockerignore": """__pycache__
*.pyc
.venv
venv
.env
.git
.ipynb_checkpoints
""",

    f"{PROJECT_NAME}/11_FastAPI_Docker/docker-compose.yml": """services:

  fastapi:
    build: .
    ports:
      - "8000:8000"
    restart: unless-stopped
""",

    f"{PROJECT_NAME}/10_Docker_for_Machine_Learning/Dockerfile": """FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "--version"]
""",

    f"{PROJECT_NAME}/10_Docker_for_Machine_Learning/.dockerignore":
        """__pycache__
*.pyc
.venv
venv
.env
.git
""",
}


# ============================================================
# Create Folders
# ============================================================

print("\nCreating FastAPI repository structure...\n")

for folder in folders:
    Path(folder).mkdir(parents=True, exist_ok=True)
    print(f"[FOLDER] {folder}")


# ============================================================
# Create Files
# ============================================================

for file in files:

    file_path = Path(file)

    # Make sure parent directory exists
    file_path.parent.mkdir(parents=True, exist_ok=True)

    # Get predefined content or use empty content
    content = file_contents.get(file, "")

    # Do not overwrite an existing file
    if file_path.exists():
        print(f"[SKIP]   {file}")
        continue

    file_path.write_text(
        content,
        encoding="utf-8"
    )

    print(f"[FILE]   {file}")


# ============================================================
# Completion Message
# ============================================================

print("\n" + "=" * 60)
print("FastAPI repository structure created successfully!")
print("=" * 60)

print(f"\nProject location:")
print(Path(PROJECT_NAME).resolve())

print("\nNext steps:")
print("1. Open the project in VS Code.")
print("2. Create/activate your Python environment.")
print("3. Install dependencies:")
print("   pip install -r requirements.txt")
print("4. Start learning from:")
print("   01_Introduction_to_APIs")
print()