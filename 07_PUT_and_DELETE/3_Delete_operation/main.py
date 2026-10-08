# ============================================================
# FastAPI - HTTP Methods
# Patient CRUD API
# ============================================================

# -----------------------------
# 1. Import Required Libraries
# -----------------------------

from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse

import uvicorn
import json

from pathlib import Path
from typing import Annotated, Literal, Optional

from pydantic import BaseModel, Field, computed_field


# ============================================================
# 2. Create FastAPI Application
# ============================================================

app = FastAPI(
    title="Patient Management API",
    description="A simple FastAPI application for managing patient data.",
    version="1.0.0"
)


# ============================================================
# 3. Define the Data File Path
# ============================================================

DATA_FILE = "../data/patients.json"

# ============================================================
# 4. Load Patient Data
# ============================================================

def load_data():
    """
    Load patient data from the JSON file.

    Returns:
        dict: Patient data stored in patients.json
    """

    try:
        with open(DATA_FILE, "r") as file:
            data = json.load(file)

        return data

    except FileNotFoundError:
        raise FileNotFoundError(
            f"Patient data file not found: {DATA_FILE}"
        )

    except json.JSONDecodeError:
        raise ValueError(
            "patients.json contains invalid JSON."
        )


# ============================================================
# 5. Save Patient Data
# ============================================================

def save_data(data):
    """
    Save patient data to the JSON file.

    Args:
        data (dict): Patient data that needs to be saved.
    """

    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)


# ============================================================
# 6. Patient Pydantic Model
# ============================================================

class Patient(BaseModel):

    # Unique patient ID
    id: Annotated[
        str,
        Field(
            ...,
            description="ID of the patient",
            examples=["P001"]
        )
    ]

    # Patient name
    name: Annotated[
        str,
        Field(
            ...,
            description="Name of the patient"
        )
    ]

    # City where the patient lives
    city: Annotated[
        str,
        Field(
            ...,
            description="City where the patient is living"
        )
    ]

    # Patient age
    age: Annotated[
        int,
        Field(
            ...,
            gt=0,
            lt=110,
            description="Age of the patient"
        )
    ]

    # Gender must be one of these three values
    gender: Annotated[
        Literal["male", "female", "other"],
        Field(
            ...,
            description="Gender of the patient"
        )
    ]

    # Height is stored in meters
    height: Annotated[
        float,
        Field(
            ...,
            gt=0,
            description="Height of the patient in meters"
        )
    ]

    # Weight is stored in kilograms
    weight: Annotated[
        float,
        Field(
            ...,
            gt=0,
            description="Weight of the patient in kilograms"
        )
    ]

    # --------------------------------------------------------
    # Computed Field: BMI
    # --------------------------------------------------------

    @computed_field
    @property
    def bmi(self) -> float:
        """
        Calculate BMI from weight and height.

        Formula:
            BMI = weight / height²
        """

        bmi = self.weight / (self.height ** 2)

        return round(bmi, 2)

    # --------------------------------------------------------
    # Computed Field: BMI Verdict
    # --------------------------------------------------------

    @computed_field
    @property
    def verdict(self) -> str:
        """
        Return a simple BMI category based on BMI value.
        """

        if self.bmi < 18.5:
            return "Underweight"

        elif self.bmi < 25:
            return "Normal"

        elif self.bmi < 30:
            return "Overweight"

        else:
            return "Obese"


# ============================================================
# 7. PatientUpdate Pydantic Model
# ============================================================

class PatientUpdate(BaseModel):

    # All fields are optional because this model is used
    # for updating an existing patient partially.

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
        Field(
            default=None,
            gt=0
        )
    ]

    gender: Annotated[
        Optional[Literal["male", "female", "other"]],
        Field(default=None)
    ]

    height: Annotated[
        Optional[float],
        Field(
            default=None,
            gt=0
        )
    ]

    # Use float here because Patient.weight is also float
    weight: Annotated[
        Optional[float],
        Field(
            default=None,
            gt=0
        )
    ]


# ============================================================
# 8. Home Route
# ============================================================

@app.get("/")
def home():
    """
    Welcome endpoint.
    """

    return {
        "message": "Welcome to the Patient Management API"
    }


# ============================================================
# 9. GET - View All Patients
# ============================================================

@app.get("/views")
def views():
    """
    Return all patients.
    """

    data = load_data()

    return data


