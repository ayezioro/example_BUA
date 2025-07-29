from bua.simulation_steps import *

from bua.building import BuildingModeled

import json
from typing import Union


def update_json(file_path: str, new_data: dict) -> None:
    """
    Update a JSON file (dictionary format) with new key-value pairs.

    :param file_path: Path to the JSON file.
    :param new_data: Dictionary of new data to add or update.
    """
    try:
        # Load existing JSON data
        with open(file_path, "r") as file:
            data = json.load(file)

        if not isinstance(data, dict):
            raise ValueError("Top-level JSON structure must be a dictionary.")

        # Update the dictionary with new data
        data.update(new_data)

        # Save it back
        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)

        print("JSON file updated successfully.")

    except FileNotFoundError:
        # If the file doesn't exist, create it
        with open(file_path, "w") as file:
            json.dump(new_data, file, indent=4)
        print("File not found. Created new JSON file.")

    except Exception as e:
        print(f"Error updating JSON file: {e}")


def extract_results(path_simulation_folder, path_json_results_file):
    """

    :return:
    """
    # Initialize urban canopy object
    urban_canopy_obj = SimulationCommonMethods.create_or_load_urban_canopy_object(
        path_simulation_folder=path_simulation_folder
    )

    name_simulation_folder = path_simulation_folder.split("\\")[-1]

    bes_dict = {}

    for building_id, building_obj in urban_canopy_obj.building_dict.items():
        if isinstance(building_obj, BuildingModeled) and building_obj.is_target:
            bes_dict[building_id] = building_obj.bes_obj.to_dict()["bes_results_dict"]

    result_dict = {
        "alternative_name": name_simulation_folder,
        "bes": bes_dict,
        "ubes": urban_canopy_obj.ubes_obj.to_dict()["ubes_results_dict"],
        # to access value result_dict["ubes"]["heating"]["yearly"]
        "kpis": {
            bipv_scenario_id: urban_canopy_obj.bipv_scenario_dict[
                bipv_scenario_id
            ].urban_canopy_bipv_kpis_obj.to_dict()["kpis"]
            for bipv_scenario_id in urban_canopy_obj.bipv_scenario_dict.keys()
        },
    }

    update_json(
        file_path=path_json_results_file, new_data={name_simulation_folder: result_dict}
    )

    return
