import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from input_read_bua_results import *

# === Set font globally ===
plt.rcParams['font.family'] = 'Calibri'  # Can also use 'Arial', 'Times New Roman', etc.

def cm_to_inches(w_cm, h_cm):
    return (w_cm / 2.54, h_cm / 2.54)

def plot_scatter(data, x_col, y_col, hue_col, style_col, title, xlabel, ylabel, filename,
                 legend_title="Legend", legend_loc="best", size=220, palette="Set2",
                 xlim=None, ylim=None, figsize_cm=(20, 12), dpi=300):

    plt.figure(figsize=cm_to_inches(figsize_cm[0], figsize_cm[1]))  # A5 landscape size

    sns.scatterplot(
        data=data,
        x=x_col,
        y=y_col,
        hue=hue_col,
        style=style_col,
        s=size,
        palette=palette,
        edgecolor="black"
    )

    # Title and labels
    plt.title(title, fontsize=32)
    plt.xlabel(xlabel, fontsize=28)
    plt.ylabel(ylabel, fontsize=28)
    # plt.legend(frameon=False)

    # Axis ticks
    plt.xticks(fontsize=18)
    plt.yticks(fontsize=18)

    # Axis limits
    if xlim:
        plt.xlim(xlim)
    if ylim:
        plt.ylim(ylim)

    # Grid style
    plt.grid(True, color='lightgray', linestyle='--', linewidth=1)
    # linestyle: '--', '-.', ':', or '-' (solid)
    # Legend customization
    legend = plt.legend(
        title=legend_title,
        loc=legend_loc,
        fontsize=12,
        title_fontsize=13,
        prop={'size': 14},
        labelspacing=1.0,
        borderpad=1.0
    )

    # legend.get_frame().set_facecolor('white')   # solid white background
    legend.get_frame().set_facecolor('none')
    # legend.get_frame().set_edgecolor('none')
    legend.get_frame().set_edgecolor('gray')    # gray border
    legend.get_frame().set_linewidth(1)

    # === Fix: Set consistent marker sizes in legend ===
    for handle in legend.legend_handles:
        if hasattr(handle, "set_sizes"):
            handle.set_sizes([size])

    # Final save and close
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(filename, dpi=dpi)
    print(f"✅ Saved: {filename}")
    plt.close()

def main():
    output_folder = path_dir_simulation_all_alternatives
    excel_path = os.path.join(output_folder, "energy_results_combined.xlsx")
    plots_folder = os.path.join(output_folder, "plots")
    os.makedirs(plots_folder, exist_ok=True)

    plot_area = 7202.56  # <-- UPDATE if needed

    df_kpis = pd.read_excel(excel_path, sheet_name="KPIs")
    df_ubes = pd.read_excel(excel_path, sheet_name="Urban_Energy")

    # === Custom Scatter Plot: EROI vs Net Energy Compensation ===
    plot_scatter(
        data=df_kpis,
        x_col="net energy compensation - total",
        y_col="eroi - total",
        hue_col="Scenario",
        style_col="Case",
        title="EROI vs Net Energy Compensation",
        xlabel="Net Energy Compensation [kWh]",
        ylabel="EROI",
        filename=os.path.join(plots_folder, "custom_eroi_vs_net_energy.png"),
        legend_title="Scenario",
        legend_loc="lower right",
        xlim=(0.16, 0.26),
        ylim=(2.8, 3.5),
        figsize_cm=(42, 28),   # A5 landscape
        dpi=300
    )

    print("✅ Scatter plot with axis bounds saved.")

if __name__ == '__main__':
    main()

