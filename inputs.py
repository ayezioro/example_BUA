import os

# Directory with the hbjson inputs
path_dir_with_hbjson_alternatives = r"D:\trash\in\hbjson"
list_hbjson_folders = [
    os.path.join(path_dir_with_hbjson_alternatives, dir_name)
    for dir_name in os.listdir(path_dir_with_hbjson_alternatives)
    if os.path.isdir(os.path.join(path_dir_with_hbjson_alternatives, dir_name))
]
# Path to the context file
# path_brep_context = os.path.join(
#     path_dir_with_hbjson_alternatives, "Context_from_brep.json"
# )
path_brep_context = None

# Directory where all the simulation will be run
path_dir_simulation_all_alternatives = (
    r"D:\trash\res"
)
# Path to the JSON results file
path_json_results_file = os.path.join(
    path_dir_simulation_all_alternatives, "results.json"
)
# Path to the EPW weather file
path_epw = r"D:\trash\in\IS_5280_A_Tel_Aviv.epw"
# Coefficient of Performance for heating and cooling
cop_heating = 3
cop_cooling = 3
# Plot area in square meters
zone_area = 7202.56  # Plot Area


# Flags for the simulation, DO NOT CHANGE THESE UNLESS YOU KNOW WHAT YOU ARE DOING
(
    run_load_buildings,
    run_mesh_generation,
    run_context_filter,
    run_ubes,
    run_radiation_simulation,
    run_bipv_simulation,
    run_results_extraction,
) = (False, False, False, False, False, False, False)

run_load_buildings = True
run_mesh_generation = True
run_context_filter = True
run_ubes = True
run_radiation_simulation = True
run_bipv_simulation = True
run_results_extraction = True

# Number of parallel processes to run
num_workers_processes = 20
num_worker_threads = 30

# Inputs Mesh generation
bipv_on_facades = True
bipv_on_roof = True
roof_grid_size_x = 2.05
roof_grid_size_y = 1.0
facades_grid_size_x = 1.05
facades_grid_size_y = 1.05
offset_dist = 0.1

# Context filter inputs
min_vf_criterion = 0.001
number_of_rays = 9
consider_windows = False
keep_discarded_faces = False


# BIPV scenarions
bipv_scenarios = {
    "BIPV_Scenario_1": {
        "minimum_panel_eroi": 1.5,  # [1.2:2.5]
        "minimum_economic_roi": 1.1,  # [1.1:1.4 for mortar. x.x for stone, y.y for metal]
        "start_year": 2024,
        "end_year": 2084,
        "roof_id_pv_tech":"mitrex_roof c-Si M390-A1F 2025",
        "facades_id_pv_tech":"mitrex_facades c-Si Solar Siding 350W - Dove Grey china 2025_1.0x1.0",
        "roof_transport_id":"China-Israel 22kg",
        "facades_transport_id":"China-Israel 9.5kg",
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
        "roof_id_pv_tech": "mitrex_roof c-Si M390-A1F 2025",
        "facades_id_pv_tech": "mitrex_facades c-Si Solar Siding 350W - Dove Grey china 2025_1.0x1.0",
        "roof_transport_id": "China-Israel 22kg",
        "facades_transport_id": "China-Israel 9.5kg",
        "replacement_scenario": "replace_all_panels_every_X_years",
        "panel_replacement_min_age": 20,  # [20:30]
        "replacement_frequency_in_years": 5,  # [5:10]
        "infrastructure_replacement_last_year": 40,  # [40:50]
    },
}
