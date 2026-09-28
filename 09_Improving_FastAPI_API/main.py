from fastapi import FastAPI


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
