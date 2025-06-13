from fastapi import FastAPI
import joblib
from pydantic import BaseModel


# creating app
app = FastAPI()


# loading the model
model = joblib.load("models/vpn_rf_model.pkl")

# loading the encoders
countryEncoder = joblib.load("models/countryLabels.pkl")
ispEncoder = joblib.load("models/ispLabels.pkl")

class IPRequest(BaseModel):
    country: str
    isp: str
    is_proxy: bool
    is_hosting: bool


# testing the endpoint
@app.get("/ping")
def ping():
    return {"status": "alive"}


@app.post("/predict")
def predict(data: IPRequest):
    try:
        # Encode inputs  using loaded LabelEncoders
        try:
            countryEncoded = countryEncoder.transform([data.country])[0]
        except ValueError:
            return {"error": f"Encoding error: country contains unseen label '{data.country}'"}

        try:
            ispEncoded = ispEncoder.transform([data.isp])[0]
        except ValueError:
            return {"error": f"Encoding error: isp contains unseen label '{data.isp}'"}

        # Create input array
        input_data = [[countryEncoded, ispEncoded, data.is_proxy, data.is_hosting]]

        # Predict
        prediction = model.predict(input_data)[0]
        label = "Suspicious" if prediction == 1 else "Safe"

        return {"prediction": int(prediction), "label": label}
    
    except ValueError as e:
        # This happens if transform() encounters unknown label
        return {"error": f"Encoding error: {str(e)}"}

    except Exception as e:
        return {"error": str(e)}
