import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from input_read_bua_results import *

def main():
    # === CONFIG ===
    # output_folder = r"C:\Users\YourName\Documents\EnergyResults"  # <<< UPDATE this
    # output_folder = path_plot_results
    output_folder = path_dir_simulation_all_alternatives
    excel_path = os.path.join(output_folder, "energy_results_combined.xlsx")
    plots_folder = os.path.join(output_folder, "plots")
    os.makedirs(plots_folder, exist_ok=True)

    # print(path_plot_results)
    # print('output folder ', output_folder, ' plots folder ', plots_folder)

    # === Load Data ===
    df_bes = pd.read_excel(excel_path, sheet_name="Building_Energy")
    df_ubes = pd.read_excel(excel_path, sheet_name="Urban_Energy")
    df_kpis = pd.read_excel(excel_path, sheet_name="KPIs")

    # === Plot 1: Urban Energy Use Breakdown (stacked bar) ===
    plt.figure(figsize=(10, 6))
    df_plot = df_ubes.set_index("case")[["heating", "cooling", "equipment", "lighting"]]
    df_plot.plot(kind="bar", stacked=True)
    plt.ylabel("Energy Use [kWh]")
    plt.title("Urban Energy Use Breakdown by Case")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(os.path.join(plots_folder, "urban_energy_use_breakdown.png"))
    plt.close()

    # === Plot 2: Economical ROI by Case and Scenario ===
    plt.figure(figsize=(10, 6))
    sns.barplot(data=df_kpis, x="case", y="economical roi - total", hue="scenario")
    plt.xticks(rotation=45)
    plt.title("Economical ROI by Case and Scenario")
    plt.ylabel("ROI")
    plt.tight_layout()
    plt.savefig(os.path.join(plots_folder, "economical_roi_by_case_scenario.png"))
    plt.close()

    # === Plot 3: EROI vs Net Energy Compensation ===
    plt.figure(figsize=(10, 6))
    sns.scatterplot(
        data=df_kpis,
        x="net energy compensation - total",
        y="eroi - total",
        hue="scenario",
        style="case",
        s=100
    )
    plt.title("EROI vs Net Energy Compensation")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(os.path.join(plots_folder, "eroi_vs_net_energy_compensation.png"))
    plt.close()

    # === Plot 4: GHG Intensity vs GHG Emissions Payback Time ===
    plt.figure(figsize=(10, 6))
    sns.scatterplot(
        data=df_kpis,
        x="ghg emissions intensity [kgCo2eq/kWh] - total",
        y="ghg emissions payback time [year] - lifetime_investment - total",
        hue="scenario",
        style="case",
        s=100
    )
    plt.title("GHG Intensity vs Emissions Payback Time")
    plt.xlabel("GHG Emissions Intensity [kgCO₂eq/kWh]")
    plt.ylabel("GHG Payback Time [years]")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(os.path.join(plots_folder, "ghg_intensity_vs_emissions_payback.png"))
    plt.close()

    # === Plot 5: Harvested Energy Density by Case and Scenario ===
    plt.figure(figsize=(10, 6))
    sns.barplot(
        data=df_kpis,
        x="case",
        y="harvested energy density [Kwh/m2] - zone - total",
        hue="scenario"
    )
    plt.title("Harvested Energy Density [kWh/m²] by Case and Scenario")
    plt.ylabel("Harvested Energy [kWh/m²]")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(os.path.join(plots_folder, "harvested_energy_density_by_case_scenario.png"))
    plt.close()

    print(f"✅ All plots saved in: {plots_folder}")




if __name__ == '__main__':
    main()
