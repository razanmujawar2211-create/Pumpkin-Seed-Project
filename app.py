from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
import pickle
import numpy as np

app = FastAPI()

# load model
model = pickle.load(open("model.pkl", "rb"))

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/predict", response_class=HTMLResponse)
def predict(
    request: Request,
    Area: float = Form(...),
    Perimeter: float = Form(...),
    Major_Axis_Length: float = Form(...),
    Solidity: float = Form(...),
    Extent: float = Form(...),
    Roundness: float = Form(...),
    Aspect_Ration: float = Form(...),
    Compactness: float = Form(...),
):
    input_data = np.array([[
        Area, Perimeter, Major_Axis_Length,
        Solidity, Extent, Roundness,
        Aspect_Ration, Compactness
    ]])

    prediction = model.predict(input_data)[0]

    if prediction == 0:
        result = "Çerçevelik"
    else:
        result = "Ürgüp Sivrisi"

    return templates.TemplateResponse(
        "index.html",
        {"request": request, "prediction_text": result}
    )