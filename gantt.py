# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "kaleido",
#     "numpy",
#     "pandas",
#     "plotly",
# ]
# ///

import plotly.express as px
import pandas as pd


def assign(task: str, start: str, finish: str, resource: str = "all") -> dict[str, str]:
    return {
        "task": task,
        "start": start,
        "finish": finish,
        "resource": resource,
    }

def main() -> None:
    """Create a Gantt chart."""

    df = pd.DataFrame([
        assign("plan summer school", "2026-03-01", "2026-06-20", "Schaffner"),
        assign("plan summer school", "2028-03-01", "2028-06-20", "Schaffner"),
        assign("plan summer school", "2030-03-01", "2030-06-20", "Schaffner"),

        assign("hold summer school", "2026-06-21", "2026-06-30", "all"),
        assign("hold summer school", "2028-06-21", "2028-06-30", "all"),
        assign("hold summer school", "2030-06-21", "2030-06-30", "all"),

        assign("journal article", "2026-04-01", finish="2026-06-15", resource="all"),
        assign("journal article", "2029-04-01", finish="2029-06-15", resource="all"),

        assign("metadata standards", "2025-07-01", "2026-04-30", "Murphy"),

        assign("PyHC interoperability", "2026-07-01", "2028-06-30", "Murphy"),


        assign("metadata standards", "2028-07-01", "2029-07-30", "Murphy"),

        assign("metadata standards", "2029-07-01", "2030-07-30", "Murphy"),


        
        assign("A", "2025-07-01", "2026-06-30", "postbac/predoc"),
        assign("B", "2026-07-01", "2027-06-30", "postbac/predoc"),
        assign("C", "2027-07-01", "2028-06-30", "postbac/predoc"),

        assign("Distribution functions", "2028-07-01", "2029-06-30", "postbac/predoc"),
        assign("Turbulence analysis", "2029-07-01", "2030-06-30", "postbac/predoc"),

        assign("Thomson 1", "2025-07-01", "2026-06-30", "UCLA"),
        assign("Thomson 2", "2026-07-01", "2027-06-30", "UCLA"),
        assign("Shadowgraphy", "2027-07-01", "2028-06-30", "UCLA"),
        assign("Langmuir", "2028-07-01", "2029-06-30", "UCLA"),
        assign("LIF", "2029-07-01", "2030-06-30", "UCLA"),

        assign("select students", "2025-12-01", "2025-12-30", "CRANE"),
        assign("CRANE seminar", "2026-01-01", "2026-05-25", "CRANE"),
        assign("select students", "2026-12-01", "2026-12-30", "CRANE"),
        assign("CRANE seminar", "2027-01-01", "2027-05-25", "CRANE"),

    ])

    fig = px.timeline(df, x_start="start", x_end="finish", y="task", color="resource")
    fig.update_yaxes(autorange="reversed")
    fig.show()

if __name__ == "__main__":
    main()
