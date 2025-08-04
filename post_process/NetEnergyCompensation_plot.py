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

    # === Read Data ===
    df = pd.read_excel(excel_path, sheet_name=sheet_name)
    df = df[["Case", "Scenario", "net energy compensation - total"]].copy()
    df.rename(columns={"net energy compensation - total": "Comp"}, inplace=True)
    df["Use"] = 1.0 - df["Comp"]
    df["Comp [%]"] = df["Comp"] * 100
    df["Use [%]"] = df["Use [%]"] = df["Use"] * 100

    cases = df["Case"].astype(str).tolist()
    scenarios = df["Scenario"].astype(str).tolist()
    comp = df["Comp [%]"]
    use = df["Use [%]"]
    x = list(range(len(df)))

    # === Set up layout ===
    fig = plt.figure(figsize=(16, 14))
    gs = GridSpec(6, 1, height_ratios=[240, 1, 2.5, 1, 1.5, 4])  # plot, space, scenario text, space, case text, legend

    # === Bar chart ===
    ax_main = fig.add_subplot(gs[0, 0])
    ax_main.bar(x, comp, color="#08306B", edgecolor="black")
    ax_main.bar(x, use, bottom=comp, color="white", edgecolor="black")
    ax_main.set_ylim(0, 100)
    ax_main.set_ylabel("Percentage [%]", fontsize=18)
    ax_main.set_title("Net Energy Use and Compensation", fontsize=24, pad=20)
    ax_main.set_xticks([])  # hide x-axis ticks

    # === Manual Scenario Text ===
    ax_scenarios = fig.add_subplot(gs[2, 0], sharex=ax_main)
    ax_scenarios.set_xlim(ax_main.get_xlim())
    ax_scenarios.set_ylim(0, 1)
    ax_scenarios.axis("off")
    # for i, txt in enumerate(scenarios):
    #     ax_scenarios.text(i, 0, txt, fontsize=12, rotation=90, ha='center', va='bottom')
    for i, txt in enumerate(scenarios):
        ax_scenarios.text(i, -20.5, txt, fontsize=12, rotation=90, ha='center', va='bottom')

    # === Manual Case Text ===
    ax_cases = fig.add_subplot(gs[4, 0], sharex=ax_main)
    ax_cases.set_xlim(ax_main.get_xlim())
    ax_cases.set_ylim(0, 1)
    ax_cases.axis("off")
    for i, txt in enumerate(cases):
        ax_cases.text(i, 0, txt, fontsize=14, rotation=0, ha='center', va='top')

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
        frameon=False
    )

    # === Final adjustments ===
    plt.subplots_adjust(hspace=0.65, top=0.93, bottom=0.03)
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
    # excel_path = r"./energy_results_combined.xlsx"  # Update if needed
    sheet_name = "KPIs"

    plots_folder = os.path.join(output_folder, "plots")
    os.makedirs(plots_folder, exist_ok=True)
    output_path = os.path.join(plots_folder, "net_energy_compensation_stack_column.png")
    # output_path = "./net_energy_stacked_plot.png"

    # === Read Data ===
    df = pd.read_excel(excel_path, sheet_name=sheet_name)
    df = df[["Case", "Scenario", "net energy compensation - total"]].copy()
    df.rename(columns={"net energy compensation - total": "Comp"}, inplace=True)
    df["Use"] = 1.0 - df["Comp"]

    # Convert to %
    df["Comp [%]"] = df["Comp"] * 100
    df["Use [%]"] = df["Use"] * 100

    # Create multi-index for x-axis (Case + Scenario)
    df["Case"] = df["Case"].astype(str)
    df["Scenario"] = df["Scenario"].astype(str)
    df["x_label"] = list(zip(df["Case"], df["Scenario"]))

    # === Plot ===
    fig = plt.figure(figsize=(16, 10))
    gs = GridSpec(10, 1, figure=fig)  # 9 rows for plot, 1 row for legend
    ax = fig.add_subplot(gs[:9, 0])   # main plot area

    x = range(len(df))
    comp = df["Comp [%]"]
    use = df["Use [%]"]

    bars1 = ax.bar(x, comp, color="#08306B", edgecolor="black")
    bars2 = ax.bar(x, use, bottom=comp, color="white", edgecolor="black")

    # Format axes
    ax.set_ylim(0, 100)
    ax.set_ylabel("Percentage [%]", fontsize=14)
    ax.set_title("Net Energy Use and Compensation", fontsize=16, pad=20)
    ax.set_xticks(x)
    ax.set_xticklabels([label[1] for label in df["x_label"]], rotation='vertical', fontsize=10)

    # === Case labels below Scenario ===
    case_labels = [label[0] for label in df["x_label"]]
    ax2 = ax.twiny()  # create a secondary x-axis for case labels
    ax2.set_xticks(x)
    ax2.set_xticklabels(case_labels, fontsize=10)
    ax2.set_xlim(ax.get_xlim())
    ax2.xaxis.set_ticks_position('bottom')
    ax2.xaxis.set_label_position('bottom')
    ax2.spines['bottom'].set_position(('outward', 60))  # move below the primary x-axis
    ax2.tick_params(axis='x', which='major', pad=10)

    # === Legend manually placed below ===
    legend_ax = fig.add_subplot(gs[9, 0])
    legend_ax.axis("off")
    legend_elements = [
        Patch(facecolor="#08306B", edgecolor="black", label="Net energy compensation"),
        Patch(facecolor="white", edgecolor="black", label="Net energy use")
    ]
    legend_ax.legend(
        handles=legend_elements,
        loc='center',
        ncol=2,
        fontsize=12,
        frameon=False
    )

    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    print(f"✅ Plot saved to: {output_path}")


