import json
import pandas as pd
import os
from input_read_bua_results import *


def main():
    # === Set custom output directory ===
    # output_folder = r"C:\Users\YourName\Documents\EnergyResults"  # <<< CHANGE THIS PATH
    output_folder = path_dir_simulation_all_alternatives
    os.makedirs(output_folder, exist_ok=True)

    # === Load JSON ===
    # json_path = r"..\..\..\..\OneDrive - Technion\GH\Tanya\14\TestAllRuns_Pycharm\results.json"  # Adjust path if needed
    json_path = path_json_results_file
    with open(json_path, "r") as f:
        data = json.load(f)

    # === 1. Extract BES (building-level yearly energy) ===
    bes_records = []
    for case_name, case_data in data.items():
        bes = case_data.get("bes", {})
        for building_name, building_data in bes.items():
            record = {"case": case_name, "building": building_name}
            for end_use in ["heating", "cooling", "equipment", "lighting", "total"]:
                record[end_use] = building_data.get(end_use, {}).get("yearly", None)
            bes_records.append(record)

    df_bes = pd.DataFrame(bes_records)
    df_bes.to_csv(os.path.join(output_folder, "building_energy_results.csv"), index=False)
    df_bes.to_excel(os.path.join(output_folder, "building_energy_results.xlsx"), index=False)

    # === 2. Extract UBES (urban-level yearly energy) ===
    ubes_records = []
    for case_name, case_data in data.items():
        ubes = case_data.get("ubes", {})
        record = {"case": case_name}
        for end_use in ["heating", "cooling", "equipment", "lighting", "total"]:
            record[end_use] = ubes.get(end_use, {}).get("yearly", None)
        ubes_records.append(record)

    df_ubes = pd.DataFrame(ubes_records)
    df_ubes.to_csv(os.path.join(output_folder, "urban_energy_results.csv"), index=False)
    df_ubes.to_excel(os.path.join(output_folder, "urban_energy_results.xlsx"), index=False)

    # === 3. Extract KPIs ===
    kpi_records = []
    for case_name, case_data in data.items():
        kpis = case_data.get("kpis", {})
        record = {"case": case_name}

        # Flat KPIs
        flat_metrics = [
            ("eroi", "roof"), ("eroi", "facades"), ("eroi", "total"),
            ("net energy compensation", "roof"), ("net energy compensation", "facades"), ("net energy compensation", "total"),
            ("economical roi", "roof"), ("economical roi", "facades"), ("economical roi", "total"),
            ("net economical benefit [$]", "roof"), ("net economical benefit [$]", "facades"), ("net economical benefit [$]", "total"),
        ]
        for cat, subkey in flat_metrics:
            value = kpis.get(cat, {}).get(subkey, None)
            record[f"{cat} - {subkey}"] = value

        # Nested payback times & emissions
        nested_metrics = [
            "primary energy payback time [year]",
            "ghg emissions payback time [year]",
            "economical payback time [year]",
        ]
        for cat in nested_metrics:
            for subcat in ["profitability_threshold", "lifetime_investment"]:
                for zone in ["roof", "facades", "total"]:
                    key = f"{cat} - {subcat} - {zone}"
                    val = kpis.get(cat, {}).get(subcat, {}).get(zone, None)
                    record[key] = val

        # Emissions intensity
        for zone in ["roof", "facades", "total"]:
            key = f"ghg emissions intensity [kgCo2eq/kWh] - {zone}"
            record[key] = kpis.get("ghg emissions intensity [kgCo2eq/kWh]", {}).get(zone, None)

        # Harvested energy & benefit density
        for label, category in [
            ("harvested energy density [Kwh/m2]", "harvested energy density [Kwh/m2]"),
            ("net economical benefit density [$/m2]", "net economical benefit density [$/m2]"),
        ]:
            for zone_type in ["zone", "conditioned_apartment"]:
                for zone in ["roof", "facades", "total"]:
                    key = f"{label} - {zone_type} - {zone}"
                    record[key] = kpis.get(category, {}).get(zone_type, {}).get(zone, None)

        kpi_records.append(record)

    df_kpis = pd.DataFrame(kpi_records)
    df_kpis.to_csv(os.path.join(output_folder, "kpis_results.csv"), index=False)
    df_kpis.to_excel(os.path.join(output_folder, "kpis_results.xlsx"), index=False)

    print(f"✅ Export complete.\nFiles saved in: {output_folder}")


if __name__ == '__main__':
    main()
