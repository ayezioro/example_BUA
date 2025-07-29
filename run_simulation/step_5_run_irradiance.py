from bua.config.config_default_values_user_parameters import (
    default_efficiency_computation_method,
)
from bua.simulation_steps import *

from bua.building import BuildingModeled


def run_radiation_simulation(
    path_simulation_folder,
    path_weather_file,
    overwrite=False,
):
    """
    :return:
    """

    # Initialize urban canopy object
    urban_canopy_obj = SimulationCommonMethods.create_or_load_urban_canopy_object(
        path_simulation_folder=path_simulation_folder
    )

    # Simulate Irradiation
    SimFunSolarRadAndBipv.run_annual_solar_irradiance_simulation(
        urban_canopy_object=urban_canopy_obj,
        path_simulation_folder=path_simulation_folder,
        building_id_list=None,
        path_weather_file=path_weather_file,
        overwrite=overwrite,
        north_angle=0,
        silent=True,
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
