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

    # Load context buildings
    SimulationLoadBuildingOrGeometry.add_buildings_from_lb_polyface3d_json_in_urban_canopy(urban_canopy_object=urban_canopy_obj,
                                                                                           path_lb_polyface3d_json_file=path_context_file_json
                                                                                           )

    SimulationLoadBuildingOrGeometry.add_buildings_from_hbjson_to_urban_canopy(urban_canopy_object=urban_canopy_obj,
                                                                               path_folder_hbjson=None,
                                                                               path_file_hbjson=path_folder_data2,
                                                                               are_buildings_targets=True
                                                                               )
    # Context Filtering
    SimulationBuildingManipulationFunctions.make_oriented_bounding_boxes_of_buildings_in_urban_canopy(urban_canopy_object=urban_canopy_obj,
                                                                                                      overwrite=True
                                                                                                      )

    ContextSelection.perform_first_pass_of_context_filtering_on_buildings(urban_canopy_object=urban_canopy_obj,
                                                                          min_vf_criterion=0.001,
                                                                          overwrite=True
                                                                          )
    ContextSelection.perform_second_pass_of_context_filtering_on_buildings(urban_canopy_object=urban_canopy_obj,
                                                                           no_ray_tracing=False,
                                                                           number_of_rays=3,
                                                                           consider_windows=False,
                                                                           keep_discarded_faces=True,
                                                                           overwrite=True
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
