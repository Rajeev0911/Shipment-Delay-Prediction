from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Shipment(BaseModel):
    shipment_id: str
    origin: str
    destination: str
    booking_date: str
    scheduled_date: str
    actual_date: str
    vehicle_type: str
    distance: int
    weather: str
    traffic: str

@app.get("/")
def home():
    return {"message": "Welcome to Shipment Prediction API"}

@app.post("/predict")
def predict(shipment: Shipment):
    # Simple prediction logic based on weather and traffic
    is_delayed = (
        shipment.weather != "Clear" 
        or shipment.traffic == "Heavy" 
        or shipment.distance > 1000
    )
    
    return {
        "prediction": "Delayed" if is_delayed else "On Time",
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)