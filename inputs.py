import os

# Directory with the hbjson inputs
path_dir_with_hbjson_alternatives = r""
list_hbjson_folders = [
    os.path.join(path_dir_with_hbjson_alternatives, dir_name)
    for dir_name in os.listdir(path_dir_with_hbjson_alternatives)
    if os.path.isdir(os.path.join(path_dir_with_hbjson_alternatives, dir_name))
]
# Path to the context file
path_brep_context = os.path.join(
    path_dir_with_hbjson_alternatives, "Context_from_brep.json"
)
# Directory where all the simulation will be run
path_dir_simulation_all_alternatives = (
    r"C:\WorkingFolder\BUA_Python\14\TestAllRuns_Pycharm"
)
# Path to the JSON results file
path_json_results_file = os.path.join(
    path_dir_simulation_all_alternatives, "results.json"
)
# Path to the EPW weather file
path_epw = r"C:\IsraelWeatheFiles_2007-2021_WindStandarized\ISR_TA_Tel.Aviv-Sde.Dov_.AP_.401762_TMYx.2007-2021_WindStandardized_Modified IMS.epw"
# Coefficient of Performance for heating and cooling
cop_heating = 3
cop_cooling = 3
# Plot area in square meters
zone_area = 7202.56  # Plot Area


# Flags for the simulation, DO NOT CHANGE THESE UNLESS YOU KNOW WHAT YOU ARE DOING
run_load_buildings = True
run_mesh_generation = True
run_context_filter = True
run_ubes = True
run_radiation_simulation = True
run_bipv_simulation = True
run_results_extraction = True

# BIPV scenarions


scenarios_bipv = {
    "BIPV_Scenario_1": {
        "minimum_panel_eroi": 1.5,  # [1.2:2.5]
        "minimum_economic_roi": 1.1,  # [1.1:1.4 for mortar. x.x for stone, y.y for metal]
        "start_year": 2024,
        "end_year": 2084,
        "replacement_scenario": "replace_failed_panels_every_X_years",
        "panel_replacement_min_age": 20,  # [20:30]
        "replacement_frequency_in_years": 5,  # [5:10]
        "infrastructure_replacement_last_year": 40,  # [40:50]
    },
    "BIPV_Scenario_2": {
        "minimum_panel_eroi": 1.5,  # [1.2:2.5]
        "minimum_economic_roi": 1.1,  # [1.1:1.4 for mortar. x.x for stone, y.y for metal]
        "start_year": 2024,
        "end_year": 2084,
        "replacement_scenario": "replace_all_panels_every_X_years",
        "panel_replacement_min_age": 20,  # [20:30]
        "replacement_frequency_in_years": 5,  # [5:10]
        "infrastructure_replacement_last_year": 40,  # [40:50]
    },
}
