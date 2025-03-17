from bua.simulation_steps import *

from input_data import *


def main():
    """

    :return:
    """
    # Set up simulation folder
    SimulationCommonMethods.make_simulation_folder(path_simulation_folder=path_simulation_folder)
    # Initialize urban canopy object
    urban_canopy_obj = SimulationCommonMethods.create_or_load_urban_canopy_object(
        path_simulation_folder=path_simulation_folder)

    # Load context buildings
    SimulationLoadBuildingOrGeometry.add_buildings_from_lb_polyface3d_json_in_urban_canopy(
        urban_canopy_object=urban_canopy_obj,
        path_lb_polyface3d_json_file=path_context_file_json)

    SimulationLoadBuildingOrGeometry.add_buildings_from_hbjson_to_urban_canopy(urban_canopy_object=urban_canopy_obj,
                                                                               path_folder_hbjson=path_folder_building_hbjson,
                                                                               path_file_hbjson=None,
                                                                               are_buildings_targets=True
                                                                               )

    # Merge faces NOT WORKING
    # SimulationBuildingManipulationFunctions.make_merged_face_of_buildings_in_urban_canopy(
    #    urban_canopy_object=urban_canopy_obj, orient_roof_mesh_to_according_to_building_orientation=True)

    # Context Filtering
    SimulationBuildingManipulationFunctions.make_oriented_bounding_boxes_of_buildings_in_urban_canopy(
        urban_canopy_object=urban_canopy_obj, overwrite=True)

    ContextSelection.perform_first_pass_of_context_filtering_on_buildings(urban_canopy_object=urban_canopy_obj,
                                                                          min_vf_criterion=0.01)
    ContextSelection.perform_second_pass_of_context_filtering_on_buildings(urban_canopy_object=urban_canopy_obj)

    # UBES
    # # Load epw and simulation parameters
    UrbanBuildingEnergySimulationFunctions.load_epw_and_hb_simulation_parameters_for_ubes_in_urban_canopy(
        urban_canopy_obj=urban_canopy_obj,
        path_simulation_folder=path_simulation_folder,
        # path_hbjson_simulation_parameter_file=path_energyplus_simulation_parameters,
        path_weather_file=path_epw,
        ddy_file=None,
        overwrite=False)
    # # Write IDF
    UrbanBuildingEnergySimulationFunctions.generate_idf_files_for_ubes_with_openstudio_in_urban_canopy(
        urban_canopy_obj=urban_canopy_obj,
        path_simulation_folder=path_simulation_folder,
        overwrite=False,
        silent=True)
    # # Run IDF through EnergyPlus
    UrbanBuildingEnergySimulationFunctions.run_idf_files_with_energyplus_for_ubes_in_urban_canopy(
        urban_canopy_obj=urban_canopy_obj,
        path_simulation_folder=path_simulation_folder,
        overwrite=False,
        silent=True)
    # # Extract results
    UrbanBuildingEnergySimulationFunctions.extract_results_from_ep_simulation(
        urban_canopy_obj=urban_canopy_obj,
        path_simulation_folder=path_simulation_folder,
        cop_heating=cop_heating, cop_cooling=cop_cooling)

    # Generate mesh for BIPV
    SimFunSolarRadAndBipv.generate_sensor_grid(urban_canopy_object=urban_canopy_obj)

    SimulationCommonMethods.save_urban_canopy_object_to_pickle(urban_canopy_object=urban_canopy_obj,
                                                               path_simulation_folder=path_simulation_folder)
    SimulationCommonMethods.save_urban_canopy_to_json(urban_canopy_object=urban_canopy_obj,
                                                      path_simulation_folder=path_simulation_folder)


if __name__ == '__main__':
    main()
