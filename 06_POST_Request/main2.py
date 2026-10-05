# =========================================================================
# FastAPI Application: Doctor and Patient Management
#
# Purpose:
# - Retrieve patient information from patients.json
# - Perform GET operations
# - Perform POST operation
# - Validate incoming patient data using Pydantic
# - Store new patient records in patients.json
#
# Workflow for POST Request:
#   Step 1: Client sends a POST request
#   Step 2: FastAPI receives the request body
#   Step 3: Pydantic validates the request data
#   Step 4: Check whether the patient already exists
#   Step 5: Add the new patient to patients.json
#   Step 6: Return a success response
# =========================================================================


# ============================================================
# 1. Import Required Libraries
# ============================================================

from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse

import uvicorn
import json

from pathlib import Path
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal


# ============================================================
# 2. Initialize the FastAPI Application
# ============================================================

app = FastAPI()


# ============================================================
# 3. Define the JSON File Path
# ============================================================

# __file__ -> current Python file (main.py)
# .resolve() -> converts it into an absolute path
# .parent -> gets the directory containing main.py
#
# Project structure:
#
# 03_HTTP_Methods/
# ├── main.py
# └── data/
#     └── patients.json

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "data" / "patients.json"


# ============================================================
# 4. Method: load_data()
# Purpose:
# Load all patient records from patients.json
# ============================================================

def load_data():
    """Load all patient records from the JSON file."""

    try:
        # Open the JSON file in read mode
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)

        return data

    except FileNotFoundError:
        raise FileNotFoundError(
            "patients.json file not found."
        )

    except json.JSONDecodeError:
        raise ValueError(
            "patients.json contains invalid JSON."
        )


# ============================================================
# 5. Method: save_data()
# Purpose:
# Save patient records into patients.json
# ============================================================

def save_data(data):
    """Save patient records to the JSON file."""

    # Open the JSON file in write mode
    with open(DATA_FILE, "w", encoding="utf-8") as f:

        # Convert Python dictionary into JSON
        # indent=4 makes the JSON file easier to read
        json.dump(data, f, indent=4)


# ============================================================
# 6. Pydantic Model: Patient
#
# Purpose:
# Validate incoming patient data for POST requests.
#
# Fields stored in the JSON file:
# - id
# - name
# - city
# - age
# - gender
# - height
# - weight
#
# Dynamic fields:
# - bmi
# - verdict
#
# bmi and verdict are calculated automatically.
# ============================================================

class Patient(BaseModel):

    # --------------------------------------------------------
    # Patient ID
    # --------------------------------------------------------

    id: Annotated[
        str,
        Field(
            ...,
            description="ID of the patient",
            examples=["P001"]
        )
    ]

    # --------------------------------------------------------
    # Patient Name
    # --------------------------------------------------------

    name: Annotated[
        str,
        Field(
            ...,
            description="Name of the patient"
        )
    ]

    # --------------------------------------------------------
    # Patient City
    # --------------------------------------------------------

    city: Annotated[
        str,
        Field(
            ...,
            description="City where the patient lives"
        )
    ]

    # --------------------------------------------------------
    # Patient Age
    # --------------------------------------------------------

    age: Annotated[
        int,
        Field(
            ...,
            gt=0,
            lt=110,
            description="Age of the patient"
        )
    ]

    # --------------------------------------------------------
    # Patient Gender
    #
    # Literal restricts the value to:
    # male, female, or other
    # --------------------------------------------------------

    gender: Annotated[
        Literal["male", "female", "other"],
        Field(
            ...,
            description="Gender of the patient"
        )
    ]

    # --------------------------------------------------------
    # Patient Height
    #
    # Height is measured in meters.
    # Example: 1.75
    # --------------------------------------------------------

    height: Annotated[
        float,
        Field(
            ...,
            gt=0,
            description="Height of the patient in meters"
        )
    ]

    # --------------------------------------------------------
    # Patient Weight
    #
    # Weight is measured in kilograms.
    # --------------------------------------------------------

    weight: Annotated[
        float,
        Field(
            ...,
            gt=0,
            description="Weight of the patient in kilograms"
        )
    ]

    # ========================================================
    # Dynamic Field 1: BMI
    #
    # BMI = weight / height²
    #
    # @computed_field tells Pydantic that this calculated
    # property should also be included when the model is
    # serialized.
    # ========================================================

    @computed_field
    @property
    def bmi(self) -> float:

        bmi = self.weight / (self.height ** 2)

        return round(bmi, 2)

    # ========================================================
    # Dynamic Field 2: Verdict
    #
    # BMI Classification:
    # < 18.5       -> Underweight
    # 18.5 - <25   -> Normal
    # 25 - <30     -> Overweight
    # >= 30        -> Obese
    # ========================================================

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
# 7. Home Route
#
# Method: GET
# Endpoint: /
# Purpose: Check whether the API is running.
# ============================================================

@app.get("/")
def home():

    return {
        "message": "Welcome to the Patient Management API"
    }


# ============================================================
# 8. View All Patients
#
# Method: GET
# Endpoint: /views
# Purpose:
# Retrieve all patient records from patients.json
# ============================================================

@app.get("/views")
def views():

    # Load all patient records
    data = load_data()

    return data


# ============================================================
# 9. Create New Patient
#
# Method: POST
# Endpoint: /create
#
# Workflow:
#
# Client
#   ↓
# POST /create
#   ↓
# Pydantic Validation
#   ↓
# Check Patient ID
#   ↓
# Add Patient
#   ↓
# Save patients.json
#   ↓
# Return Success Response
# ============================================================

@app.post("/create")
def create_patient(patient: Patient):

    # --------------------------------------------------------
    # Step 1: Load existing patient records
    # --------------------------------------------------------

    data = load_data()

    # --------------------------------------------------------
    # Step 2: Check whether the patient already exists
    #
    # Since patient IDs are used as dictionary keys,
    # we can check directly using:
    #
    #     if patient.id in data
    # --------------------------------------------------------

    if patient.id in data:

        raise HTTPException(
            status_code=400,
            detail="Patient already exists."
        )

    # --------------------------------------------------------
    # Step 3: Convert Pydantic object into a Python dictionary
    #
    # exclude={"id"} means:
    # Do not store the ID inside the patient information,
    # because the ID is already being used as the dictionary key.
    #
    # computed_field values (bmi and verdict) are also included.
    # --------------------------------------------------------

    patient_data = patient.model_dump(
        exclude={"id"}
    )

    # --------------------------------------------------------
    # Step 4: Add the new patient to the existing data
    # --------------------------------------------------------

    data[patient.id] = patient_data

    # --------------------------------------------------------
    # Step 5: Save the updated data back to patients.json
    # --------------------------------------------------------

    save_data(data)

    # --------------------------------------------------------
    # Step 6: Return success response
    # --------------------------------------------------------

    return JSONResponse(
        status_code=201,
        content={
            "message": "Patient created successfully.",
            "patient_id": patient.id
        }
    )


# ============================================================
# 10. Run the FastAPI Application
# ============================================================

if __name__ == "__main__":

    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8080,
        reload=True
    )

