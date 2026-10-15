# Import necessary libraries
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import uvicorn
from pydantic import BaseModel, Field, computed_field
from typing import Literal, Annotated
import pickle
import pandas as pd

# 1. import the Trained ml model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# 2. Create an FastAPI object
app = FastAPI()


# (4.4 - 4.5): Define the city tier
tier_1_cities = ["Mumbai", "Delhi", "Bangalore", "Chennai", "Kolkata", "Hyderabad", "Pune"]
tier_2_cities = [
    "Jaipur", "Chandigarh", "Indore", "Lucknow", "Patna", "Ranchi", "Visakhapatnam", "Coimbatore",
    "Bhopal", "Nagpur", "Vadodara", "Surat", "Rajkot", "Jodhpur", "Raipur", "Amritsar", "Varanasi",
    "Agra", "Dehradun", "Mysore", "Jabalpur", "Guwahati", "Thiruvananthapuram", "Ludhiana", "Nashik",
    "Allahabad", "Udaipur", "Aurangabad", "Hubli", "Belgaum", "Salem", "Vijayawada", "Tiruchirappalli",
    "Bhavnagar", "Gwalior", "Dhanbad", "Bareilly", "Aligarh", "Gaya", "Kozhikode", "Warangal",
    "Kolhapur", "Bilaspur", "Jalandhar", "Noida", "Guntur", "Asansol", "Siliguri"
]

# 3. Create Pydantic model for validated incoming data
class UserInput(BaseModel):
    age: Annotated[int, Field(..., gt=0, le=120, description="Age of the user")]

    weight: Annotated[float, Field(..., ge=0, description="Weight of the user in kg")]

    height: Annotated[float, Field(..., ge=0, le=2.5, description="Height of the user in meters")]

    income_lpa: Annotated[float, Field(..., ge=0,  description="Annual salary of the user in lpa")]

    smoker: Annotated[bool, Field(..., description="Is user a smoker")]

    city: Annotated[str, Field(..., description="City name the user is belong to")]

    occupation: Annotated[Literal['retired','freelancer','student','government_job','business_owner','unemployed','private_job'], Field(..., description="Occupation of the user")]


    # 4. Create new feature that our model want

    # 4.1 bmi: First computed field
    @computed_field
    @property
    def bmi(self) -> float:
        bmi = self.weight/(self.height**2)

        return bmi

    # 4.2 age_group: second computed field
    @computed_field
    @property
    def age_group(self) -> str:
        if self.age < 25:
            return "young"
        elif self.age < 45:
            return "adult"
        elif self.age < 60:
            return "middle_aged"
        return "senior"

    # 4.3 lifestyle_risk: Third computed field
    @computed_field
    @property
    def lifestyle_risk(self) -> str:
        if self.smoker and self.bmi > 30:
            return "high"
        elif self.smoker or self.bmi > 27:
            return "medium"
        else:
            return "low"

    # 4.4 city_tier: Four computed field
    @computed_field
    @property
    def city_tier(self) -> int:
        if self.city in tier_1_cities:
            return 1
        elif self.city in tier_2_cities:
            return 2
        else:
            return 3


# ============================================================
# Home Route
# ============================================================

@app.get("/")
def home():
     return {
        "message": "Welcome to the ML Serving ML Model with FastAPI"
    }



# 5. Create a predict Route 
@app.post('/predict')
def predict_premium(data: UserInput):

    # 5.1 Convert thee user data structure into  model want format with Dataframe. 
    input_df = pd.DataFrame([{
        "bmi": data.bmi,
        "age_group": data.age_group,
        "lifestyle_risk": data.lifestyle_risk,
        "city_tier": data.city_tier,
        "income_lpa": data.income_lpa,
        "occupation": data.occupation
    }])

    # 5.2: Predict the user data
    prediction = model.predict(input_df)[0]

    return JSONResponse(status_code=200, content={"predicted_category": prediction}) 

# ============================================================
# 6. Run the FastAPI Application
# ============================================================

if __name__ == "__main__":

    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8080,
        reload=True
    )