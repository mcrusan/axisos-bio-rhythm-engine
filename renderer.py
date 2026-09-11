# ============================================================
# File:        renderer.py
# Description: Renderer tentacle for AxisOS Bio‑Rhythm Engine
# Author:      Marc
# Version:     2.0
# ============================================================

"""
Module Docstring:
    Rendering layer for AxisOS Bio‑Rhythm Engine.
    Converts agent state into structured output formats.
"""

# ============================================================
# Console Renderer (default)
# ============================================================

def render_console(state):
    return (
        f"[render] bpm={state.bpm}, mode={state.mode}, "
        f"goal={state.goal}, scans={state.scans}, reports={state.reports}"
    )


# ============================================================
# JSON Renderer (Cloud Run)
# ============================================================

def render_json(state):
    return {
        "bpm": state.bpm,
        "mode": state.mode,
        "goal": state.goal,
        "scans": state.scans,
        "reports": state.reports,
    }


# ============================================================
# Renderer Router
# ============================================================

def render(state, format="console"):
    if format == "json":
        return render_json(state)
    return render_console(state)
