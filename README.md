# AxisOS Bio‑Rhythm Engine — PP‑CLI v2  
Heartbeat‑driven agent loop with persona‑swappable narration, modular tentacles, and Cloud Run deployment.

---

## 🧩 Project Structure

axisos-biorhythm-engine/
│
├── heartbeat_agent.py        # Core rhythm loop (PP‑CLI v2)
├── biorhythm_engine.py       # Full engine (Cloud Run entrypoint wrapper)
├── narration.py              # PP + Medea narration tentacle
├── state_machine.py          # BPM → mode mapping + goal transitions
├── renderer.py               # Console + JSON rendering tentacle
│
├── main.py                   # Cloud Run HTTP entrypoint
├── agent.yaml                # Gemini Agent API config
├── manifest.json             # Gemini agent manifest
├── tools.json                # Gemini tool schemas
│
├── requirements.txt          # Python dependencies
├── Dockerfile                # Cloud Run container
├── project_id.txt            # GCP project identifier
│
└── README.md                 # This file

---

## 🧠 Architecture Overview

AxisOS Bio‑Rhythm Engine follows **PP‑CLI v2 lineage**:

### Core
- heartbeat loop  
- task planning  
- task execution  

### Tentacles
- narration → PP (architectural) or Medea (presentation)  
- state_machine → BPM → mode → goal transitions  
- renderer → console or JSON output  

### Cloud Run Layer
- `main.py` exposes `/run`  
- Gemini Agent API wraps the engine  
- Dockerfile builds the container  

Everything is modular, persona‑agnostic, and predictable.

---

## 🚀 Spin‑Up Instructions (Local)

### 1. Install dependencies

pip install -r requirements.txt

### 2. Run the engine locally

python heartbeat_agent.py

Or with Medea narration:

python heartbeat_agent.py medea


### 3. Run the Cloud Run entrypoint locally

python main.py

Then POST to it:

curl -X POST http://localhost:8080/run \
-H "Content-Type: application/json" \
-d '{"goal": "generate_report", "delay": 1.0}'


---

## ☁️ Deploying to Cloud Run

### 1. Build the container

gcloud builds submit --tag gcr.io/$(cat project_id.txt)/axisos-biorhythm-engine

### 2. Deploy

gcloud run deploy axisos-biorhythm-engine \
--image gcr.io/$(cat project_id.txt)/axisos-biorhythm-engine \
--platform managed \
--region us-west1 \
--allow-unauthenticated


### 3. Trigger the engine

curl -X POST https://<cloud-run-url>/run \
-H "Content-Type: application/json" \
-d '{"goal": "generate_report"}'


---

## 🎭 Persona Selection (PP or Medea)

Inside `heartbeat_agent.py`:

main(persona="pp")
main(persona="medea")


Inside Cloud Run:
{
"goal": "generate_report",
"persona": "medea"
}

---

## 📄 License  
Internal AxisOS development artifact — not for external distribution.
