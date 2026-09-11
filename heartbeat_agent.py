#!/usr/bin/env python3
# ============================================================
# File:        heartbeat_agent.py
# Description: AxisOS Bio‑Rhythm Engine — PP‑CLI v2 agent loop
# Author:      Marc
# Version:     2.0
# ============================================================

"""
Module Docstring:
    Heartbeat-driven agent loop for AxisOS Bio‑Rhythm Engine.
    Follows PP‑CLI lineage: predictable logs, explicit state,
    and no silent side effects.
"""

import time
from dataclasses import dataclass
from narration import narrate   # ⭐ Combined narration tentacle


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
    mode: str = "idle"


# ============================================================
# Core Functions (Core)
# ============================================================

def pulse():
    print("[pulse] beat received")


def plan_tasks(state: AgentState):
    if state.goal == "scan":
        state.tasks = ["scan_area"]
    elif state.goal == "generate_report":
        state.tasks = ["compile_report"]
    else:
        state.tasks = []
    print(f"[pp-core] tasks planned: {state.tasks}")


def execute_next_task(state: AgentState):
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
# Main Loop (Core)
# ============================================================

def main(persona="pp"):
    state = AgentState(goal="generate_report")
    beat = 0

    print("[pp-core] agent starting with goal:", state.goal)

    while True:
        beat += 1

        pulse()
        plan_tasks(state)

        # ⭐ Combined narration (PP or Medea)
        narrate(state, beat, persona=persona)

        execute_next_task(state)

        if state.goal == "generate_report" and state.reports >= 1 and not state.tasks:
            print("[pp-core] goal achieved: report generated. Agent going idle.")
            break

        time.sleep(1)


# ============================================================
# Entrypoint
# ============================================================

if __name__ == "__main__":
    main(persona="pp")   # Change to "medea" to switch narration
