import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from matplotlib.gridspec import GridSpec
from input_read_bua_results import *

def main():
    # === Config ===
    output_folder = path_dir_simulation_all_alternatives
    excel_path = os.path.join(output_folder, "energy_results_combined.xlsx")
    sheet_name = "KPIs"

    plots_folder = os.path.join(output_folder, "plots")
    os.makedirs(plots_folder, exist_ok=True)
    output_path = os.path.join(plots_folder, "net_energy_compensation_stack_column.png")

    # === Read Data (with lowercase-safe columns) ===
    df = pd.read_excel(excel_path, sheet_name=sheet_name)
    df.columns = df.columns.str.lower()
    df = df[["case", "scenario", "net energy compensation - total"]].copy()
    df.rename(columns={"net energy compensation - total": "comp"}, inplace=True)
    df["use"] = 1.0 - df["comp"]
    df["comp [%]"] = df["comp"] * 100
    df["use [%]"] = df["use"] * 100

    cases = df["case"].astype(str).tolist()
    scenarios = df["scenario"].astype(str).tolist()
    comp = df["comp [%]"]
    use = df["use [%]"]
    x = list(range(len(df)))

    # === Identify Case Transitions for Grouping  ===
    case_transitions = [0]
    for i in range(1, len(cases)):
        if cases[i] != cases[i - 1]:
            case_transitions.append(i)
    case_transitions.append(len(cases))  # Add end marker

    # === Set up layout ===
    fig = plt.figure(figsize=(48, 14))
    gs = GridSpec(6, 1, height_ratios=[200, 1, 2.5, 1, 1.5, 4])  # plot, space, scenarios, space, cases, legend

    # === Bar chart ===
    ax_main = fig.add_subplot(gs[0, 0])
    ax_main.bar(x, comp, color="#08306B", edgecolor="black")
    ax_main.bar(x, use, bottom=comp, color="white", edgecolor="black")
    ax_main.set_ylim(0, 100)
    ax_main.set_ylabel("Percentage [%]", fontsize=18)
    ax_main.set_title("Net Energy Use and Compensation", fontsize=24, pad=20)
    ax_main.set_xticks([])
    ax_main.yaxis.grid(True, linestyle='--', alpha=0.5)

    # === Manual Scenario Text ===
    ax_scenarios = fig.add_subplot(gs[2, 0], sharex=ax_main)
    ax_scenarios.set_xlim(ax_main.get_xlim())
    ax_scenarios.set_ylim(0, 1)
    ax_scenarios.axis("off")

    # === Manual Case Text (centered per group) ===
    ax_cases = fig.add_subplot(gs[4, 0], sharex=ax_main)
    ax_cases.set_xlim(ax_main.get_xlim())
    ax_cases.set_ylim(0, 1)
    ax_cases.axis("off")

    # === Add vertical lines between case groups ===
    for idx in case_transitions[1:-1]:  # skip first and last
        for ax in [ax_main, ax_scenarios, ax_cases]:  # 👈 add to all 3 axes
            ax.axvline(
                x=idx - 0.5,
                color='black',      # 👈 make it black
                linestyle='-',      # 👈 solid line
                linewidth=0.8,
                zorder=0             # 👈 draw behind bars/text
            )


    # === Optional: Add shaded background bands (uncomment below if preferred over lines) ===
    # for i in range(len(case_transitions) - 1):
    #     start = case_transitions[i]
    #     end = case_transitions[i + 1]
    #     if i % 2 == 0:
    #         ax_main.axvspan(start - 0.5, end - 0.5, color='gray', alpha=0.05)

    for i, txt in enumerate(scenarios):
        ax_scenarios.text(i, -22.5, txt, fontsize=12, rotation=90, ha='center', va='bottom')

    unique_cases = df["case"].unique()
    for case in unique_cases:
        case_indices = df[df["case"] == case].index.tolist()
        if not case_indices:
            continue
        middle_index = sum(case_indices) / len(case_indices)
        ax_cases.text(
            middle_index, -9.0, str(case),  # -9.0 sets the Y location of the Cases
            fontsize=14, rotation=0,
            ha='center', va='top'
        )

    # === Legend at the very bottom ===
    ax_legend = fig.add_subplot(gs[5, 0])
    ax_legend.axis("off")
    legend_elements = [
        Patch(facecolor="#08306B", edgecolor="black", label="Net energy compensation"),
        Patch(facecolor="white", edgecolor="black", label="Net energy use")
    ]
    ax_legend.legend(
        handles=legend_elements,
        loc='center',
        ncol=2,
        fontsize=18,
        frameon=False,
        bbox_to_anchor=(0.5, 0.05),  # 👈 Y position is 0.3 (center is 0.5)
        bbox_transform=ax_legend.transAxes
    )

    # === Final adjustments ===
    plt.subplots_adjust(
        hspace=0.65,
        top=0.93,
        bottom=0.03,   # bottom sets the Y location of the Legend
        left=0.04,     # default is around 0.125
        right=0.98     # default is around 0.9
    )

    plt.savefig(output_path, dpi=300)
    print(f"✅ Plot saved to: {output_path}")

