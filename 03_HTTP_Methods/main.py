# =========================================================================
# Create a FastAPI application for Doctor and Patients with CRUD operations 
# Purpose: Retrieve the Patient's information from the Json file and Perform only GET Operation 
# =========================================================================


# ============================================================
# 1. Import libraries
# ============================================================
from fastapi import FastAPI
import uvicorn
import json

# ============================================================
# 2. Initialize the FastAPI
# ============================================================

app = FastAPI()

# Create a function to load the Patient Data from patient.json file
def load_data():
    file_path = "data/patients.json"
    try:
        with open(file_path, "r") as f:
            data = json.load(f)

        return data

    except FileNotFoundError:
        raise FileNotFoundError("patient.json file not found.")

    except json.JSONDecodeError:
        raise ValueError("patient.json contains invalid JSON.")


# ============================================================
# 3. CRATE Default/Home Route
# ============================================================
@app.get("/")
def Welcome():
    return {
        "message": "Patient Management System API"
    }

# ============================================================
# 5. CRATE about Route
# ============================================================
@app.get("/about")
def Welcome():
    return {
        "message": "A Fully Functional API to Mange Your Patient Records"
    }


# ============================================================
# 6. CRATE view Route 
# Purpose: View the all patient records
# ============================================================
@app.get("/view")
def view():
    data = load_data()

    return data




@app.get("/view")
def Welcome():
    return {
        "message": "A Fully Functional API to Mange Your Patient Records"
    }



# ============================================================
# 4.Run the app
# ============================================================
if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host ="0.0.0.0",
        port = 8080,
        reload=True
    )