"""
Inputs for the simulation
"""

import os

# Simulation folder
path_simulation_folder = r"D:\Elie\PhD\Sim_ext_paper\\Simulation_dir"  # Todo: Add path
path_input_folder = r"D:\Elie\PhD\Sim_ext_paper\\Inputs"

# Path to the target buildings hbjson folder for the various geometry alternatives
geometry_alternative_list = ["Low_Density", "Medium_Density", "High_Density"]  # Todo: Add more densities
path_geometry_alternatives_folder = os.path.join(path_input_folder, r"hbjsons_geometry_alternatives")

path_geometry_alternative_hbjson_folder_dict = {
    alternative: os.path.join(path_geometry_alternatives_folder, alternative) for alternative in
    geometry_alternative_list}

# Context
path_gis_context = os.path.join(path_input_folder, r"GIS_context", r"Context_buildings_in_deg")
unit_gis = "deg"
# Context filtering parameters
mvfc = 0.001  # Minimum view factor criterion  todo : check the value
num_ray = 3  # Number of rays for the second pass of the context filtering

# UBES parameters
path_epw = os.path.join(path_input_folder, r"IS_5280_A_Tel_Aviv.epw")
path_energyplus_simulation_parameters = os.path.join(path_input_folder, r"hb_sim_paramters.json")

cop_heating = 3.
cop_cooling = 3.

# BIPV Simulation parameters

start_year = 2024
end_year = 2084

offset_dist = 0.1

plot_area = 34122  # in m2

