# RK360 Prior-Auth MVP - Built from Sillod for US Healthcare

Day 16: Clinical Note -> ICD-10 -> FHIR Claim -> X12 278
Tech: FastAPI, FHIR R4, X12 278
Features: /prior-auth API that converts clinical note to FHIR Claim and X12 prior-auth request

Next: HITL Queue + Denial Prediction
Goal: Internship at RK360

## How to Run
pip install fastapi uvicorn
python app.py

## API Endpoint
POST /prior-auth
Body: { "clinical_note": "Patient needs MRI for back pain" }
