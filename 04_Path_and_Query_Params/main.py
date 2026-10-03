# =========================================================================
# Create a FastAPI application for Doctor and Patients with CRUD operations 
# Purpose: Retrieve the Patient's information from the Json file and Perform only GET Operation 

# Use:
# Path ->  identify a specific resource (data)
# Query Params -> REFINEMENT of the resource (data)
# =========================================================================


# ============================================================
# 1. Import libraries
# ============================================================
from fastapi import FastAPI
import uvicorn
import json


# ------------------------------------------------------------------------
# Method 1: load_data
# Purpose: Load the patient all records from the json file
# ------------------------------------------------------------------------
def load_data():
    """ Load All Patient Records """
    # data path
    file_path = "../data/patients.json"
    try:
        with open(file_path, "r") as f:
            data = json.load(f)

            return data
    except FileNotFoundError:
        raise FileNotFoundError("patient.json file not found.")

    except json.JSONDecodeError:
        raise ValueError("patient.json contains invalid JSON.")


# ============================================================
# 2. Initialize the FastAPI
# ============================================================
app = FastAPI()


# ============================================================
# 3. Create a Default/Home Route
# ============================================================
@app.get("/")
def Home():
    return {
        "message": "Welcome to the Path and Query Params Lecture"
    }


# ============================================================
# 5. Create a views Route -> Retrieve all data
# ============================================================
@app.get("/views")
def views():
    data = load_data()

    return data


# ============================================================
# 6. Create a patient Route -> Retrieve Specific records
# ============================================================
@app.get("/patient/{patient_id}")
def view_patient(patient_id: str):
    # load the all data
    data = load_data()

    # find the specific data based on patient_id
    if patient_id in data:
        return data[patient_id]

    return {
        "error": "Patient not found"
    }



# ============================================================
# 4.Run the main/app Route
# ============================================================

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8080,
        reload=True    

    )



