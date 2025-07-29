from operator import contains

from bua.simulation_steps import *
from bua.config.config_default_values_user_parameters import (
    default_efficiency_computation_method,
)


def run_bipv_simulations(
    path_simulation_folder,
    zone_area,
    bipv_scenario_identifier,
    roof_id_pv_tech="mitrex_roof c-Si M390-A1F baseline 2025",
    facades_id_pv_tech="mitrex_facades c-Si Solar Siding 350W - Dove Grey china 2025_1.0x1.0",
    roof_transport_id="China-Israel 22kg",
    facades_transport_id="China-Israel 9.5kg",
    roof_inverter_id="inverter_default",
    facades_inverter_id="inverter_default",
    roof_inverter_sizing_ratio=0.9,
    facades_inverter_sizing_ratio=0.4,
    efficiency_computation_method=default_efficiency_computation_method,
    minimum_panel_eroi=1.5,  # [1.2:2.5]
    minimum_economic_roi=1.1,  # [1.1:1.4 for mortar. x.x for stone, y.y for metal]
    start_year=2024,
    end_year=2084,
    replacement_scenario="replace_failed_panels_every_X_years",
    panel_replacement_min_age=20,  # [20:30]
    replacement_frequency_in_years=5,  # [5:10]
    infrastructure_replacement_last_year=40,  # [40:50]
    continue_simulation=False,
    grid_ghg_intensity=0.660,
    grid_energy_intensity=2.84,
    grid_electricity_sell_price=0.14,
):

    # Initialize urban canopy object
    urban_canopy_obj = SimulationCommonMethods.create_or_load_urban_canopy_object(
        path_simulation_folder=path_simulation_folder
    )

    SimFunSolarRadAndBipv.run_bipv_harvesting_and_lca_simulation(
        urban_canopy_object=urban_canopy_obj,
        path_simulation_folder=path_simulation_folder,
        bipv_scenario_identifier=bipv_scenario_identifier,
        building_id_list=None,
        roof_id_pv_tech=roof_id_pv_tech,
        facades_id_pv_tech=facades_id_pv_tech,
        roof_transport_id=roof_transport_id,
        facades_transport_id=facades_transport_id,
        roof_inverter_id=roof_inverter_id,
        facades_inverter_id=facades_inverter_id,
        roof_inverter_sizing_ratio=roof_inverter_sizing_ratio,
        facades_inverter_sizing_ratio=facades_inverter_sizing_ratio,
        efficiency_computation_method=efficiency_computation_method,
        minimum_panel_eroi=minimum_panel_eroi,  # [1.2:2.5]
        minimum_economic_roi=minimum_economic_roi,  # [1.1:1.4 for mortar. x.x for stone, y.y for metal]
        electricity_sell_price=grid_electricity_sell_price,
        start_year=start_year,
        end_year=end_year,
        replacement_scenario=replacement_scenario,
        panel_replacement_min_age=panel_replacement_min_age,  # [20:30]
        replacement_frequency_in_years=replacement_frequency_in_years,  # [5:10]
        infrastructure_replacement_last_year=infrastructure_replacement_last_year,  # [40:50]
        continue_simulation=continue_simulation,
    )

    SimFunSolarRadAndBipv.run_kpi_simulation(
        urban_canopy_object=urban_canopy_obj,
        path_simulation_folder=path_simulation_folder,
        bipv_scenario_identifier=bipv_scenario_identifier,
        grid_ghg_intensity=grid_ghg_intensity,
        grid_energy_intensity=grid_energy_intensity,
        grid_electricity_sell_price=grid_electricity_sell_price,
        zone_area=zone_area,
    )
    # Save the urban canopy object
    SimulationCommonMethods.save_urban_canopy_object_to_pickle(
        urban_canopy_object=urban_canopy_obj,
        path_simulation_folder=path_simulation_folder,
    )
    SimulationCommonMethods.save_urban_canopy_to_json(
        urban_canopy_object=urban_canopy_obj,
        path_simulation_folder=path_simulation_folder,
    )
    return
