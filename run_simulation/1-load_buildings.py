from bua.config.config_default_values_user_parameters import default_efficiency_computation_method
from bua.simulation_steps import *

def load_buildings(path_simulation_folder,
                    path_folder_hbjson,
                    path_context_file_json,
                    ):
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
    # Load context buildings
    SimulationLoadBuildingOrGeometry.add_buildings_from_lb_polyface3d_json_in_urban_canopy(
        urban_canopy_object=urban_canopy_obj,
        path_lb_polyface3d_json_file=path_context_file_json
    )

    SimulationLoadBuildingOrGeometry.add_buildings_from_hbjson_to_urban_canopy(
        urban_canopy_object=urban_canopy_obj,
                                                                             path_folder_hbjson=path_folder_hbjson,
                                                                               path_file_hbjson=None,
                                                                               are_buildings_targets=True
                                                                               )

    SimulationCommonMethods.save_urban_canopy_object_to_pickle(urban_canopy_object=urban_canopy_obj,
                                                               path_simulation_folder=path_simulation_folder
                                                               )
    SimulationCommonMethods.save_urban_canopy_to_json(urban_canopy_object=urban_canopy_obj,
                                                      path_simulation_folder=path_simulation_folder
                                                      )

    return result_dict


from bua.building import BuildingModeled