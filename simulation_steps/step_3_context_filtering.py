from bua.simulation_steps import *


def perform_context_selection(
    path_simulation_folder,
    min_vf_criterion=0.001,
    number_of_rays=9,
    consider_windows=False,
    keep_discarded_faces=False,
    overwrite=False,
):
    """
    :return:
    """

    # Initialize urban canopy object
    urban_canopy_obj = SimulationCommonMethods.create_or_load_urban_canopy_object(
        path_simulation_folder=path_simulation_folder
    )

    SimulationBuildingManipulationFunctions.make_oriented_bounding_boxes_of_buildings_in_urban_canopy(
        urban_canopy_object=urban_canopy_obj, overwrite=overwrite
    )

    ContextSelection.perform_first_pass_of_context_filtering_on_buildings(
        urban_canopy_object=urban_canopy_obj,
        min_vf_criterion=min_vf_criterion,
        overwrite=overwrite,
    )
    ContextSelection.perform_second_pass_of_context_filtering_on_buildings(
        urban_canopy_object=urban_canopy_obj,
        no_ray_tracing=False,
        number_of_rays=number_of_rays,
        consider_windows=consider_windows,
        keep_discarded_faces=keep_discarded_faces,
        overwrite=overwrite,
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
