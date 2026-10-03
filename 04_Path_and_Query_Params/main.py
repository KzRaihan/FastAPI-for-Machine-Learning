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
from fastapi import FastAPI, Path, HTTPException, Query
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


# ================================================================================
# 6. Create a patient Route -> Retrieve Specific records by provided patient_id
# ================================================================================
@app.get("/patient/{patient_id}")
def view_patient(patient_id: str = Path(..., description="ID of the Patient in the DB", example="P001")):
    # load the all data
    data = load_data()

    # find the specific data based on patient_id
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail="Patient not Found")



# ================================================================================
# 7. Create a sort Route -> Retrieve and sort Specific records 
# sort_by = required Parameter
# order = optional parameter
# ================================================================================
@app.get("/sort")
def sort_patients(sort_by: str = Query(..., description="Sort on the basis of height, weight, bmi"), order: str=Query('asc', description="sort in asc or desc order")):

    valid_fields = ["height", "weight", "bmi"]

    # we first handle the error or invalid portion
    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f"Invalid field select from {valid_fields}")

    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail="Invalid order select between asc and desc")

    # Now perform the valid portion

    # load the data
    data = load_data()

    # define the sort order
    sorted_order = True if order=="desc" else False

    sorted_data = sorted(data.values(), key=lambda x:x.get(sort_by, 0), reverse=sorted_order)

    # return the sorted data
    return sorted_data
        


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



