# Purpose: User input validation
from pydantic import BaseModel, Field, computed_field, field_validator
from typing import Literal, Annotated
from src.config.city_tier import tier_1_cities, tier_2_cities

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
