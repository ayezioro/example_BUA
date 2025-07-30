import os
from bua.simulation_steps import *


def load_buildings(
    path_simulation_folder,
    path_folder_hbjson,
    path_context_file_json,
):
    """
    :return:
    """

    # Set up simulation folder
    SimulationCommonMethods.make_simulation_folder(
        path_simulation_folder=path_simulation_folder
    )
    # Initialize urban canopy object
    urban_canopy_obj = SimulationCommonMethods.create_or_load_urban_canopy_object(
        path_simulation_folder=path_simulation_folder
    )
    if path_context_file_json is not None and os.path.isfile(path_context_file_json):
        # Load context buildings
        SimulationLoadBuildingOrGeometry.add_buildings_from_lb_polyface3d_json_in_urban_canopy(
            urban_canopy_object=urban_canopy_obj,
            path_lb_polyface3d_json_file=path_context_file_json,
        )

    SimulationLoadBuildingOrGeometry.add_buildings_from_hbjson_to_urban_canopy(
        urban_canopy_object=urban_canopy_obj,
        path_folder_hbjson=path_folder_hbjson,
        path_file_hbjson=None,
        are_buildings_targets=True,
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
