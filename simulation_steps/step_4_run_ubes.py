from bua.simulation_steps import *


def run_ubes(
    path_simulation_folder, path_weather_file, cop_heating, cop_cooling, overwrite=False
):
    """
    :return:
    """

    # Initialize urban canopy object
    urban_canopy_obj = SimulationCommonMethods.create_or_load_urban_canopy_object(
        path_simulation_folder=path_simulation_folder
    )

    # UBES
    # Load epw and simulation parameters
    UrbanBuildingEnergySimulationFunctions.load_epw_and_hb_simulation_parameters_for_ubes_in_urban_canopy(
        urban_canopy_obj=urban_canopy_obj,
        path_simulation_folder=path_simulation_folder,
        path_weather_file=path_weather_file,  # path_epw
        ddy_file=None,
        overwrite=overwrite,
    )
    # # Write IDF
    UrbanBuildingEnergySimulationFunctions.generate_idf_files_for_ubes_with_openstudio_in_urban_canopy(
        urban_canopy_obj=urban_canopy_obj,
        path_simulation_folder=path_simulation_folder,
        building_id_list=None,
        overwrite=overwrite,
        silent=False,
    )
    # # Run IDF through EnergyPlus
    UrbanBuildingEnergySimulationFunctions.run_idf_files_with_energyplus_for_ubes_in_urban_canopy(
        urban_canopy_obj=urban_canopy_obj,
        path_simulation_folder=path_simulation_folder,
        building_id_list=None,
        overwrite=overwrite,
        silent=True,
        run_in_parallel=False,
    )
    # # Extract results
    UrbanBuildingEnergySimulationFunctions.extract_results_from_ep_simulation(
        urban_canopy_obj=urban_canopy_obj,
        path_simulation_folder=path_simulation_folder,
        cop_heating=cop_heating,
        cop_cooling=cop_cooling,
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
