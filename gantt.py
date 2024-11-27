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

    df = pd.DataFrame([
        assign("plan summer school", "2026-03-01", "2026-06-20", "Schaffner"),
        assign("plan summer school", "2028-03-01", "2028-06-20", "Schaffner"),
        assign("plan summer school", "2030-03-01", "2030-06-20", "Schaffner"),

        assign("hold summer school", "2026-06-21", "2026-06-30", "all"),
        assign("hold summer school", "2028-06-21", "2028-06-30", "all"),
        assign("hold summer school", "2030-06-21", "2030-06-30", "all"),

        assign("metadata standards", *year1, "Murphy"),
        assign("PyHC interoperability", "2026-07-01", "2028-06-30", "Murphy"),
        assign("metadata standards", "2028-07-01", "2030-06-30", "Murphy"),
        assign("metadata standards", "2029-07-01", "2030-07-30", "Murphy"),

        assign("distribution functions", *year1, "postbac/predoc"),
        assign("magnetic topology", *year2, "postbac/predoc"),
        assign("dispersion solver", *year3, "postbac/predoc"),
        assign("TBD", *year4, "postbac/predoc"),
        assign("turbulence/shocks", *year5, "postbac/predoc"),

        # UCLA

        assign("Thomson scattering", *year1, "UCLA"), # hedp + fun

        assign("Shadowgraphy", *year2, "UCLA"), # hepd
        assign("magnetic probes", *year2, "UCLA"), # fun

        assign("Refractometry", *year3, "UCLA"), # hedp
        assign("LIF", *year3, "UCLA"), # fun

        assign("CPR reconstruction", *year4, "UCLA"), # hedp
        assign("probes", *year4, "UCLA"), # fun

        assign("particle energy spectrometers", *year5, "UCLA"), # hedp
        assign("probes", *year5, "UCLA"), # fun

        assign("select students", "2025-12-01", "2025-12-30", "CRANE"),
        assign("CRANE seminar", "2026-01-01", "2026-05-25", "CRANE"),
        assign("select students", "2026-12-01", "2026-12-30", "CRANE"),
        assign("CRANE seminar", "2027-01-01", "2027-05-25", "CRANE"),

    ])

    fig = px.timeline(df, x_start="Start", x_end="Finish", y="Task", color="Resource")
    fig.update_yaxes(autorange="reversed")
#    fig.show()
    fig.write_image("gantt.png")

    print(dir(fig))

if __name__ == "__main__":
    main()
