from fastapi import FastAPI
from schemas import User


app = FastAPI()


@app.post("/users")
def create_user(user: User):

    return {
        "message": "User created successfully",
        "user": user
    }
