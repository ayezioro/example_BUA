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
    SimulationCommonMethods.make_simulation_folder(path_simulation_folder = path_simulation_folder
                                                   )
    # Initialize urban canopy object
    urban_canopy_obj = SimulationCommonMethods.create_or_load_urban_canopy_object(path_simulation_folder = path_simulation_folder
                                                                                  )
    ###############################################################################################################################

    # UBES
    # Load epw and simulation parameters
    UrbanBuildingEnergySimulationFunctions.load_epw_and_hb_simulation_parameters_for_ubes_in_urban_canopy(urban_canopy_obj=urban_canopy_obj,
                                                                                                          path_simulation_folder=path_simulation_folder,
                                                                                                          path_hbjson_simulation_parameter_file=r"C:\Users\User\Downloads\unnamed.json",
                                                                                                          path_weather_file=path_epw,
                                                                                                          ddy_file=None,
                                                                                                          overwrite=False
                                                                                                          )
    # # Write IDF
    UrbanBuildingEnergySimulationFunctions.generate_idf_files_for_ubes_with_openstudio_in_urban_canopy(urban_canopy_obj=urban_canopy_obj,
                                                                                                       path_simulation_folder = path_simulation_folder,
                                                                                                       building_id_list=None,
                                                                                                       overwrite=True,
                                                                                                       silent=False
                                                                                                       )
    # # Run IDF through EnergyPlus
    UrbanBuildingEnergySimulationFunctions.run_idf_files_with_energyplus_for_ubes_in_urban_canopy(urban_canopy_obj=urban_canopy_obj,
                                                                                                  path_simulation_folder = path_simulation_folder,
                                                                                                  building_id_list=None,
                                                                                                  overwrite=False,
                                                                                                  silent=True,
                                                                                                  run_in_parallel=False
                                                                                                  )
    # # Extract results
    UrbanBuildingEnergySimulationFunctions.extract_results_from_ep_simulation(urban_canopy_obj=urban_canopy_obj,
                                                                              path_simulation_folder=path_simulation_folder,
                                                                              cop_heating=cop_heating,
                                                                              cop_cooling=cop_cooling
                                                                              )

    ###############################################################################################################################
    # Save Urban Canopy Object
    SimulationCommonMethods.save_urban_canopy_object_to_pickle(urban_canopy_object=urban_canopy_obj,
                                                               path_simulation_folder = path_simulation_folder
                                                               )
    SimulationCommonMethods.save_urban_canopy_to_json(urban_canopy_object=urban_canopy_obj,
                                                      path_simulation_folder = path_simulation_folder
                                                      )
    ###############################################################################################################################

if __name__ == '__main__':
    main()
