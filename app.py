from fastapi import FastAPI
from pydantic import BaseModel
import mlflow.pyfunc
import pandas as pd

# Initialize FastAPI app
app = FastAPI()

# Load best model from MLflow
mlflow_uri = "runs:/d0f7d16ce56d49d3868601fc9180321d/RandomForest"
model = mlflow.pyfunc.load_model(mlflow_uri)


# Define request schema
class ChurnRequest(BaseModel):
    Call_Failure: int
    Complains: int
    Subscription_Length: int
    Charge_Amount: int
    Seconds_of_Use: int
    Frequency_of_use: int
    Frequency_of_SMS: int
    Distinct_Called_Numbers: int
    Age_Group: int
    Tariff_Plan: int
    Status: int
    Age: int
    Customer_Value: float


# Define API endpoint
@app.get("/")
def root():
    return {"message": "Hello World"}


@app.post("/predict")
def predict_churn(request: ChurnRequest):
    # Convert request data to DataFrame
    print("=====REQUEST======", request)
    data = pd.DataFrame([request.model_dump()])

    # Make prediction
    prediction = model.predict(data)

    # Return result
    return {"churn_prediction": int(prediction[0])}


# To run, execute this in terminal:
# uvicorn app:app --host 0.0.0.0 --port 8000