if __name__ == '__main__':
    main()









"""
import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from matplotlib.gridspec import GridSpec
from input_read_bua_results import *

def main():
    # === Config ===
    output_folder = path_dir_simulation_all_alternatives
    excel_path = os.path.join(output_folder, "energy_results_combined.xlsx")
    sheet_name = "KPIs"

    plots_folder = os.path.join(output_folder, "plots")
    os.makedirs(plots_folder, exist_ok=True)
    output_path = os.path.join(plots_folder, "net_energy_compensation_stack_column.png")

    # === Read Data (with lowercase-safe columns) ===
    df = pd.read_excel(excel_path, sheet_name=sheet_name)
    df.columns = df.columns.str.lower()
    df = df[["case", "scenario", "net energy compensation - total"]].copy()
    df.rename(columns={"net energy compensation - total": "comp"}, inplace=True)
    df["use"] = 1.0 - df["comp"]
    df["comp [%]"] = df["comp"] * 100
    df["use [%]"] = df["use"] * 100

    cases = df["case"].astype(str).tolist()
    scenarios = df["scenario"].astype(str).tolist()
    comp = df["comp [%]"]
    use = df["use [%]"]
    x = list(range(len(df)))

    # === Identify Case Transitions for Grouping ===
    case_transitions = [0]
    for i in range(1, len(cases)):
        if cases[i] != cases[i - 1]:
            case_transitions.append(i)
    case_transitions.append(len(cases))  # Add end marker

    # === Set up layout ===
    fig = plt.figure(figsize=(18, 14))
    gs = GridSpec(6, 1, height_ratios=[200, 1, 2.5, 1, 1.5, 4])  # plot, space, scenarios, space, cases, legend

    # === Bar chart ===
    ax_main = fig.add_subplot(gs[0, 0])
    ax_main.bar(x, comp, color="#08306B", edgecolor="black")
    ax_main.bar(x, use, bottom=comp, color="white", edgecolor="black")
    ax_main.set_ylim(0, 100)
    ax_main.set_ylabel("Percentage [%]", fontsize=18)
    ax_main.set_title("Net Energy Use and Compensation", fontsize=24, pad=20)
    ax_main.set_xticks([])
    ax_main.yaxis.grid(True, linestyle='--', alpha=0.5)

   # === Add vertical lines between groups ===
    for idx in case_transitions[1:-1]:  # skip 0 and end
        ax_main.axvline(idx - 0.5, color='gray', linestyle='--', linewidth=1)


    # === Optional: Add shaded background bands (uncomment below if preferred over lines) ===
    # for i in range(len(case_transitions) - 1):
    #     start = case_transitions[i]
    #     end = case_transitions[i + 1]
    #     if i % 2 == 0:
    #         ax_main.axvspan(start - 0.5, end - 0.5, color='gray', alpha=0.05)

    # === Manual Scenario Text ===
    ax_scenarios = fig.add_subplot(gs[2, 0], sharex=ax_main)
    ax_scenarios.set_xlim(ax_main.get_xlim())
    ax_scenarios.set_ylim(0, 1)
    ax_scenarios.axis("off")
    for i, txt in enumerate(scenarios):
        ax_scenarios.text(i, -22.5, txt, fontsize=12, rotation=90, ha='center', va='bottom')

    # === Manual Case Text (centered per group) ===
    ax_cases = fig.add_subplot(gs[4, 0], sharex=ax_main)
    ax_cases.set_xlim(ax_main.get_xlim())
    ax_cases.set_ylim(0, 1)
    ax_cases.axis("off")
    unique_cases = df["case"].unique()
    for case in unique_cases:
        case_indices = df[df["case"] == case].index.tolist()
        if not case_indices:
            continue
        middle_index = sum(case_indices) / len(case_indices)
        ax_cases.text(
            middle_index, -9.0, str(case),  # -9.0 sets the Y location of the Cases
            fontsize=14, rotation=0,
            ha='center', va='top'
        )

    # === Legend at the very bottom ===
    ax_legend = fig.add_subplot(gs[5, 0])
    ax_legend.axis("off")
    legend_elements = [
        Patch(facecolor="#08306B", edgecolor="black", label="Net energy compensation"),
        Patch(facecolor="white", edgecolor="black", label="Net energy use")
    ]
    ax_legend.legend(
        handles=legend_elements,
        loc='center',
        ncol=2,
        fontsize=18,
        frameon=False,
        bbox_to_anchor=(0.5, 0.05),  # 👈 Y position is 0.3 (center is 0.5)
        bbox_transform=ax_legend.transAxes
    )

    # === Final adjustments ===
    plt.subplots_adjust(
        hspace=0.65,
        top=0.93,
        bottom=0.03,   # bottom sets the Y location of the Legend
        left=0.04,     # default is around 0.125
        right=0.98     # default is around 0.9
    )

    plt.savefig(output_path, dpi=300)
    print(f"✅ Plot saved to: {output_path}")

if __name__ == '__main__':
    main()
"""
