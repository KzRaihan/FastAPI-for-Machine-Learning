from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def home():

    return {
        "message": "FastAPI application running inside Docker."
    }
