from fastapi import FastAPI


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
