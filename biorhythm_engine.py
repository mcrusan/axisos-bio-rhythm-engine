#!/usr/bin/env python3
# ============================================================
# File:        biorhythm_engine.py
# Description: AxisOS Bio‑Rhythm Engine — PP‑CLI v2
# Author:      Marc
# Version:     2.0
# ------------------------------------------------------------
# Notes:
#   - Heartbeat-driven agent loop.
#   - PP‑CLI lineage: core‑tentacle architecture.
#   - Ready for Cloud Run wrapping via main.py.
# ============================================================

"""
Module Docstring:
    Bio‑Rhythm Engine for AxisOS.

    Responsibilities:
    - Accept heartbeat input (simulated or real).
    - Map BPM / beats to agent state.
    - Plan and execute tasks based on goals.
    - Emit clear, inspectable console output.
"""

import time
from dataclasses import dataclass


# ============================================================
# State Model (Tentacle)
# ============================================================

@dataclass
class AgentState:
    goal: str = None
    tasks: list = None
    scans: int = 0
    reports: int = 0
    bpm: int = 0
    mode: str = "idle"   # e.g., "idle", "active", "alert"


# ============================================================
# Heartbeat & Mapping (Core)
# ============================================================

def read_heartbeat() -> int:
    """
    Simulate heartbeat input.
    In a real deployment, this would read from a sensor or API.
    """
    bpm = 72  # placeholder for now
    print(f"[pulse] bpm={bpm}")
    return bpm


def map_bpm_to_mode(bpm: int) -> str:
    """
    Map BPM to a qualitative mode.
    """
    if bpm < 60:
        return "idle"
    elif 60 <= bpm < 90:
        return "active"
    else:
        return "alert"


def update_state_from_bpm(state: AgentState, bpm: int):
    """
    Update agent state based on BPM.
    """
    state.bpm = bpm
    state.mode = map_bpm_to_mode(bpm)
    print(f"[pp-core] state updated from bpm: mode={state.mode}")


# ============================================================
# Task Planning & Execution (Tentacle)
# ============================================================

def plan_tasks(state: AgentState):
    """
    Assign tasks based on current goal and mode.
    """
    if state.goal == "scan":
        if state.mode in ("active", "alert"):
            state.tasks = ["scan_area"]
        else:
            state.tasks = []
    elif state.goal == "generate_report":
        if state.mode == "active":
            state.tasks = ["compile_report"]
        else:
            state.tasks = []
    else:
        state.tasks = []

    print(f"[pp-core] tasks planned: {state.tasks}")


def execute_next_task(state: AgentState):
    """
    Execute the next task in the queue.
    """
    if not state.tasks:
        print("[pp-core] no tasks to execute")
        return

    task = state.tasks.pop(0)
    print(f"[pp-core] executing: {task}")

    if task == "scan_area":
        state.scans += 1
        print(f"[agent] scan complete (total scans={state.scans})")

    elif task == "compile_report":
        state.reports += 1
        print(f"[agent] report generated (total reports={state.reports})")


# ============================================================
# Narration (Presentation Layer Hooks)
# ============================================================

def narrate_state(state: AgentState, beat: int):
    """
    Narration hook — this is where Medea can attach later.
    For now, it's PP‑style console narration.
    """
    print(f"[heartbeat] beat #{beat}")
    print(f"[agent] bpm={state.bpm}, mode={state.mode}")
    print(f"[agent] goal: {state.goal}")
    print(f"[agent] tasks: {state.tasks}")
    print(f"[agent] state: scans={state.scans}, reports={state.reports}")


# ============================================================
# Main Loop (Core)
# ============================================================

def run_biorhythm_engine(initial_goal: str = "generate_report", delay_seconds: float = 1.0):
    """
    Core Bio‑Rhythm loop.
    Designed to be wrapped by a Cloud Run entrypoint.
    """
    state = AgentState(goal=initial_goal)
    beat = 0

    print("[pp-core] Bio‑Rhythm Engine starting with goal:", state.goal)

    while True:
        beat += 1

        bpm = read_heartbeat()
        update_state_from_bpm(state, bpm)
        plan_tasks(state)

        # ⭐ Narration hook (PP‑CLI v2)
        narrate_state(state, beat)

        execute_next_task(state)

        # Exit condition — explicit, logged
        if state.goal == "generate_report" and state.reports >= 1 and not state.tasks:
            print("[pp-core] goal achieved: report generated. Engine going idle.")
            break

        time.sleep(delay_seconds)


# ============================================================
# Entrypoint (for local runs)
# ============================================================

if __name__ == "__main__":
    run_biorhythm_engine()
