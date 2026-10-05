# ========================================================================= 
# FastAPI Application: Doctor and Patient Management 

# Purpose: 
# - Retrieve patient information from patients.json 
# - Perform GET operations 
# - Perform POST operation 
# - Validate incoming patient data using Pydantic 
# - Store new patient records in patients.json 

#  Workflow for POST Request: 
#   - Step 1: Client sends a POST request 
#   - Step 2: FastAPI receives the request body 
#   - Step 3: Pydantic validates the request data 
#   - Step 4: Check whether the patient already exists 
#   - Step 5: Add the new patient to patients.json 
#   - Step 6: Return a success response 
# =========================================================================


# ============================================================
# 1. Import libraries
# ============================================================
from fastapi import FastAPI, Path, HTTPException, Query
from fastapi.responses import JSONResponse
import uvicorn
import json
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal


# ============================================================
# 1. Initialize the FastAPI
# ============================================================
app = FastAPI()


# ------------------------------------------------------------------------
# Method 1: load_data
# Purpose: Load the patient all records from the json file
# ------------------------------------------------------------------------
def load_data():
    """ Load All Patient Records from Json file """
    file_path = "../data/patients.json"

    try:
        # open the file
        with open(file_path, "r") as f:
            data = json.load(f)

        return data
    
    except FileNotFoundError:
        raise FileNotFoundError("patient.json file not found.")

    except json.JSONDecodeError:
        raise ValueError("patient.json contains invalid JSON.")

# -----------------------------------------------------
# Method 2: save_data
# Purpose: Save the json file 
# -----------------------------------------------------
def save_data(data):
    """ Save Patient Records to Json file """
    file_path = "../data/patients.json"
    with open(file_path, "w") as f:
        json.dump(data, f)



# ============================================================ 
#  1. Pydantic Model: Patient
#  Purpose:  Validate incoming patient data for POST requests. 
#  Fields stored in the JSON file: 
    # - id 
    # - name 
    # - city  
    # - age 
    # - gender 
    # - height 
    # - weight 
    # - Dynamic fields:  
    # - bmi 
    # - verdict 
# - bmi and verdict are calculated automatically.  ============================================================

class Patient(BaseModel):
    id: Annotated[str, Field(..., description="ID of the Patient", examples=["P001"])]
    name: Annotated[str, Field(...,description="Name of the Patient")]
    city: Annotated[str, Field(..., description="City Name Where the Patient is Living")]
    age: Annotated[int, Field(...,gt=0, lt=110 ,description="Age of the Patient")]
    gender: Annotated[Literal['male', 'female', 'other'], Field(..., description="Gender of the Patient")]
    height: Annotated[float, Field(..., gt=0, description= "Height of the Patient in Meters")]
    weight: Annotated[float, Field(..., ge=0, description="Weight of the Patient in Kgs")]


    # ======================================================== 
    # Dynamic Field 1: bmi
    # BMI = weight / height² 
    # @computed_field tells Pydantic that this calculated 
    # property should also be included when the model is serialized. 
    # ========================================================
    @computed_field
    @property
    def bmi(self)-> float:
        bmi = self.weight / (self.height ** 2)

        return round(bmi, 2)

    # 2. Create second Dynamic Field: verdict
    @computed_field
    @property
    def verdict(self) -> str:
        if self.bmi < 18.5:
            return "Underweight"
        elif self.bmi < 25:
            return "Normal"
        elif self.bmi < 30:
            return "Overweight"
        else:
            return "Obese"

# ============================================================ 
# 2. Home Route 
#   Method: GET 
#   Endpoint: / 
#   Purpose: Check whether the API is running.
# ============================================================
@app.get("/")
def Home():
    return {
        "Message": "Welcome to the Post Operation Module"
    }


# ============================================================================
# 3. Create a views Route -> Retrieve or vies all data from the json file
#  - Create Method 1: load_data
# ============================================================================
# ============================================================ 
# 3. View All Patients 
# Method: GET 
# Endpoint: /views 
# Purpose: 
#   - Retrieve all patient records from patients.json
# ============================================================

@app.get("/views")
def views():
    data = load_data()

    return data


# ============================================================
# 5. Create a views Route -> create 
#  - Create an new records to the json file
#  - For doing the validation use -> class 1: Patient
# ============================================================
@app.post("/create")
def create_patient(patient: Patient):
    
    # -------------------------------------------------------- 
    # Step 1: Load existing patient records 
    # --------------------------------------------------------
    data = load_data()

    # 2. Check the data is already exists or not
    if patient.id in data:
        raise HTTPException(status_code=400, detail="Patient already exists")

    # 3. Only New Patient add to the existing json file
    # here, data is the python dictionary but our file contain the json data, therefore first convert the new data(pydantic object) into json file format then add.

    # 3.1: Convert new data (pydantic object) to dictionary
    data[patient.id] = patient.model_dump(exclude=['id'])

    # 3.2: save the new data (dict) to the json file
    # Method 2: save_data
    save_data(data)

    # -------------------------------------------------------- 
    # Step 6: Return success response 
    # -------------------------------------------------------- 
    return JSONResponse( 
        status_code=201, 
        content={ "message": "Patient created successfully.", "patient_id": patient.id } )




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




