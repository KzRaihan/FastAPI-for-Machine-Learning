# ============================================================
# 1. Import libraries
# ============================================================

from fastapi import FastAPI
import uvicorn


# ============================================================
# 2. Create the FastAPI application object
# ============================================================

app = FastAPI()


# ============================================================
# 3. Define Routes
# ============================================================

# Default/Home Route
@app.get("/")
def welcome():
    return {
        "message": "WELCOME To the Fast API"
    }

# about route (# Now app is running on: http://127.0.0.1:8000/about)
@app.get("/about")
def about():
    return{
        "message": "My Name is Md Kamruzzaman Raihan"
    }

# ============================================================
# 4. Run the application
# ============================================================

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )