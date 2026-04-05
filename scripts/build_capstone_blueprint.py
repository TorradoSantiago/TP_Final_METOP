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
                "mechanism": "Pocketbook assessments and sociotropic expectations shape retrospective voting.",
                "core_variables": "Economic outlook, government approval, vote intention",
                "test_family": "Cross-tabulation, ordered logit, marginal effects",
                "deliverable": "Probability profiles by economic sentiment segment",
            },
            {
                "hypothesis_id": "H2",
                "hypothesis": "Institutional trust predicts turnout intention and policy legitimacy.",
                "mechanism": "Trust reduces political alienation and raises willingness to endorse institutions.",
                "core_variables": "Trust in institutions, turnout intention, reform support",
                "test_family": "Index construction, logistic regression, calibration plots",
                "deliverable": "Trust index and turnout-probability table",
            },
            {
                "hypothesis_id": "H3",
                "hypothesis": "Issue salience segments the electorate into distinct opinion clusters.",
                "mechanism": "Priority issues structure how voters map identity and choice.",
                "core_variables": "Issue salience, ideology, candidate preference",
                "test_family": "MCA/PCA, clustering, silhouette diagnostics",
                "deliverable": "Segment profiles and narrative personas",
            },
            {
                "hypothesis_id": "H4",
                "hypothesis": "Sociodemographic differences moderate the relationship between issue salience and political behavior.",
                "mechanism": "Age, education, and class position shape how issues are interpreted.",
                "core_variables": "Age, education, region, class proxies, political behavior",
                "test_family": "Interaction models, subgroup contrasts, partial dependence charts",
                "deliverable": "Heterogeneity matrix by subgroup",
            },
            {
                "hypothesis_id": "H5",
                "hypothesis": "Candidate evaluation is driven by both valence attributes and ideological proximity.",
                "mechanism": "Voters reward competence cues but also anchor on ideological fit.",
                "core_variables": "Candidate ratings, ideology, leadership traits",
                "test_family": "Factor analysis, multinomial logit, dominance analysis",
                "deliverable": "Relative importance of valence and ideology",
            },
            {
                "hypothesis_id": "H6",
                "hypothesis": "Media consumption patterns amplify differences in economic expectations and trust.",
                "mechanism": "Information environments mediate beliefs about performance and legitimacy.",
                "core_variables": "Media source, economic outlook, institutional trust",
                "test_family": "Difference-in-means, propensity-score weighting, robustness checks",
                "deliverable": "Media ecosystem comparison table",
            },
        ]
    )


def build_theoretical_framework() -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "construct": "Retrospective voting",
                "theoretical_anchor": "Voters reward or punish incumbents based on perceived performance.",
                "observable_proxies": "Government approval, vote intention, economic expectations",
                "why_it_matters": "Connects subjective evaluations with concrete electoral behavior.",
            },
            {
                "construct": "Institutional trust",
                "theoretical_anchor": "Trust sustains compliance, turnout, and acceptance of policy outcomes.",
                "observable_proxies": "Confidence in Congress, courts, presidency, electoral authority",
                "why_it_matters": "Separates dissatisfaction with outcomes from dissatisfaction with the regime itself.",
            },
            {
                "construct": "Issue salience",
                "theoretical_anchor": "The issues voters prioritize structure what counts as persuasive politics.",
                "observable_proxies": "Top national problem, policy priorities, reform preferences",
                "why_it_matters": "Supports segmentation and message design rather than one-size-fits-all conclusions.",
            },
            {
                "construct": "Political behavior",
                "theoretical_anchor": "Attitudes matter when they translate into participation, support, or rejection.",
                "observable_proxies": "Turnout intention, candidate preference, policy legitimacy",
                "why_it_matters": "Keeps the capstone tied to behavioral outcomes instead of pure description.",
            },
            {
                "construct": "Information environment",
                "theoretical_anchor": "Media exposure shapes priors, trust, and perceived performance.",
                "observable_proxies": "Primary media source, frequency of news consumption, platform mix",
                "why_it_matters": "Introduces a mechanism for heterogeneity and potential intervention design.",
            },
        ]
    )


def build_methodological_test_plan() -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "stage": "Measurement",
                "test": "Reliability and dimensionality checks",
                "purpose": "Validate scales for trust, ideology, and issue salience before modeling.",
                "tools": "Cronbach alpha, polychoric PCA/factor analysis",
                "output": "Validated index specification",
            },
            {
                "stage": "Description",
                "test": "Weighted descriptive tables and uncertainty bands",
                "purpose": "Summarize the electorate before moving to causal or predictive claims.",
                "tools": "Survey weights, confidence intervals, subgroup dashboards",
                "output": "Clean descriptive baseline",
            },
            {
                "stage": "Association",
                "test": "Difference-in-means and non-parametric distribution tests",
                "purpose": "Check whether headline contrasts appear before fitting multivariable models.",
                "tools": "Mann-Whitney, Kruskal-Wallis, Spearman",
                "output": "First-pass evidence for each hypothesis",
            },
            {
                "stage": "Modeling",
                "test": "Logit, ordered logit, multinomial logit",
                "purpose": "Model turnout, approval, and vote intention using interpretable coefficients.",
                "tools": "Marginal effects, calibration plots, ROC/AUC where relevant",
                "output": "Core inferential results",
            },
            {
                "stage": "Segmentation",
                "test": "Latent or empirical clustering",
                "purpose": "Identify coherent voter blocs based on issue salience and trust patterns.",
                "tools": "K-means, hierarchical clustering, silhouette and stability metrics",
                "output": "Electorate segments with narrative profiles",
            },
            {
                "stage": "Robustness",
                "test": "Alternative codings, reweighting, and sensitivity checks",
                "purpose": "Test whether the conclusions depend on specific operational choices.",
                "tools": "Bootstrap, propensity weights, alternative thresholds",
                "output": "Credibility appendix",
            },
        ]
    )


def build_validity_matrix() -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "risk": "Construct validity",
                "threat": "Survey items may not map cleanly onto trust or ideology.",
                "mitigation": "Document coding decisions and test internal consistency before index construction.",
            },
            {
                "risk": "Selection bias",
                "threat": "Nonresponse and low-propensity groups may be underrepresented.",
                "mitigation": "Use weights, compare sample margins to public benchmarks, and run weighted/unweighted contrasts.",
            },
            {
                "risk": "Model dependence",
                "threat": "Conclusions may change with coding thresholds or link functions.",
                "mitigation": "Report alternative specifications and keep a robustness appendix.",
            },
            {
                "risk": "Overinterpretation",
                "threat": "Correlational results may be framed as causal.",
                "mitigation": "State scope conditions clearly and separate explanatory from predictive claims.",
            },
            {
                "risk": "Temporal instability",
                "threat": "Campaign dynamics can change quickly around major events.",
                "mitigation": "Anchor findings to survey fieldwork dates and flag where repeat measurement is needed.",
            },
        ]
    )


def build_measurement_blueprint() -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "domain": "Economic outlook",
                "example_items": "Personal finances, country trajectory, inflation expectations",
                "preferred_scale": "Ordered categorical",
                "analytic_use": "Approval and vote models",
            },
            {
                "domain": "Institutional trust",
                "example_items": "Confidence in courts, congress, presidency, electoral authority",
                "preferred_scale": "Likert or ordinal composite",
                "analytic_use": "Turnout and legitimacy models",
            },
            {
                "domain": "Issue salience",
                "example_items": "Main national problem, most urgent reform, policy priorities",
                "preferred_scale": "Top choice plus ranked preferences",
                "analytic_use": "Segmentation and heterogeneity analysis",
            },
            {
                "domain": "Political behavior",
                "example_items": "Turnout intention, vote intention, government approval",
                "preferred_scale": "Binary, ordered, or multinomial",
                "analytic_use": "Outcome layer",
            },
            {
                "domain": "Exposure and context",
                "example_items": "Media source, education, age, class proxy, geography",
                "preferred_scale": "Categorical plus continuous controls",
                "analytic_use": "Moderation and robustness checks",
            },
        ]
    )


def build_deliverable_roadmap() -> pd.DataFrame:
    return pd.DataFrame(
        [
            {"phase": "Problem framing", "weeks": 1, "deliverable": "Research question, scope, and theoretical memo"},
            {"phase": "Source audit", "weeks": 1, "deliverable": "Dataset shortlist, codebook review, comparability note"},
            {"phase": "Cleaning and harmonization", "weeks": 2, "deliverable": "Reusable scripts and clean analysis sample"},
            {"phase": "Measurement design", "weeks": 1, "deliverable": "Indices, coding rules, and diagnostics"},
            {"phase": "Core inference", "weeks": 2, "deliverable": "Main regression tables and marginal effects"},
            {"phase": "Segmentation", "weeks": 1, "deliverable": "Cluster profiles and audience narratives"},
            {"phase": "Robustness appendix", "weeks": 1, "deliverable": "Sensitivity checks and alternative specifications"},
            {"phase": "Executive packaging", "weeks": 1, "deliverable": "Portfolio PDF, README, and presentation"},
        ]
    )


