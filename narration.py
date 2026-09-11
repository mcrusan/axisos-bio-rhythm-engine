# ============================================================
# File:        narration.py
# Description: Combined narration tentacle for AxisOS Bio‑Rhythm Engine
# Author:      Marc
# Version:     2.0
# ------------------------------------------------------------
# Notes:
#   - PP‑CLI v2 lineage: narration is a separate tentacle.
#   - PP = architectural voice
#   - Medea = presentation voice
#   - Core engine remains persona‑agnostic
# ============================================================

"""
Module Docstring:
    Narration layer for AxisOS Bio‑Rhythm Engine.
    Provides PP-style architectural narration and
    Medea-style presentation narration.
"""

# ============================================================
# PP Narration (architectural)
# ============================================================

def pp_narrate_state(state, beat):
    print(f"[heartbeat] beat #{beat}")
    print(f"[agent] bpm={state.bpm}, mode={state.mode}")
    print(f"[agent] goal: {state.goal}")
    print(f"[agent] tasks: {state.tasks}")
    print(f"[agent] state: scans={state.scans}, reports={state.reports}")


# ============================================================
# Medea Narration (presentation)
# ============================================================

def medea_narrate_state(state, beat):
    print(f"[medea] Beat {beat} acknowledged.")
    print(f"[medea] Rhythm: {state.bpm} BPM ({state.mode}).")
    print(f"[medea] Current goal: {state.goal}.")
    print(f"[medea] Task queue: {state.tasks}.")
    print(f"[medea] Progress → scans={state.scans}, reports={state.reports}.")


# ============================================================
# Narration Router
# ============================================================

def narrate(state, beat, persona="pp"):
    if persona == "medea":
        medea_narrate_state(state, beat)
    else:
        pp_narrate_state(state, beat)
