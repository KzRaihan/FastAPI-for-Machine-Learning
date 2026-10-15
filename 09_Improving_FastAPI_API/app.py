from fastapi import FastAPI
from fastapi.responses import JSONResponse
import uvicorn

from src.config.paths import MODEL_VERSION
from schema.user_input_validation import UserInput
from model.predict import model, predict_output
from schema.prediction_response import PredictionResponse

# ============================================================
# Create an FastAPI object
# ============================================================
app = FastAPI()


# ============================================================
# Home Route
# ============================================================

@app.get("/")
def home():
     return {
        "message": "Insurance Premium Prediction API"
    }



# ============================================================
# health Route that is machine readable
# ============================================================
@app.get('/health')
def health_check():
    return {
        'status': 'OK',
        'version': MODEL_VERSION,
        'model_loaded': model is not None
    }



# ============================================================
#  predict_premium Route
# ============================================================
@app.post('/predict', response_model=PredictionResponse)
def predict_premium(data: UserInput):

    user_input = {
        'bmi': data.bmi,
        'age_group': data.age_group,
        'lifestyle_risk': data.lifestyle_risk,
        'city_tier': data.city_tier,
        'income_lpa': data.income_lpa,
        'occupation': data.occupation
    }

    try:
        prediction = predict_output(user_input)

        return JSONResponse(status_code=200, content={'response': prediction})
    
    except Exception as e:

        return JSONResponse(status_code=500, content=str(e))

# ============================================================
# 6. Run the FastAPI Application
# ============================================================

if __name__ == "__app__":

    uvicorn.run(
        "app:app",
        host="0.0.0.0",
        port=8080,
        reload=True
    )