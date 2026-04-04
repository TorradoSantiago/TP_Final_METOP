from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[1]
TABLES_DIR = BASE_DIR / "outputs" / "tables"
FIGURES_DIR = BASE_DIR / "outputs" / "figures"


def ensure_directories() -> None:
    TABLES_DIR.mkdir(parents=True, exist_ok=True)
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)


def build_hypothesis_matrix() -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "hypothesis_id": "H1",
                "hypothesis": "Economic expectations are associated with government approval and vote intention.",
                "primary_variables": "Economic outlook, government approval, vote intention",
                "method": "Cross-tabulation, logistic regression, marginal effects",
                "evidence_status": "Pending source data",
            },
            {
                "hypothesis_id": "H2",
                "hypothesis": "Institutional trust predicts turnout intention and policy legitimacy.",
                "primary_variables": "Trust in institutions, turnout intention, policy support",
                "method": "Index construction, segmentation, regression analysis",
                "evidence_status": "Pending source data",
            },
            {
                "hypothesis_id": "H3",
                "hypothesis": "Issue salience segments the electorate into distinct opinion clusters.",
                "primary_variables": "Issue salience, ideology, candidate preference",
                "method": "Cluster analysis, dimensional reduction, profile summaries",
                "evidence_status": "Pending source data",
            },
            {
                "hypothesis_id": "H4",
                "hypothesis": "Sociodemographic differences moderate the relationship between issue salience and political behavior.",
                "primary_variables": "Age, education, region, class proxies, political behavior",
                "method": "Interaction models and subgroup analysis",
                "evidence_status": "Pending source data",
            },
        ]
    )


def build_deliverable_roadmap() -> pd.DataFrame:
    return pd.DataFrame(
        [
            {"phase": "Problem framing", "weeks": 1, "deliverable": "Research question and hypothesis matrix"},
            {"phase": "Data acquisition", "weeks": 1, "deliverable": "Survey source log and codebook review"},
            {"phase": "Cleaning and harmonization", "weeks": 2, "deliverable": "Reusable processing scripts and clean dataset"},
            {"phase": "Core analysis", "weeks": 2, "deliverable": "Tables, models, and segmentation outputs"},
            {"phase": "Narrative synthesis", "weeks": 1, "deliverable": "Executive brief and presentation assets"},
            {"phase": "Publication layer", "weeks": 1, "deliverable": "Portfolio README, PDF brief, and public repository polish"},
        ]
    )


def export_workflow_figure(roadmap: pd.DataFrame) -> None:
    chart_data = roadmap.copy()
    chart_data["start_week"] = chart_data["weeks"].cumsum() - chart_data["weeks"]

    plt.figure(figsize=(11, 6))
    plt.barh(
        y=chart_data["phase"],
        width=chart_data["weeks"],
        left=chart_data["start_week"],
        color="#145da0",
        alpha=0.9,
    )

    for _, row in chart_data.iterrows():
        plt.text(
            row["start_week"] + row["weeks"] / 2,
            row["phase"],
            f"{row['weeks']}w",
            ha="center",
            va="center",
            color="white",
            fontsize=10,
            fontweight="bold",
        )

    plt.title("Capstone delivery roadmap")
    plt.xlabel("Week")
    plt.ylabel("")
    plt.xticks(range(0, int(chart_data["weeks"].sum()) + 1))
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "capstone_delivery_roadmap.png", dpi=150)
    plt.close()


def main() -> None:
    ensure_directories()
    hypothesis_matrix = build_hypothesis_matrix()
    deliverable_roadmap = build_deliverable_roadmap()

    hypothesis_matrix.to_csv(TABLES_DIR / "hypothesis_matrix.csv", index=False)
    deliverable_roadmap.to_csv(TABLES_DIR / "deliverable_roadmap.csv", index=False)
    export_workflow_figure(deliverable_roadmap)

    print("Capstone blueprint exported.")
    print(f"- {TABLES_DIR / 'hypothesis_matrix.csv'}")
    print(f"- {TABLES_DIR / 'deliverable_roadmap.csv'}")
    print(f"- {FIGURES_DIR / 'capstone_delivery_roadmap.png'}")


if __name__ == "__main__":
    main()
