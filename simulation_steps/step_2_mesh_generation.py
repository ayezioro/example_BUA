from bua.simulation_steps import *


def generate_mesh_on_buildings(
    path_simulation_folder,
    bipv_on_facades=True,
    bipv_on_roof=True,
    roof_grid_size_x=2.05,
    roof_grid_size_y=1.0,
    facades_grid_size_x=1.05,
    facades_grid_size_y=1.05,
    offset_dist=0.1,
    overwrite=False,
):
    """
    :return:
    """

    # Initialize urban canopy object
    urban_canopy_obj = SimulationCommonMethods.create_or_load_urban_canopy_object(
        path_simulation_folder=path_simulation_folder
    )
    # Generate mesh for BIPV
    SimFunSolarRadAndBipv.generate_sensor_grid(
        urban_canopy_object=urban_canopy_obj,
        building_id_list=None,
        bipv_on_facades=bipv_on_facades,
        bipv_on_roof=bipv_on_roof,
        roof_grid_size_x=roof_grid_size_x,
        roof_grid_size_y=roof_grid_size_y,
        facades_grid_size_x=facades_grid_size_x,
        facades_grid_size_y=facades_grid_size_y,
        offset_dist=offset_dist,
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
