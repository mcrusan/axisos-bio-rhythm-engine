#!/usr/bin/env python3
# ============================================================
# File:        main.py
# Description: Cloud Run entrypoint for AxisOS Bio‑Rhythm Engine
# Version:     2.0
# ============================================================

from flask import Flask, request, jsonify
from biorhythm_engine import run_biorhythm_engine

app = Flask(__name__)

@app.route("/run", methods=["POST"])
def run_engine():
    payload = request.get_json(silent=True) or {}
    goal = payload.get("goal", "generate_report")
    delay = float(payload.get("delay", 1.0))

    print(f"[pp-core] Cloud Run request received: goal={goal}, delay={delay}")
    run_biorhythm_engine(initial_goal=goal, delay_seconds=delay)

    return jsonify({"status": "completed", "goal": goal}), 200


if __name__ == "__main__":
    print("[pp-core] Cloud Run entrypoint starting (local mode)")
    app.run(host="0.0.0.0", port=8080)