# ============================================================
# 10. POST - Create a New Patient
# ============================================================

@app.post("/create")
def create_patient(patient: Patient):
    """
    Create a new patient.

    The patient ID must be unique.
    """

    # Load existing patient data
    data = load_data()

    # Check whether the patient ID already exists
    if patient.id in data:
        raise HTTPException(
            status_code=400,
            detail="Patient already exists."
        )

    # Convert Pydantic object into dictionary.
    #
    # We exclude "id" because the ID is already being used
    # as the dictionary key.
    data[patient.id] = patient.model_dump(
        exclude={"id"}
    )

    # Save updated data
    save_data(data)

    return JSONResponse(
        status_code=201,
        content={
            "message": "Patient created successfully.",
            "patient_id": patient.id
        }
    )


# ============================================================
# 11. PUT - Update an Existing Patient
# ============================================================

@app.put("/edit/{patient_id}")
def update_patient(
    patient_id: str,
    patient_update: PatientUpdate
):
    """
    Update an existing patient.

    Only the fields provided in the request body
    will be updated.
    """

    # --------------------------------------------------------
    # Step 1: Load existing patient data
    # --------------------------------------------------------

    data = load_data()

    # --------------------------------------------------------
    # Step 2: Check whether patient exists
    # --------------------------------------------------------

    if patient_id not in data:
        raise HTTPException(
            status_code=404,
            detail="Patient not found."
        )

    # --------------------------------------------------------
    # Step 3: Get existing patient information
    # --------------------------------------------------------

    # .copy() prevents us from directly modifying the
    # original dictionary before validation.
    existing_patient_info = data[patient_id].copy()

    # --------------------------------------------------------
    # Step 4: Get only fields sent by the user
    # --------------------------------------------------------

    # exclude_unset=True means:
    #
    # If the user sends:
    #
    # {
    #     "weight": 70
    # }
    #
    # Only "weight" will be included here.
    #
    # Fields such as name, city, age, etc. will not be
    # included unless the user actually sends them.

    updated_patient_info = patient_update.model_dump(
        exclude_unset=True
    )

    # --------------------------------------------------------
    # Step 5: Update existing fields
    # --------------------------------------------------------

    for key, value in updated_patient_info.items():
        existing_patient_info[key] = value

    # --------------------------------------------------------
    # Step 6: Add ID back for Pydantic validation
    # --------------------------------------------------------

    existing_patient_info["id"] = patient_id

    # --------------------------------------------------------
    # Step 7: Validate the complete patient object
    # --------------------------------------------------------

    patient_pydantic_obj = Patient(
        **existing_patient_info
    )

    # --------------------------------------------------------
    # Step 8: Convert validated patient back to dictionary
    # --------------------------------------------------------

    updated_patient_data = patient_pydantic_obj.model_dump(
        exclude={"id"}
    )

    # --------------------------------------------------------
    # Step 9: Save updated patient data
    # --------------------------------------------------------

    data[patient_id] = updated_patient_data

    save_data(data)

    # --------------------------------------------------------
    # Step 10: Return success response
    # --------------------------------------------------------

    return JSONResponse(
        status_code=200,
        content={
            "message": "Patient updated successfully.",
            "patient_id": patient_id
        }
    )


# ============================================================
# 12. DEl - Delete an Existing Patient
# ============================================================
@app.delete("/delete/{patient_id}")
def delete_patient(patient_id: str):
    # --------------------------------------------------------
    # Step 1: Load existing patient data
    # --------------------------------------------------------

    data = load_data()

    # --------------------------------------------------------
    # Step 2: Check whether patient exists
    # --------------------------------------------------------

    if patient_id not in data:
        raise HTTPException(
            status_code=404,
            detail="Patient not found."
        )

    # --------------------------------------------------------
    # Step 3: Delete the patient exists
    # --------------------------------------------------------
    del data[patient_id]

    # --------------------------------------------------------
    # Step 4: Save updated patient data
    # --------------------------------------------------------

    save_data(data)

    # --------------------------------------------------------
    # Step 10: Return success response
    # --------------------------------------------------------

    return JSONResponse(
        status_code=200,
        content={
            "message": "Patient Delete successfully.",
            "patient_id": patient_id
        }
    )


# ============================================================
# 13. Run the FastAPI Application
# ============================================================

if __name__ == "__main__":

    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8080,
        reload=True
    )