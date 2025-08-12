import json
import os
from pathlib import Path
from inputs import path_dir_simulation_all_alternatives

def get_minimal_radiation_for_kept_panel(path_simulation_folder):
    path_json = os.path.join(path_simulation_folder, "urban_canopy.json")
    # print('HERE ', path_json)

    # Check if the urban canopy json file exists
    if not os.path.isfile(path_json):
        raise ValueError(
            "The urban canopy json file does not exist, buildings need to be loaded before running the context selection.")
    # Read the json file
    with open(path_json, 'r') as json_file:
        urban_canopy_dict = json.load(json_file)

    building_id_list = [building_id for building_id in urban_canopy_dict["buildings"].keys() if
                        (urban_canopy_dict["buildings"][building_id]["type"] == "BuildingModeled" and
                         (urban_canopy_dict["buildings"][building_id]["solar_radiation_and_bipv"][
                              "roof_annual_panel_irradiance_list"] is not None
                          or urban_canopy_dict["buildings"][building_id]["solar_radiation_and_bipv"][
                              "facades_annual_panel_irradiance_list"] is not None))]
    # Init
    roof_annual_solar_irr_list = []
    facades_annual_solar_irr_list = []

    for building_id in building_id_list:
        # Roof
        if urban_canopy_dict["buildings"][building_id]["solar_radiation_and_bipv"][
            "roof_annual_panel_irradiance_list"] is not None:
            annual_solar_irr = urban_canopy_dict["buildings"][building_id]["solar_radiation_and_bipv"][
                "roof_annual_panel_irradiance_list"]
            if urban_canopy_dict["buildings"][building_id]["solar_radiation_and_bipv"][
                "roof_panel_mesh_index_list"] is not None:
                annual_solar_irr = [
                    annual_solar_irr[i] if i in urban_canopy_dict["buildings"][building_id][
                        "solar_radiation_and_bipv"][
                        "roof_panel_mesh_index_list"] else 0 for i, _ in enumerate(annual_solar_irr)]
            roof_annual_solar_irr_list += annual_solar_irr

        # Facade
        if urban_canopy_dict["buildings"][building_id]["solar_radiation_and_bipv"][
            "facades_annual_panel_irradiance_list"] is not None:
            annual_solar_irr = urban_canopy_dict["buildings"][building_id]["solar_radiation_and_bipv"][
                "facades_annual_panel_irradiance_list"]
            if urban_canopy_dict["buildings"][building_id]["solar_radiation_and_bipv"][
                "facades_panel_mesh_index_list"] is not None:
                annual_solar_irr = [
                    annual_solar_irr[i] if i in urban_canopy_dict["buildings"][building_id][
                        "solar_radiation_and_bipv"][
                        "facades_panel_mesh_index_list"] else 0 for i, _ in enumerate(annual_solar_irr)]
            facades_annual_solar_irr_list += annual_solar_irr


    # Filter values greater than min_val
    min_val = 1
    filtered_roof_annual_solar_irr_list = [value for value in roof_annual_solar_irr_list if value > min_val]
    filtered_facades_annual_solar_irr_list = [value for value in facades_annual_solar_irr_list if value > min_val]

    return min(min(filtered_roof_annual_solar_irr_list), min(filtered_facades_annual_solar_irr_list))

def main():
    path = Path(path_dir_simulation_all_alternatives)

    # Collect results
    results = {}

    # Loop through each subfolder and call the function
    for folder in path.iterdir():
        if folder.is_dir():
            minRad = get_minimal_radiation_for_kept_panel(folder)
            results[folder.name] = {
                "minRad": minRad
            }

    # Save to JSON
    output_file = path / "minimal_radiation_results.json"
    with open(output_file, "w") as f:
        json.dump(results, f, indent=4)

    print(f"Results saved to {output_file}")


if __name__ == "__main__":
    main()
