from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"msg": "RK360 MVP Ready - Sillod se US tak"}

@app.get("/health")
def health():
    return {"status": "Motor ON hai", "farmer": "Gorak", "ready": True}

@app.post("/prior-auth")
def prior_auth(clinical_note: str):
    icd = "I63.9"
    fhir_claim = {
        "resourceType": "Claim",
        "status": "active",
        "use": "preauthorization",
        "patient": "Patient/123",
        "diagnosis": icd
    }
    x12 = f"ST*278*0001~HI*ABK:{icd}~"
    return {
        "extracted_icd": icd,
        "fhir_claim": fhir_claim,
        "x12_278": x12,
        "message": "MVP DONE"
    }