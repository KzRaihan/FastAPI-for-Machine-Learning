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
from typing import Annotated, Literal, Optional


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
#  2. Pydantic Model: Patient
# ============================================================ 
class PatientUpdate(BaseModel):

    name: Annotated[
        Optional[str],
        Field(default=None)
    ]

    city: Annotated[
        Optional[str],
        Field(default=None)
    ]

    age: Annotated[
        Optional[int],
        Field(default=None, gt=0)
    ]

    gender: Annotated[
        Optional[Literal["male", "female", "other"]],
        Field(default=None)
    ]

    height: Annotated[
        Optional[float],
        Field(default=None, gt=0)
    ]

    weight: Annotated[
        Optional[float],
        Field(default=None, gt=0)
    ]



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
# 6. Update Patient Route
#
# Method: PUT
# Endpoint: /edit/{patient_id}
#
# Purpose:
# Update an existing patient's information.
#
# Workflow:
#
# Client
#   ↓
# PUT /edit/{patient_id}
#   ↓
# Validate patient_id
#   ↓
# Load existing patient data
#   ↓
# Validate updated fields using PatientUpdate
#   ↓
# Update existing information
#   ↓
# Recalculate BMI and Verdict
#   ↓
# Save updated data
#   ↓
# Return success response
# ============================================================

@app.put("/edit/{patient_id}")
def update_patient(
    patient_id: str,
    patient_update: PatientUpdate
):
    
    # --------------------------------------------------------
    # Step 1: Load all existing patient records
    # --------------------------------------------------------

    data = load_data()

    # --------------------------------------------------------
    # Step 2: Check whether the patient exists
    #
    # If the patient ID does not exist, return HTTP 404.
    # --------------------------------------------------------

    if patient_id not in data:

        raise HTTPException(
            status_code=404,
            detail="Patient not found."
        )

    # --------------------------------------------------------
    # Step 3: Get the existing patient's information
    #
    # patient_id is a variable, so we use:
    #
    #     data[patient_id]
    #
    # NOT:
    #
    #     data["patient_id"]
    # --------------------------------------------------------

    existing_patient_info = data[patient_id]

    # --------------------------------------------------------
    # Step 4: Convert the Pydantic update object into a
    # dictionary.
    #
    # exclude_unset=True means:
    # Only fields explicitly provided by the client
    # will be included.
    #
    # Example:
    #
    # {
    #     "weight": 70
    # }
    #
    # Only weight will be updated.
    # --------------------------------------------------------

    updated_patient_info = patient_update.model_dump(
        exclude_unset=True
    )

    # --------------------------------------------------------
    # Step 5: Update the existing patient information
    #
    # Loop through the fields provided by the client and
    # replace the corresponding existing values.
    # --------------------------------------------------------

    for key, value in updated_patient_info.items():

        existing_patient_info[key] = value

    # --------------------------------------------------------
    # Step 6: Add the patient ID temporarily
    #
    # We need the ID to recreate the complete Patient model.
    # The Patient model will validate the updated information
    # and automatically calculate:
    #
    #   - BMI
    #   - Verdict
    # --------------------------------------------------------

    existing_patient_info["id"] = patient_id

    # --------------------------------------------------------
    # Step 7: Re-create the Patient Pydantic object
    #
    # This is important because the updated height/weight
    # may change the BMI and verdict.
    #
    # Pydantic will also validate the complete patient data.
    # --------------------------------------------------------

    patient_pydantic_obj = Patient(
        **existing_patient_info
    )

    # --------------------------------------------------------
    # Step 8: Convert the validated Patient object back
    # into a dictionary.
    #
    # exclude={"id"} removes the ID because the ID is already
    # being used as the dictionary key in our JSON structure.
    #
    # The computed fields BMI and verdict are included.
    # --------------------------------------------------------

    updated_patient_data = patient_pydantic_obj.model_dump(
        exclude={"id"}
    )

    # --------------------------------------------------------
    # Step 9: Replace the old patient record with the
    # newly validated and updated patient data.
    # --------------------------------------------------------

    data[patient_id] = updated_patient_data

    # --------------------------------------------------------
    # Step 10: Save the updated patient records to JSON.
    # --------------------------------------------------------

    save_data(data)

    # --------------------------------------------------------
    # Step 11: Return a successful response.
    # --------------------------------------------------------

    return JSONResponse(
        status_code=200,
        content={
            "message": "Patient updated successfully.",
            "patient_id": patient_id
        }
    )





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




