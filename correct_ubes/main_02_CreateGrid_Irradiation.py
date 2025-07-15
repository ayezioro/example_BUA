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

    # Generate mesh for BIPV
    SimFunSolarRadAndBipv.generate_sensor_grid(urban_canopy_object=urban_canopy_obj,
                                               building_id_list=None,
                                               bipv_on_facades=True,
                                               bipv_on_roof=True,
                                               roof_grid_size_x=2.05,
                                               roof_grid_size_y=1.0,
                                               facades_grid_size_x=1.05,
                                               facades_grid_size_y=1.05,
                                               offset_dist=0.1,
                                               overwrite=True
                                               )



    # Simulate Irradiation
    SimFunSolarRadAndBipv.run_annual_solar_irradiance_simulation(urban_canopy_object=urban_canopy_obj,
                                                                 path_simulation_folder=path_simulation_folder,
                                                                 building_id_list=None,
                                                                 path_weather_file=path_epw,
                                                                 overwrite=True,
                                                                 north_angle=0,
                                                                 silent=True
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
