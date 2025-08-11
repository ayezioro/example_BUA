import os

# Directory with the hbjson inputs
# path_dir_with_hbjson_alternatives = r"C:\Users\User\OneDrive - Technion\GH\Tanya\14\TRASHHHHHH_New-Test"
# path_dir_with_hbjson_alternatives = r"C:\Users\User\OneDrive - Technion\GH\Tanya\14\TRASHHHHHH"
path_dir_with_hbjson_alternatives = r"C:\Users\User\OneDrive - Technion\GH\Tanya\14\Alternatives_JSONs"
list_hbjson_folders = [
    os.path.join(path_dir_with_hbjson_alternatives, dir_name)
    for dir_name in os.listdir(path_dir_with_hbjson_alternatives)
    if os.path.isdir(os.path.join(path_dir_with_hbjson_alternatives, dir_name))
]
# Path to the context file
path_brep_context = os.path.join(
    path_dir_with_hbjson_alternatives, r"C:\Users\User\OneDrive - Technion\GH\Tanya\14\Alternatives_JSONs\Context_from_brep.json"
)
# path_brep_context = None

# Directory where all the simulation will be run
path_dir_simulation_all_alternatives = (
    # r"C:\WorkingFolder\BUA_Python\14\TestNewVersion"
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
# num_workers_processes = 1 # In case the threads doesn't work

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
    "BIPV_Scenario_1_prma20_rfiy5_irly40": {
        "minimum_panel_eroi": 1.5,  # [1.2:2.5]
        "minimum_economic_roi": 1.1,  # [1.1:1.4 for mortar. x.x for stone, y.y for metal]
        "start_year": 2024,
        "end_year": 2084,
        "roof_id_pv_tech":"mitrex_roof c-Si M390-A1F baseline 2025",
        "facades_id_pv_tech":"mitrex_facades c-Si Solar Siding 350W - Dove Grey china 2025_1.0x1.0",
        "roof_transport_id":"China-Israel 22kg",
        "facades_transport_id":"China-Israel 9.5kg",
        "replacement_scenario": "replace_failed_panels_every_X_years",
        "panel_replacement_min_age": 20,  # [20:30]
        "replacement_frequency_in_years": 5,  # [5:10]
        "infrastructure_replacement_last_year": 40,  # [40:50]
    },
    "BIPV_Scenario_2_prma30_rfiy10_irly50": {
        "minimum_panel_eroi": 1.5,  # [1.2:2.5]
        "minimum_economic_roi": 1.1,  # [1.1:1.4 for mortar. x.x for stone, y.y for metal]
        "start_year": 2024,
        "end_year": 2084,
        "roof_id_pv_tech": "mitrex_roof c-Si M390-A1F baseline 2025",
        "facades_id_pv_tech": "mitrex_facades c-Si Solar Siding 350W - Dove Grey china 2025_1.0x1.0",
        "roof_transport_id": "China-Israel 22kg",
        "facades_transport_id": "China-Israel 9.5kg",
        "replacement_scenario": "replace_all_panels_every_X_years",
        "panel_replacement_min_age": 30,  # [20:30]
        "replacement_frequency_in_years": 10,  # [5:10]
        "infrastructure_replacement_last_year": 50,  # [40:50]
    },
    "BIPV_Scenario_3_eroi_1.1": {
        "minimum_panel_eroi": 1.1,  # [1.2:2.5] - 1.1 to encourage more PV panels
        "minimum_economic_roi": 1.1,  # [1.1:1.4 for mortar. x.x for stone, y.y for metal]
        "start_year": 2024,
        "end_year": 2084,
        "roof_id_pv_tech":"mitrex_roof c-Si M390-A1F baseline 2025",
        "facades_id_pv_tech":"mitrex_facades c-Si Solar Siding 350W - Dove Grey china 2025_1.0x1.0",
        "roof_transport_id":"China-Israel 22kg",
        "facades_transport_id":"China-Israel 9.5kg",
        "replacement_scenario": "replace_failed_panels_every_X_years",
        "panel_replacement_min_age": 20,  # [20:30]
        "replacement_frequency_in_years": 5,  # [5:10]
        "infrastructure_replacement_last_year": 40,  # [40:50]
    },
    "BIPV_Scenario_4_SubstFacMat_METAL-405USm2": {
        "minimum_panel_eroi": 1.1,  # [1.2:2.5] - 1.1 to encourage more PV panels
        "minimum_economic_roi": 1.1,  # [1.1:1.4 for mortar. x.x for stone, y.y for metal]
        "start_year": 2024,
        "end_year": 2084,
        "roof_id_pv_tech":"mitrex_roof c-Si M390-A1F baseline 2025",
        "facades_id_pv_tech":"mitrex_facades c-Si Solar Siding 350W - Dove Grey china 2025_1.0x1.0_SubstFacMat_METAL-405USm2",
        "roof_transport_id":"China-Israel 22kg",
        "facades_transport_id":"China-Israel 9.5kg",
        "replacement_scenario": "replace_failed_panels_every_X_years",
        "panel_replacement_min_age": 20,  # [20:30]
        "replacement_frequency_in_years": 5,  # [5:10]
        "infrastructure_replacement_last_year": 40,  # [40:50]
    },
    "BIPV_Scenario_5_conservative substituted mat": {
        "minimum_panel_eroi": 1.5,  # [1.2:2.5] - 1.1 to encourage more PV panels
        "minimum_economic_roi": 1.1,  # [1.1:1.4 for mortar. x.x for stone, y.y for metal]
        "start_year": 2024,
        "end_year": 2084,
        "roof_id_pv_tech":"mitrex_roof c-Si M390-A1F baseline 2025",
        "facades_id_pv_tech":"mitrex_facades c-Si Solar Siding 350W - Dove Grey china 2025_1.0x1.0 conservative substituted mat",
        "roof_transport_id":"China-Israel 22kg",
        "facades_transport_id":"China-Israel 9.5kg",
        "replacement_scenario": "replace_failed_panels_every_X_years",
        "panel_replacement_min_age": 20,  # [20:30]
        "replacement_frequency_in_years": 5,  # [5:10]
        "infrastructure_replacement_last_year": 40,  # [40:50]
    },
    "BIPV_Scenario_6_optimistic substituted mat": {
        "minimum_panel_eroi": 1.5,  # [1.2:2.5] - 1.1 to encourage more PV panels
        "minimum_economic_roi": 1.1,  # [1.1:1.4 for mortar. x.x for stone, y.y for metal]
        "start_year": 2024,
        "end_year": 2084,
        "roof_id_pv_tech":"mitrex_roof c-Si M390-A1F baseline 2025",
        "facades_id_pv_tech":"mitrex_facades c-Si Solar Siding 350W - Dove Grey china 2025_1.0x1.0 optimistic substituted mat",
        "roof_transport_id":"China-Israel 22kg",
        "facades_transport_id":"China-Israel 9.5kg",
        "replacement_scenario": "replace_failed_panels_every_X_years",
        "panel_replacement_min_age": 20,  # [20:30]
        "replacement_frequency_in_years": 5,  # [5:10]
        "infrastructure_replacement_last_year": 40,  # [40:50]
    },
    "BIPV_Scenario_7_Fibercement_USD180": {
        "minimum_panel_eroi": 1.5,  # [1.2:2.5]
        "minimum_economic_roi": 1.1,  # [1.1:1.4 for mortar. x.x for stone, y.y for metal]
        "start_year": 2024,
        "end_year": 2084,
        "roof_id_pv_tech":"mitrex_roof c-Si M390-A1F baseline 2025",
        "facades_id_pv_tech":"mitrex_facades c-Si Solar Siding 350W - Dove Grey china 2025_1.0x1.0",
        "roof_transport_id":"China-Israel 22kg",
        "facades_transport_id":"China-Israel 9.5kg",
        "replacement_scenario": "replace_failed_panels_every_X_years",
        "panel_replacement_min_age": 20,  # [20:30]
        "replacement_frequency_in_years": 5,  # [5:10]
        "infrastructure_replacement_last_year": 40,  # [40:50]
    },
    "BIPV_Scenario_8_Fibercement_USD180_eroi_1.1": {
        "minimum_panel_eroi": 1.1,  # [1.2:2.5]
        "minimum_economic_roi": 1.1,  # [1.1:1.4 for mortar. x.x for stone, y.y for metal]
        "start_year": 2024,
        "end_year": 2084,
        "roof_id_pv_tech":"mitrex_roof c-Si M390-A1F baseline 2025",
        "facades_id_pv_tech":"mitrex_facades c-Si Solar Siding 350W - Dove Grey china 2025_1.0x1.0",
        "roof_transport_id":"China-Israel 22kg",
        "facades_transport_id":"China-Israel 9.5kg",
        "replacement_scenario": "replace_failed_panels_every_X_years",
        "panel_replacement_min_age": 20,  # [20:30]
        "replacement_frequency_in_years": 5,  # [5:10]
        "infrastructure_replacement_last_year": 40,  # [40:50]
    },
    "BIPV_Scenario_9_SubstFacMat_METAL-405USm2_eroi_1.5": {
        "minimum_panel_eroi": 1.5,  # [1.2:2.5] - 1.1 to encourage more PV panels
        "minimum_economic_roi": 1.1,  # [1.1:1.4 for mortar. x.x for stone, y.y for metal]
        "start_year": 2024,
        "end_year": 2084,
        "roof_id_pv_tech":"mitrex_roof c-Si M390-A1F baseline 2025",
        "facades_id_pv_tech":"mitrex_facades c-Si Solar Siding 350W - Dove Grey china 2025_1.0x1.0_SubstFacMat_METAL-405USm2",
        "roof_transport_id":"China-Israel 22kg",
        "facades_transport_id":"China-Israel 9.5kg",
        "replacement_scenario": "replace_failed_panels_every_X_years",
        "panel_replacement_min_age": 20,  # [20:30]
        "replacement_frequency_in_years": 5,  # [5:10]
        "infrastructure_replacement_last_year": 40,  # [40:50]
    },
    # "BIPV_Scenario_7_SubstFacMat_STONE-619USm2": {
    #     "minimum_panel_eroi": 1.1,  # [1.2:2.5] - 1.1 to encourage more PV panels
    #     "minimum_economic_roi": 1.1,  # [1.1:1.4 for mortar. x.x for stone, y.y for metal]
    #     "start_year": 2024,
    #     "end_year": 2084,
    #     "roof_id_pv_tech":"mitrex_roof c-Si M390-A1F baseline 2025",
    #     "facades_id_pv_tech":"mitrex_facades c-Si Solar Siding 350W - Dove Grey china 2025_1.0x1.0_SubstFacMat_STONE-619USm2",
    #     "roof_transport_id":"China-Israel 22kg",
    #     "facades_transport_id":"China-Israel 9.5kg",
    #     "replacement_scenario": "replace_failed_panels_every_X_years",
    #     "panel_replacement_min_age": 20,  # [20:30]
    #     "replacement_frequency_in_years": 5,  # [5:10]
    #     "infrastructure_replacement_last_year": 40,  # [40:50]
    # },
}
