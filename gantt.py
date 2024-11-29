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
        "Task": task,
        "Start": start,
        "Finish": finish,
        "Resource": resource,
    }

def main() -> None:
    """Create a Gantt chart."""

    year1 = ("2025-07-01", "2026-06-30")
    year2 = ("2026-07-01", "2027-06-30")
    year3 = ("2027-07-01", "2028-06-30")
    year4 = ("2028-07-01", "2029-06-30")
    year5 = ("2029-07-01", "2030-06-30")

    years = [year1, year2, year3, year4, year5]
    full = (year1[0], year5[1])

    sao_postbac = [
        "distribution",
        "dispersion solver",
        "turbulence analysis",
        "equilibrium/stability",
        "magnetic topology",
#        "shock analysis",
    ]

    sao_tasks = []
    for year, sao_postbac in zip(years, sao_postbac):
        sao_tasks.append(assign(sao_postbac, *year, "SAO postbac/predoc"))

    df = pd.DataFrame([

        assign("package infrastructure", *full, "Murphy"),

        assign("NEI/fiasco", *year1,"Murphy"),
        #assign("Plasma-MDS/openPMD", *year1, "Murphy"),
        assign("PyHC interoperability", *year2, "Murphy"),
        assign("metadata standards", "2027-07-01", "2030-06-30", "Murphy"),

        *sao_tasks,

        # UCLA

        assign("Thomson scattering", *year1, "UCLA"),  # hedp + fun
        assign("CPR reconstruction", *year2, "UCLA"),  # hedp
        assign("shadowgraphy/refractometry", *year3, "UCLA"), # hepd
        assign("LIF", *year4, "UCLA"), # fun
        assign("particle spectrometers", *year5, "UCLA"),  # hedp

        assign("plasma diagnostics", *full, "Everson"),  # fun

        assign("organize summer school", "2026-03-01", "2026-06-30", "BMC"),
        assign("organize summer school", "2028-03-01", "2028-06-30", "BMC"),
        assign("organize summer school", "2030-03-01", "2030-06-30", "BMC"),

        assign("CRANE planning", "2025-11-01", "2025-12-30", "CRANE"),
        assign("CRANE semester", "2026-01-01", "2026-05-25", "CRANE"),
        assign("CRANE planning", "2026-11-01", "2026-12-30", "CRANE"),
        assign("CRANE semester", "2027-01-01", "2027-05-25", "CRANE"),

    ])

    fig = px.timeline(df, x_start="Start", x_end="Finish", y="Task", color="Resource")
    fig.update_yaxes(autorange="reversed")
    fig.show()
    fig.write_image("gantt.png")

if __name__ == "__main__":
    main()
