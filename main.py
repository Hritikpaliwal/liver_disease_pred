#importing libraries
from fastapi import FastAPI
from pydantic import BaseModel
from joblib import load

# Load the trained model using joblib
model = load('model1.joblib')


# Load the pre-trained model using pickle
#with open('model.pkl', 'rb') as f:
# old model with different version of sklearn lib which was giving error
    #model = pickle.load(f)


# Define FastAPI app
app = FastAPI()

# Define input data schema
class InputData(BaseModel):
    Age_of_the_patient: float
    Gender_of_the_patient: str
    Total_Bilirubin: float
    Direct_Bilirubin: float
    Alkaline_Phosphatase: float
    Alanine_Aminotransferase: float
    Aspartate_Aminotransferase: float
    Total_Proteins: float
    Albumin: float
    Albumin_and_Globulin_Ratio: float


# Endpoint for model prediction
@app.post("/predict")
async def predict(data: InputData):
    # Convert input data to dictionary
    input_data = data.dict()
    
    # Extract features for prediction
    features = [
        input_data['Age_of_the_patient'],
        input_data['Total_Bilirubin'],
        input_data['Direct_Bilirubin'],
        input_data['Alkaline_Phosphatase'],
        input_data['Alanine_Aminotransferase'],
        input_data['Aspartate_Aminotransferase'],
        input_data['Total_Proteins'],
        input_data['Albumin'],
        input_data['Albumin_and_Globulin_Ratio']
    ]
    
    # Make prediction
    prediction = model.predict([features])[0]
    
    # Return prediction result
    return {"prediction": prediction}

