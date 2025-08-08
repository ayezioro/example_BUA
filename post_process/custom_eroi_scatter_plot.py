import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from input_read_bua_results import *

# === Set font globally ===
plt.rcParams['font.family'] = 'Calibri'  # Or: 'Arial', 'Times New Roman'

def cm_to_inches(w_cm, h_cm):
    return (w_cm / 2.54, h_cm / 2.54)

def plot_scatter(data, x_col, y_col, hue_col, style_col, title, xlabel, ylabel, filename,
                 legend_title="Legend", size=180, palette="Set2",
                 xlim=None, ylim=None, figsize_cm=(50, 28), dpi=300):

    fig, ax = plt.subplots(figsize=cm_to_inches(figsize_cm[0], figsize_cm[1]))

    sns.scatterplot(
        data=data,
        x=x_col,
        y=y_col,
        hue=hue_col,
        style=style_col,
        s=size,
        palette=palette,
        edgecolor="black",
        ax=ax
    )

    # Titles and labels
    ax.set_title(title, fontsize=32)
    ax.set_xlabel(xlabel, fontsize=28)
    ax.set_ylabel(ylabel, fontsize=28)

    # Axis ticks
    ax.tick_params(axis='both', labelsize=18)

    # Axis limits
    if xlim:
        ax.set_xlim(xlim)
    if ylim:
        ax.set_ylim(ylim)

    # Grid style
    ax.grid(True, color='lightgray', linestyle='--', linewidth=1)

    # === Legend outside to the right ===
    legend = ax.legend(
        title=legend_title,
        loc="center left",
        bbox_to_anchor=(1.02, 0.5),  # Outside to the right, centered vertically
        fontsize=12,
        title_fontsize=14,
        borderpad=1.0,
        labelspacing=1.0,
        frameon=True
    )
    legend.get_frame().set_facecolor('none')
    legend.get_frame().set_edgecolor('gray')
    legend.get_frame().set_linewidth(1)

    # === Ensure consistent marker size in legend ===
    for handle in legend.legend_handles:
        if hasattr(handle, "set_sizes"):
            handle.set_sizes([size * 0.5])  # 👈 Reduce legend size

    # Final save
    plt.tight_layout()
    plt.savefig(filename, dpi=dpi, bbox_inches='tight')  # ensure legend is included
    print(f"✅ Saved: {filename}")
    plt.close()

def main():
    output_folder = path_dir_simulation_all_alternatives
    excel_path = os.path.join(output_folder, "energy_results_combined.xlsx")
    plots_folder = os.path.join(output_folder, "plots")
    os.makedirs(plots_folder, exist_ok=True)

    plot_area = 7202.56  # <-- update if needed

    # === Read and normalize column names ===
    df_kpis = pd.read_excel(excel_path, sheet_name="KPIs")
    df_kpis.columns = df_kpis.columns.str.lower()

    df_ubes = pd.read_excel(excel_path, sheet_name="Urban_Energy")
    df_ubes.columns = df_ubes.columns.str.lower()

    # === Scatter Plot: EROI vs Net Energy Compensation ===
    plot_scatter(
        data=df_kpis,
        x_col="net energy compensation - total",
        y_col="eroi - total",
        hue_col="scenario",          # <-- lowercase-safe
        style_col="case",            # <-- lowercase-safe
        title="EROI vs Net Energy Compensation",
        xlabel="Net Energy Compensation [kWh]",
        ylabel="EROI",
        filename=os.path.join(plots_folder, "custom_eroi_vs_net_energy.png"),
        legend_title="Scenario",
        xlim=(0.16, 0.26),
        ylim=(2.8, 3.5),
        figsize_cm=(50, 40),
        dpi=300
    )

    print("✅ Scatter plot with external legend saved.")

if __name__ == '__main__':
    main()
