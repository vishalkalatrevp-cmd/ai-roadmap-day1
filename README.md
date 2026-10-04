# RK360 Prior-Auth MVP - Built from Sillod for US Healthcare 🇮🇳 → 🇺🇸

**Day 16/90: Clinical Note → ICD-10 → FHIR R4 Claim → X12 278**

I built an end-to-end Prior Authorization automation system that converts clinical notes into FHIR Claims and X12 278 requests.

### 🚀 Live Features
- **POST /prior-auth** - Converts free-text clinical note to structured FHIR R4 Claim
- Auto-generates X12 278 Prior-Auth transaction
- Built with FastAPI, FHIR R4, X12 278

### 🛠️ Tech Stack
- **Backend:** FastAPI (Python)
- **Healthcare Standards:** FHIR R4, ICD-10, X12 278
- **Deployment:** 【entity-GitHub¦canonical_name=GitHub】

### 📈 Roadmap
- **Day 17-20:** HITL (Human-In-The-Loop) Queue + Denial Prediction Model
- **Day 21-30:** Full Payer Integration & Dashboard

### 👨‍💻 About Me
Building from Sillod, Maharashtra for US Healthcare. Goal: Direct SDE role at RK360 / Healthcare IT startups.

### How to Run
pip install fastapi uvicorn
uvicorn app:app --reload

API Endpoint: POST /prior-auth
Body: { "clinical_note": "Patient needs MRI for back pain" }
