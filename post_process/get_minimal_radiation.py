import json
import os


def get_minimal_radiation_for_kept_panel(path_simulation_folder):
    path_json = os.path.join(path_simulation_folder, "urban_canopy.json")

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

    return min(min(roof_annual_solar_irr_list), min(facades_annual_solar_irr_list))
