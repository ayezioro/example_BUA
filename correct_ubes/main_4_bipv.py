from bua.config.config_default_values_user_parameters import default_efficiency_computation_method
from bua.simulation_steps import *

from input_data import *


def main():
    """
    :return:
    """
    # Clean Simulation clean
    ##SimulationCommonMethods.clear_simulation_temp_folder()
    # Set up simulation folder
    SimulationCommonMethods.make_simulation_folder(path_simulation_folder=path_simulation_folder
                                                   )
    # Initialize urban canopy object
    urban_canopy_obj = SimulationCommonMethods.create_or_load_urban_canopy_object(
        path_simulation_folder=path_simulation_folder
        )



    # BIPV Panel Simulation
    # User defined values
    SimFunSolarRadAndBipv.run_bipv_harvesting_and_lca_simulation(urban_canopy_object=urban_canopy_obj,
                                                                 path_simulation_folder=path_simulation_folder,
                                                                 bipv_scenario_identifier="bipv_simulation_1",
                                                                 building_id_list=None,
                                                                 roof_id_pv_tech="mitrex_roof c-Si M390-A1F default",
                                                                 facades_id_pv_tech="mitrex_facades c-Si Solar Siding 350W - Dove Grey china default_1.0x1.0",
                                                                 roof_transport_id="China-Israel",
                                                                 facades_transport_id="China-Israel",
                                                                 roof_inverter_id="inverter_default",
                                                                 facades_inverter_id="inverter_default",
                                                                 roof_inverter_sizing_ratio=0.9,
                                                                 facades_inverter_sizing_ratio=0.4,
                                                                 efficiency_computation_method=default_efficiency_computation_method,
                                                                 minimum_panel_eroi=1.5,
                                                                 minimum_economic_roi=0,
                                                                 electricity_sell_price=0.14,
                                                                 start_year=2024,
                                                                 end_year=2074,
                                                                 replacement_scenario="replace_failed_panels_every_X_years",
                                                                 panel_replacement_min_age=20,
                                                                 replacement_frequency_in_years=15,
                                                                 infrastructure_replacement_last_year=40,
                                                                 continue_simulation=False
                                                                 )


    #
    SimFunSolarRadAndBipv.run_kpi_simulation(urban_canopy_object=urban_canopy_obj,
                                             path_simulation_folder=path_simulation_folder,
                                             bipv_scenario_identifier="bipv_simulation_1",
                                             grid_ghg_intensity=0.660,
                                             grid_energy_intensity=2.84,
                                             grid_electricity_sell_price=0.14,
                                             zone_area=zone_area
                                             )

    ###############################################################################################################################
    # Save Urban Canopy Object
    SimulationCommonMethods.save_urban_canopy_object_to_pickle(urban_canopy_object=urban_canopy_obj,
                                                               path_simulation_folder=path_simulation_folder
                                                               )
    SimulationCommonMethods.save_urban_canopy_to_json(urban_canopy_object=urban_canopy_obj,
                                                      path_simulation_folder=path_simulation_folder
                                                      )
    ###############################################################################################################################


if __name__ == '__main__':
    main()
