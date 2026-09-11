# ============================================================
# File:        state_machine.py
# Description: State machine tentacle for AxisOS Bio‑Rhythm Engine
# Author:      Marc
# Version:     2.0
# ============================================================

"""
Module Docstring:
    State machine for AxisOS Bio‑Rhythm Engine.
    Handles BPM → mode mapping and goal transitions.
"""

# ============================================================
# BPM → Mode Mapping
# ============================================================

def map_bpm_to_mode(bpm: int) -> str:
    if bpm < 60:
        return "idle"
    elif 60 <= bpm < 90:
        return "active"
    else:
        return "alert"


# ============================================================
# Goal Transition Logic
# ============================================================

def update_goal(state):
    """
    Update the agent's goal based on mode or future rules.
    PP‑CLI v2: explicit, predictable transitions.
    """
    if state.mode == "alert" and state.goal != "scan":
        state.goal = "scan"

    # Future expansion:
    # if state.mode == "idle" and state.goal == "scan":
    #     state.goal = "generate_report"

    return state.goal


# ============================================================
# State Update
# ============================================================

def update_state_from_bpm(state, bpm: int):
    state.bpm = bpm
    state.mode = map_bpm_to_mode(bpm)
    update_goal(state)
    return state