bipv_scenarios_param_dict = {  # Todo: Have variations with various technologies
    "Sustainable_c_si": {
        "roof_grid_size_x": 1,
        "facades_grid_size_x": 1,
        "roof_grid_size_y": 2.04,
        "facades_grid_size_y": 2.04,
        "roof_id_pv_tech": "mitrex_roof c-Si M390-A1F Simbuild paper extended",
        "facades_id_pv_tech": "mitrex_facades c-Si Solar Siding 350W - Dove Grey china Simbuild paper extended",
        "roof_transport_id": "China-Israel",
        "facades_transport_id": "China-Israel",
        "roof_inverter_id": "inverter_default_old",
        "facades_inverter_id": "inverter_default_old",
        "roof_inverter_sizing_ratio": 0.85,
        "facades_inverter_sizing_ratio": 0.4,
        "minimum_panel_eroi": 2.5,
        "minimum_economic_roi": 1.2,
        "electricity_sell_price": 0.14,
        "replacement_scenario": "replace_failed_panels_every_X_years",
        "panel_replacement_min_age": 20,
        "replacement frequency": 5,
        "infrastructure_replacement_last_year": 40
    },
    "Energy_Production_c_si":
        {
            "roof_grid_size_x": 1,
            "facades_grid_size_x": 1,
            "roof_grid_size_y": 2.04,
            "facades_grid_size_y": 2.04,
            "roof_id_pv_tech": "mitrex_roof c-Si M390-A1F Simbuild paper extended",
            "facades_id_pv_tech": "mitrex_facades c-Si Solar Siding 350W - Dove Grey china Simbuild paper extended",
            "roof_transport_id": "China-Israel",
            "facades_transport_id": "China-Israel",
            "roof_inverter_id": "inverter_default_old",
            "facades_inverter_id": "inverter_default_old",
            "roof_inverter_sizing_ratio": 0.85,
            "facades_inverter_sizing_ratio": 0.4,
            "minimum_panel_eroi": 1.2,
            "minimum_economic_roi": 1.2,
            "electricity_sell_price": 0.14,
            "replacement_scenario": "replace_all_panels_every_X_years",
            "panel_replacement_min_age": 20,
            "replacement frequency": 5,
            "infrastructure_replacement_last_year": 45
        },
    "Balanced_c_si":
        {
            "roof_grid_size_x": 1,
            "facades_grid_size_x": 1,
            "roof_grid_size_y": 2.04,
            "facades_grid_size_y": 2.04,
            "roof_id_pv_tech": "mitrex_roof c-Si M390-A1F Simbuild paper extended",
            "facades_id_pv_tech": "mitrex_facades c-Si Solar Siding 350W - Dove Grey china Simbuild paper extended",
            "roof_transport_id": "China-Israel",
            "facades_transport_id": "China-Israel",
            "roof_inverter_id": "inverter_default_old",
            "facades_inverter_id": "inverter_default_old",
            "roof_inverter_sizing_ratio": 0.85,
            "facades_inverter_sizing_ratio": 0.4,
            "minimum_panel_eroi":2.,
            "minimum_economic_roi": 1.2,
            "electricity_sell_price": 0.14,
            "replacement_scenario": "replace_failed_panels_every_X_years",
            "panel_replacement_min_age": 20,
            "replacement frequency": 5,
            "infrastructure_replacement_last_year": 45
        },
    "Sustainable_cigs":
        {
            "roof_grid_size_x": 1.3,
            "facades_grid_size_x": 1.3,
            "roof_grid_size_y": 1.9,
            "facades_grid_size_y": 1.9,
            "roof_id_pv_tech": "cigs eterbright CIGS-3650A1 roof Simbuild paper extended",
            "facades_id_pv_tech": "cigs eterbright CIGS-3650A1 facade Simbuild paper extended",
            "roof_transport_id": "China-Israel",
            "facades_transport_id": "China-Israel",
            "roof_inverter_id": "inverter_default_old",
            "facades_inverter_id": "inverter_default_old",
            "roof_inverter_sizing_ratio": 0.85,
            "facades_inverter_sizing_ratio": 0.4,
            "minimum_panel_eroi": 2.5,
            "minimum_economic_roi": 1.2,
            "electricity_sell_price": 0.14,
            "replacement_scenario": "replace_failed_panels_every_X_years",
            "panel_replacement_min_age": 20,
            "replacement frequency": 5,
            "infrastructure_replacement_last_year": 40
        },
    "Energy_Production_cigs":
        {
            "roof_grid_size_x": 1.3,
            "facades_grid_size_x": 1.3,
            "roof_grid_size_y": 1.9,
            "facades_grid_size_y": 1.9,
            "roof_id_pv_tech": "cigs eterbright CIGS-3650A1 roof Simbuild paper extended",
            "facades_id_pv_tech": "cigs eterbright CIGS-3650A1 facade Simbuild paper extended",
            "roof_transport_id": "China-Israel",
            "facades_transport_id": "China-Israel",
            "roof_inverter_id": "inverter_default_old",
            "facades_inverter_id": "inverter_default_old",
            "roof_inverter_sizing_ratio": 0.85,
            "facades_inverter_sizing_ratio": 0.4,
            "minimum_panel_eroi": 1.2,
            "minimum_economic_roi": 1.2,
            "electricity_sell_price": 0.14,
            "replacement_scenario": "replace_all_panels_every_X_years",
            "panel_replacement_min_age": 20,
            "replacement frequency": 5,
            "infrastructure_replacement_last_year": 45
        },
    "Balanced_cigs":
        {
            "roof_grid_size_x": 1.3,
            "facades_grid_size_x": 1.3,
            "roof_grid_size_y": 1.9,
            "facades_grid_size_y": 1.9,
            "roof_id_pv_tech": "cigs eterbright CIGS-3650A1 roof Simbuild paper extended",
            "facades_id_pv_tech": "cigs eterbright CIGS-3650A1 facade Simbuild paper extended",
            "roof_transport_id": "China-Israel",
            "facades_transport_id": "China-Israel",
            "roof_inverter_id": "inverter_default_old",
            "facades_inverter_id": "inverter_default_old",
            "roof_inverter_sizing_ratio": 0.85,
            "facades_inverter_sizing_ratio": 0.4,
            "minimum_panel_eroi":2.,
            "minimum_economic_roi": 1.2,
            "electricity_sell_price": 0.14,
            "replacement_scenario": "replace_failed_panels_every_X_years",
            "panel_replacement_min_age": 20,
            "replacement frequency": 5,
            "infrastructure_replacement_last_year": 45
        }
}

# KPI parameters
grid_ghg_intensity = 0.660
grid_energy_intensity = 2.84
grid_electricity_sell_price = 0.14

# Simulation alternatives

alternative_dict = {
    bipv_scenario + "_" + geometry_alternative: {
        "bipv_scenario_identifier": bipv_scenario,
        "geometry_alternative": geometry_alternative,
    }
    for bipv_scenario in bipv_scenarios_param_dict.keys()
    for geometry_alternative in geometry_alternative_list
}

alternative_dict_test = {
    bipv_scenario + "_" + geometry_alternative: {
        "bipv_scenario_identifier": bipv_scenario,
        "geometry_alternative": geometry_alternative,
    }
    for bipv_scenario in list(bipv_scenarios_param_dict.keys())[0:1]
    for geometry_alternative in geometry_alternative_list[0:1]
}