def export_workflow_figure(roadmap: pd.DataFrame) -> None:
    chart_data = roadmap.copy()
    chart_data["start_week"] = chart_data["weeks"].cumsum() - chart_data["weeks"]

    plt.figure(figsize=(11.5, 6.5))
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
    plt.savefig(FIGURES_DIR / "capstone_delivery_roadmap.png", dpi=160)
    plt.close()


def export_research_architecture_figure() -> None:
    fig, ax = plt.subplots(figsize=(11.5, 6))
    ax.axis("off")
    boxes = [
        (0.05, 0.55, 0.24, 0.22, "Theory\nEconomic voting,\ntrust, salience"),
        (0.38, 0.55, 0.24, 0.22, "Measurement\nIndices, coding,\nscale checks"),
        (0.71, 0.55, 0.24, 0.22, "Inference\nLogit, clusters,\nrobustness"),
        (0.38, 0.15, 0.24, 0.22, "Delivery\nExecutive brief,\nportfolio story"),
    ]

    for x, y, w, h, label in boxes:
        rect = plt.Rectangle((x, y), w, h, facecolor="#edf4ff", edgecolor="#145da0", linewidth=2)
        ax.add_patch(rect)
        ax.text(x + w / 2, y + h / 2, label, ha="center", va="center", fontsize=12, color="#13243b")

    arrows = [
        ((0.29, 0.66), (0.38, 0.66)),
        ((0.62, 0.66), (0.71, 0.66)),
        ((0.5, 0.55), (0.5, 0.37)),
    ]
    for start, end in arrows:
        ax.annotate("", xy=end, xytext=start, arrowprops=dict(arrowstyle="->", lw=2, color="#145da0"))

    ax.set_title("Capstone research architecture", fontsize=16, color="#13243b", pad=10)
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "capstone_research_architecture.png", dpi=160)
    plt.close()


def export_test_strategy_figure(test_plan: pd.DataFrame) -> None:
    chart = test_plan.copy()
    chart["count"] = [1.0, 1.2, 1.0, 1.6, 1.1, 1.0]

    plt.figure(figsize=(11.5, 6.5))
    plt.barh(chart["stage"], chart["count"], color=["#145da0", "#1f77b4", "#2ca02c", "#9467bd", "#ff7f0e", "#8c564b"])
    for _, row in chart.iterrows():
        plt.text(row["count"] + 0.03, row["stage"], row["test"], va="center", fontsize=10, color="#13243b")
    plt.xlim(0, 2.2)
    plt.xlabel("Relative analytic depth")
    plt.ylabel("")
    plt.title("Methodological test strategy")
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "capstone_test_strategy.png", dpi=160)
    plt.close()


def main() -> None:
    ensure_directories()

    hypothesis_matrix = build_hypothesis_matrix()
    theoretical_framework = build_theoretical_framework()
    methodological_test_plan = build_methodological_test_plan()
    validity_matrix = build_validity_matrix()
    measurement_blueprint = build_measurement_blueprint()
    deliverable_roadmap = build_deliverable_roadmap()

    hypothesis_matrix.to_csv(TABLES_DIR / "hypothesis_matrix.csv", index=False)
    theoretical_framework.to_csv(TABLES_DIR / "theoretical_framework.csv", index=False)
    methodological_test_plan.to_csv(TABLES_DIR / "methodological_test_plan.csv", index=False)
    validity_matrix.to_csv(TABLES_DIR / "validity_matrix.csv", index=False)
    measurement_blueprint.to_csv(TABLES_DIR / "measurement_blueprint.csv", index=False)
    deliverable_roadmap.to_csv(TABLES_DIR / "deliverable_roadmap.csv", index=False)

    export_workflow_figure(deliverable_roadmap)
    export_research_architecture_figure()
    export_test_strategy_figure(methodological_test_plan)

    print("Capstone blueprint exported.")
    print(f"- {TABLES_DIR / 'hypothesis_matrix.csv'}")
    print(f"- {TABLES_DIR / 'theoretical_framework.csv'}")
    print(f"- {TABLES_DIR / 'methodological_test_plan.csv'}")
    print(f"- {TABLES_DIR / 'validity_matrix.csv'}")
    print(f"- {TABLES_DIR / 'measurement_blueprint.csv'}")
    print(f"- {TABLES_DIR / 'deliverable_roadmap.csv'}")
    print(f"- {FIGURES_DIR / 'capstone_delivery_roadmap.png'}")
    print(f"- {FIGURES_DIR / 'capstone_research_architecture.png'}")
    print(f"- {FIGURES_DIR / 'capstone_test_strategy.png'}")


if __name__ == "__main__":
    main()