if __name__ == '__main__':
    main()






import os
import pandas as pd
import matplotlib.pyplot as plt
from input_read_bua_results import *

def main():
    # === Paths ===
    output_folder = path_dir_simulation_all_alternatives
    excel_path = os.path.join(output_folder, "energy_results_combined.xlsx")
    print ('Excel path is', excel_path)
    plots_folder = os.path.join(output_folder, "plots")
    os.makedirs(plots_folder, exist_ok=True)
    filename = os.path.join(plots_folder, "net_energy_compensation_stack_column.png")

    # === Read data ===
    df = pd.read_excel(excel_path, sheet_name="KPIs")
    df = df[["Case", "Scenario", "net energy compensation - total"]].copy()
    df.rename(columns={"net energy compensation - total": "Net energy compensation"}, inplace=True)
    df["Net energy use"] = 1.0 - df["Net energy compensation"]

    # Convert to percentage
    df["Net energy compensation [%]"] = df["Net energy compensation"] * 100
    df["Net energy use [%]"] = df["Net energy use"] * 100

    # Sort for grouped display
    df.sort_values(by=["Case", "Scenario"], inplace=True)
    df.reset_index(drop=True, inplace=True)

    # === Plotting ===
    fig, ax = plt.subplots(figsize=(12, 6))

    labels = df["Scenario"]
    cases = df["Case"].unique()
    case_positions = []

    comp = df["Net energy compensation [%]"]
    use = df["Net energy use [%]"]

    # Bar plot
    bars1 = ax.bar(labels, comp, label="Net energy compensation [%]",
                   color="#08306B", edgecolor="black")
    bars2 = ax.bar(labels, use, bottom=comp, label="Net energy use [%]",
                   color="white", edgecolor="black")

    # Title and axis
    ax.set_title("Net Energy Compensation [%]", fontsize=16)
    ax.set_ylabel("%", fontsize=14)
    ax.set_ylim(0, 100)
    ax.tick_params(axis='x', rotation=45)

    # === Grouping X-axis by case ===
    xticks = list(range(len(df)))
    ax.set_xticks(xticks)
    ax.set_xticklabels(df["Scenario"], fontsize=9)

    # Add case group labels below x-axis
    prev_case = None
    start_idx = 0
    for idx, case in enumerate(df["Case"]):
        if case != prev_case and prev_case is not None:
            mid = (start_idx + idx - 1) / 2
            ax.text(mid, -10, prev_case, ha='center', va='top', fontsize=10, fontweight='bold')
            start_idx = idx
        prev_case = case
    # Draw last group label
    if prev_case is not None:
        mid = (start_idx + len(df) - 1) / 2
        ax.text(mid, -10, prev_case, ha='center', va='top', fontsize=10, fontweight='bold')

    # Extend bottom margin for group labels
    plt.subplots_adjust(bottom=0.25)

    # Grid and legend
    ax.grid(axis='y', linestyle='--', alpha=0.5)
    ax.legend(
        loc='upper center',
        bbox_to_anchor=(0.5, -0.20),
        ncol=2,
        frameon=True
    )

    # Save
    plt.tight_layout()
    plt.savefig(filename, dpi=300)
    plt.close()
    print(f"✅ Saved: {filename}")

if __name__ == '__main__':
    main()
"""







"""
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from input_read_bua_results import *


def main():
    output_folder = path_dir_simulation_all_alternatives
    excel_path = os.path.join(output_folder, "energy_results_combined.xlsx")
    plots_folder = os.path.join(output_folder, "plots")
    os.makedirs(plots_folder, exist_ok=True)

    plot_area = 7202.56  # <-- UPDATE if needed

    # === CONFIG ===
    filename = os.path.join(plots_folder, "net_energy_compensation_stack_column.png")

    # === Read data ===
    df = pd.read_excel(excel_path, sheet_name="KPIs")

    # === Clean & Prepare ===
    df = df[["Case", "Scenario", "net energy compensation - total"]].copy()
    df.rename(columns={"net energy compensation - total": "Net energy compensation"}, inplace=True)
    df["Net energy use"] = 1.0 - df["Net energy compensation"]

    # Convert to percentage
    df["Net energy compensation [%]"] = df["Net energy compensation"] * 100
    df["Net energy use [%]"] = df["Net energy use"] * 100

    # Create new label combining scenario and case (can modify for clarity)
    df["label"] = df["Scenario"] + "\n" + df["Case"]

    # Sort if needed (optional)
    df.sort_values(by=["Case", "Scenario"], inplace=True)

    # === Plot ===
    labels = df["label"]
    comp = df["Net energy compensation [%]"]
    use = df["Net energy use [%]"]

    fig, ax = plt.subplots(figsize=(12, 6))

    # Bottom: Net energy compensation (dark fill)
    bars1 = ax.bar(labels, comp, label="Net energy compensation [%]",
                   color="#08306B", edgecolor="black")

    # Top: Net energy use (white fill, black edge)
    bars2 = ax.bar(labels, use, bottom=comp, label="Net energy use [%]",
                   color="white", edgecolor="black")

    # Title and axis
    ax.set_title("Net Energy Compensation [%]", fontsize=16)
    ax.set_ylabel("%", fontsize=14)
    ax.set_ylim(0, 100)
    ax.tick_params(axis='x', rotation=45)

    # Grid and legend
    ax.grid(axis='y', linestyle='--', alpha=0.5)
    ax.legend(loc="upper right")

    plt.tight_layout()
    plt.savefig(filename, dpi=300)
    plt.show()

if __name__ == '__main__':
    main()
"""
