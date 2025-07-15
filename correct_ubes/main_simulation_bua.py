from bua.simulation_steps import *

from input_data import *


def main():
    """

    :return:
    """
    # Clean Simulation clean
    ##SimulationCommonMethods.clear_simulation_temp_folder()
    # Set up simulation folder
    ###SimulationCommonMethods.make_simulation_folder()
    SimulationCommonMethods.make_simulation_folder(path_simulation_folder = path_simulation_folder)
    # Initialize urban canopy object
    #urban_canopy_obj = SimulationCommonMethods.create_or_load_urban_canopy_object()
    urban_canopy_obj = SimulationCommonMethods.create_or_load_urban_canopy_object(
        path_simulation_folder = path_simulation_folder)

    #print('uco ', urban_canopy_obj, path_context_file_json)

    # Load context buildings
    SimulationLoadBuildingOrGeometry.add_buildings_from_lb_polyface3d_json_in_urban_canopy(
        urban_canopy_object=urban_canopy_obj,
        path_lb_polyface3d_json_file=path_context_file_json)

    SimulationLoadBuildingOrGeometry.add_buildings_from_hbjson_to_urban_canopy(urban_canopy_object=urban_canopy_obj,
                                                                               path_folder_hbjson=path_folder_data1,
                                                                               path_file_hbjson=None,
                                                                               are_buildings_targets=True
                                                                               )
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
    UrbanBuildingEnergySimulationFunctions.generate_idf_files_for_ubes_with_openstudio_in_urban_canopy(
        urban_canopy_obj=urban_canopy_obj,
        path_simulation_folder = path_simulation_folder,
        overwrite=False,
        silent=True)
    # # Run IDF through EnergyPlus
    UrbanBuildingEnergySimulationFunctions.run_idf_files_with_energyplus_for_ubes_in_urban_canopy(
        urban_canopy_obj=urban_canopy_obj,
        path_simulation_folder = path_simulation_folder,
        overwrite=False,
        silent=True)
    # # Extract results
    UrbanBuildingEnergySimulationFunctions.extract_results_from_ep_simulation(
        urban_canopy_obj=urban_canopy_obj,
        path_simulation_folder = path_simulation_folder,
        cop_heating=cop_heating, cop_cooling=cop_cooling)

    """
    """
    SimulationCommonMethods.save_urban_canopy_object_to_pickle(urban_canopy_object=urban_canopy_obj,
                                                               path_simulation_folder = path_simulation_folder
                                                               )
    SimulationCommonMethods.save_urban_canopy_to_json(urban_canopy_object=urban_canopy_obj,
                                                      path_simulation_folder = path_simulation_folder
                                                      )

if __name__ == '__main__':
    main()
