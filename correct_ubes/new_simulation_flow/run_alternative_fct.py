from bua.config.config_default_values_user_parameters import default_efficiency_computation_method
from bua.simulation_steps import *

from bua.building import BuildingModeled


def run_alternative(path_simulation_folder,
                    path_folder_hbjson,
                    path_context_file_json,
                    path_weather_file,
                    cop_heating,
                    cop_cooling,
                    zone_area,
                    get_results_only):
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
    if not get_results_only:

        # Load context buildings
        SimulationLoadBuildingOrGeometry.add_buildings_from_lb_polyface3d_json_in_urban_canopy(
            urban_canopy_object=urban_canopy_obj,
            path_lb_polyface3d_json_file=path_context_file_json
        )

        SimulationLoadBuildingOrGeometry.add_buildings_from_hbjson_to_urban_canopy(urban_canopy_object=urban_canopy_obj,
                                                                                   path_folder_hbjson=path_folder_hbjson,
                                                                                   path_file_hbjson=None,
                                                                                   are_buildings_targets=True
                                                                                   )
        # Context Filtering
        SimulationBuildingManipulationFunctions.make_oriented_bounding_boxes_of_buildings_in_urban_canopy(
            urban_canopy_object=urban_canopy_obj,
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
        # UBES
        # Load epw and simulation parameters
        UrbanBuildingEnergySimulationFunctions.load_epw_and_hb_simulation_parameters_for_ubes_in_urban_canopy(
            urban_canopy_obj=urban_canopy_obj,
            path_simulation_folder=path_simulation_folder,
            # path_hbjson_simulation_parameter_file=r"C:\Users\User\Downloads\unnamed.json",
            path_weather_file=path_weather_file, # path_epw
            ddy_file=None,
            overwrite=True
        )
        # # Write IDF
        UrbanBuildingEnergySimulationFunctions.generate_idf_files_for_ubes_with_openstudio_in_urban_canopy(
            urban_canopy_obj=urban_canopy_obj,
            path_simulation_folder=path_simulation_folder,
            building_id_list=None,
            overwrite=True,
            silent=False
        )
        # # Run IDF through EnergyPlus
        UrbanBuildingEnergySimulationFunctions.run_idf_files_with_energyplus_for_ubes_in_urban_canopy(
            urban_canopy_obj=urban_canopy_obj,
            path_simulation_folder=path_simulation_folder,
            building_id_list=None,
            overwrite=True,
            silent=True,
            run_in_parallel=False
        )
        # # Extract results
        UrbanBuildingEnergySimulationFunctions.extract_results_from_ep_simulation(urban_canopy_obj=urban_canopy_obj,
                                                                                  path_simulation_folder=path_simulation_folder,
                                                                                  cop_heating=cop_heating,
                                                                                  cop_cooling=cop_cooling
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
                                                                     path_weather_file=path_weather_file,
                                                                     overwrite=True,
                                                                     north_angle=0,
                                                                     silent=True
                                                                     )


        ###############################################################################################################################

        # BIPV Panel Simulation
        # User defined values
        SimFunSolarRadAndBipv.run_bipv_harvesting_and_lca_simulation(urban_canopy_object=urban_canopy_obj,
                                                                     path_simulation_folder=path_simulation_folder,
                                                                     bipv_scenario_identifier="bipv_simulation_1",
                                                                     building_id_list=None,
                                                                     # roof_id_pv_tech="mitrex_roof c-Si M390-A1F default",
                                                                     roof_id_pv_tech="mitrex_roof c-Si M390-A1F 2025",
                                                                     facades_id_pv_tech="mitrex_facades c-Si Solar Siding 350W - Dove Grey china 2025_1.0x1.0",
                                                                     roof_transport_id="China-Israel",
                                                                     facades_transport_id="China-Israel",
                                                                     roof_inverter_id="inverter_default",
                                                                     facades_inverter_id="inverter_default",
                                                                     roof_inverter_sizing_ratio=0.9,
                                                                     facades_inverter_sizing_ratio=0.4,
                                                                     efficiency_computation_method=default_efficiency_computation_method,
                                                                     minimum_panel_eroi=1.5,
                                                                     minimum_economic_roi=0,
                                                                     electricity_sell_price=0.14,
                                                                     start_year=2024,
                                                                     end_year=2074,
                                                                     replacement_scenario="replace_failed_panels_every_X_years",
                                                                     panel_replacement_min_age=20,
                                                                     replacement_frequency_in_years=15,
                                                                     infrastructure_replacement_last_year=40,
                                                                     continue_simulation=False
                                                                     )

        #
        SimFunSolarRadAndBipv.run_kpi_simulation(urban_canopy_object=urban_canopy_obj,
                                                 path_simulation_folder=path_simulation_folder,
                                                 bipv_scenario_identifier="bipv_simulation_1",
                                                 grid_ghg_intensity=0.660,
                                                 grid_energy_intensity=2.84,
                                                 grid_electricity_sell_price=0.14,
                                                 zone_area=zone_area
                                                 )


    ###############################################################################################################################
    # Make result dictionary
    name_simulation_folder = path_simulation_folder.split("\\")[-1]

    bes_dict = {}

    for building_id,building_obj in urban_canopy_obj.building_dict.items():
        if isinstance(building_obj,BuildingModeled) and building_obj.is_target:
            bes_dict[building_id] = building_obj.bes_obj.to_dict()["bes_results_dict"]

    result_dict={
        "alternative_name" : name_simulation_folder,
        "bes" : bes_dict,
        "ubes" : urban_canopy_obj.ubes_obj.to_dict()["ubes_results_dict"],  # to access value result_dict["ubes"]["heating"]["yearly"]
        "kpis" : urban_canopy_obj.bipv_scenario_dict["bipv_simulation_1"].urban_canopy_bipv_kpis_obj.to_dict()["kpis"],
    }

    # ###############################################################################################################################
    if not get_results_only:
        # Save Urban Canopy Object
        SimulationCommonMethods.save_urban_canopy_object_to_pickle(urban_canopy_object=urban_canopy_obj,
                                                                   path_simulation_folder=path_simulation_folder
                                                                   )
        SimulationCommonMethods.save_urban_canopy_to_json(urban_canopy_object=urban_canopy_obj,
                                                          path_simulation_folder=path_simulation_folder
                                                          )

    return result_dict