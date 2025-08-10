"""Read the annual solar irradiance results from the json file of the urban canopy.
    Inputs:
        path_simulation_folder_: Path to the folder
        building_id_list_: list of ints: list of buildings we want to read the results
        kept_panel_only_ : Set to True if we want to read the results for the kept panels only.
            This option is only available after the bipv simulation.
        _run: Plug in a boolean toggle to run the component and read the results
    Output:
        report: report
        roof_annual_irradiance_tree: Tree of the annual irradiance for the roof
        facades_annual_irradiance_tree: Tree of the annual irradiance for the facades"""


import json
import os


# Path to the urban canopy json file
path_json = os.path.join(path_simulation_folder, "urban_canopy.json")

# Check if the urban canopy json file exists
if not os.path.isfile(path_json):
    raise ValueError(
        "The urban canopy json file does not exist, buildings need to be loaded before running the context selection.")
# Read the json file
with open(path_json, 'r') as json_file:
    urban_canopy_dict = json.load(json_file)

building_id_list_ = []
# add the id of the buildings that have been run if no list is provided
building_id_list_ = [building_id for building_id in urban_canopy_dict["buildings"].keys() if
                     (urban_canopy_dict["buildings"][building_id]["type"] == "BuildingModeled" and
                      (urban_canopy_dict["buildings"][building_id]["solar_radiation_and_bipv"]["roof_annual_panel_irradiance_list"] is not None
                       or urban_canopy_dict["buildings"][building_id]["solar_radiation_and_bipv"]["facades_annual_panel_irradiance_list"] is not None))]

# Init
roof_annual_solar_irr_list, facades_annual_solar_irr_list = [], []

for building_id in building_id_list_:
    # Roof
    if urban_canopy_dict["buildings"][building_id]["solar_radiation_and_bipv"][
        "roof_annual_panel_irradiance_list"] is not None:
        annual_solar_irr = urban_canopy_dict["buildings"][building_id]["solar_radiation_and_bipv"][
            "roof_annual_panel_irradiance_list"]
        if kept_panel_only_ and urban_canopy_dict["buildings"][building_id]["solar_radiation_and_bipv"][
            "roof_panel_mesh_index_list"] is not None:
            annual_solar_irr = [
                annual_solar_irr[i] if i in urban_canopy_dict["buildings"][building_id]["solar_radiation_and_bipv"][
                    "roof_panel_mesh_index_list"] else 0 for i, _ in enumerate(annual_solar_irr)]
        roof_annual_solar_irr_list.append(annual_solar_irr)
    else:
        roof_annual_solar_irr_list.append([])
    # Facade
    if urban_canopy_dict["buildings"][building_id]["solar_radiation_and_bipv"][
        "facades_annual_panel_irradiance_list"] is not None:
        annual_solar_irr = urban_canopy_dict["buildings"][building_id]["solar_radiation_and_bipv"][
            "facades_annual_panel_irradiance_list"]
        if kept_panel_only_ and urban_canopy_dict["buildings"][building_id]["solar_radiation_and_bipv"][
            "facades_panel_mesh_index_list"] is not None:
            annual_solar_irr = [
                annual_solar_irr[i] if i in urban_canopy_dict["buildings"][building_id]["solar_radiation_and_bipv"][
                    "facades_panel_mesh_index_list"] else 0 for i, _ in enumerate(annual_solar_irr)]
        facades_annual_solar_irr_list.append(annual_solar_irr)
    else:
        facades_annual_solar_irr_list.append([])

# min_roof_irrad = min(roof_annual_solar_irr_list)
# min_facd_irrad = min(facades_annual_solar_irr_list)
#
if roof_annual_solar_irr_list or facades_annual_solar_irr_list:
    min_irrad_value = min(*roof_annual_solar_irr_list, *facades_annual_solar_irr_list)
else:
    min_irrad_value = None  # or raise an error or define default behavior

if not os.path.isfile(path_json):
    print("the json file of the urban canopy does not exist")
