"""
Main file to simulate all the configurations for the extended BIPV paper
"""

import os
import shutil
import concurrent.futures

from concurrent.futures import ProcessPoolExecutor

from bua.simulation_steps import *

from simulation_inputs import *


def simulate_alternative(path_simulation_folder: str, alternative_name: str,
                         path_geometry_alternative_hbjson_folder: str,
                         path_gis_context: str, bipv_scenario_param_dict: dict):
    """

    :param path_simulation_folder:
    :param alternative_name:
    :param path_geometry_alternative_hbjson_folder:
    :param path_gis_context:
    :param bipv_scenario_param_dict:
    :return:
    """
    path_alternative_simulation_folder = os.path.join(path_simulation_folder, alternative_name)

    # Clean folder
    if os.path.isdir(path_alternative_simulation_folder):
        shutil.rmtree(path_alternative_simulation_folder)
    os.makedirs(path_alternative_simulation_folder)

    # ----- Init Urban canpy object -----#
    # Create simulation folder
    SimulationCommonMethods.make_simulation_folder(path_simulation_folder=path_alternative_simulation_folder)
    # Create urban_canopy
    urban_canopy_object = SimulationCommonMethods.create_or_load_urban_canopy_object(
        path_simulation_folder=path_alternative_simulation_folder)
    # ------ Load Buildings ------#
    # load GIS
    SimulationLoadBuildingOrGeometry.add_2D_GIS_to_urban_canopy(urban_canopy=urban_canopy_object,
                                                                path_gis=path_gis_context,
                                                                path_additional_gis_attribute_key_dict=None,
                                                                unit=unit_gis)
    # Move to origin
    SimulationBuildingManipulationFunctions.move_buildings_to_origin(urban_canopy_object=urban_canopy_object)
    # Load target buildnigs
    SimulationLoadBuildingOrGeometry.add_buildings_from_hbjson_to_urban_canopy(
        urban_canopy_object=urban_canopy_object,
        path_folder_hbjson=path_geometry_alternative_hbjson_folder,
        path_file_hbjson=None,
        are_buildings_targets=True,
        keep_context_from_hbjson=False
    )

    # ------ Context filtering -----#
    # Make merged faces hb models of buildings
    SimulationBuildingManipulationFunctions.make_merged_face_of_buildings_in_urban_canopy(
        urban_canopy_object=urban_canopy_object,
        orient_roof_mesh_to_according_to_building_orientation=True,
        north_angle=0,
        overwrite=True)
    # Make bounding boxes
    SimulationBuildingManipulationFunctions.make_oriented_bounding_boxes_of_buildings_in_urban_canopy(
        urban_canopy_object=urban_canopy_object, overwrite=True)

    # 1st pass context filter
    ContextSelection.perform_first_pass_of_context_filtering_on_buildings(
        urban_canopy_object,
        building_id_list=None,
        on_building_to_simulate=False,
        min_vf_criterion=mvfc,
        overwrite=True
    )
    # 2nd pass context filter
    ContextSelection.perform_second_pass_of_context_filtering_on_buildings(
        urban_canopy_object,
        number_of_rays=num_ray,
        on_building_to_simulate=False,
        consider_windows=True,
        keep_shades_from_user=False,
        overwrite=True,
        keep_discarded_faces=True
    )

    # # ------ UBES simulation -----#
    # # Load epw and simulation parameters
    # UrbanBuildingEnergySimulationFunctions.load_epw_and_hb_simulation_parameters_for_ubes_in_urban_canopy(
    #     urban_canopy_obj=urban_canopy_object,
    #     path_simulation_folder=path_alternative_simulation_folder,
    #     path_hbjson_simulation_parameter_file=path_energyplus_simulation_parameters,
    #     path_weather_file=path_epw,
    #     ddy_file=None,
    #     overwrite=False)
    # # Write IDF
    # UrbanBuildingEnergySimulationFunctions.generate_idf_files_for_ubes_with_openstudio_in_urban_canopy(
    #     urban_canopy_obj=urban_canopy_object,
    #     path_simulation_folder=path_alternative_simulation_folder,
    #     overwrite=False,
    #     silent=True)
    # # Run IDF through EnergyPlus
    # UrbanBuildingEnergySimulationFunctions.run_idf_files_with_energyplus_for_ubes_in_urban_canopy(
    #     urban_canopy_obj=urban_canopy_object,
    #     path_simulation_folder=path_alternative_simulation_folder,
    #     overwrite=False,
    #     silent=True)
    # # Extract results
    # UrbanBuildingEnergySimulationFunctions.extract_results_from_ep_simulation(
    #     urban_canopy_obj=urban_canopy_object,
    #     path_simulation_folder=path_alternative_simulation_folder,
    #     cop_heating=cop_heating, cop_cooling=cop_cooling)

    # ------ BIPV simulation -----#
    # Mesh Generation
    SimFunSolarRadAndBipv.generate_sensor_grid(
        urban_canopy_object=urban_canopy_object,
        bipv_on_roof=True,
        bipv_on_facades=True,
        roof_grid_size_x=bipv_scenario_param_dict["roof_grid_size_x"],
        facades_grid_size_x=bipv_scenario_param_dict["facades_grid_size_x"],
        roof_grid_size_y=bipv_scenario_param_dict["roof_grid_size_y"],
        facades_grid_size_y=bipv_scenario_param_dict["facades_grid_size_y"],
        offset_dist=offset_dist,
        overwrite=False)
    # Radiation Simulation
    SimFunSolarRadAndBipv.run_annual_solar_irradiance_simulation(
        urban_canopy_object=urban_canopy_object,
        path_simulation_folder=path_alternative_simulation_folder,
        building_id_list=None,
        path_weather_file=path_epw,
        overwrite=False, north_angle=0, silent=True
    )
    # BIPV Simulation
    SimFunSolarRadAndBipv.run_bipv_harvesting_and_lca_simulation(
        urban_canopy_object=urban_canopy_object,
        path_simulation_folder=path_alternative_simulation_folder,
        bipv_scenario_identifier=alternative_name,
        roof_id_pv_tech=bipv_scenario_param_dict["roof_id_pv_tech"],
        facades_id_pv_tech=bipv_scenario_param_dict["facades_id_pv_tech"],
        roof_transport_id=bipv_scenario_param_dict["roof_transport_id"],
        facades_transport_id=bipv_scenario_param_dict["facades_transport_id"],
        roof_inverter_id=bipv_scenario_param_dict["roof_inverter_id"],
        facades_inverter_id=bipv_scenario_param_dict["facades_inverter_id"],
        roof_inverter_sizing_ratio=bipv_scenario_param_dict["roof_inverter_sizing_ratio"],
        facades_inverter_sizing_ratio=bipv_scenario_param_dict["facades_inverter_sizing_ratio"],
        minimum_panel_eroi=bipv_scenario_param_dict["minimum_panel_eroi"],
        minimum_economic_roi=bipv_scenario_param_dict["minimum_economic_roi"],
        electricity_sell_price=bipv_scenario_param_dict["electricity_sell_price"],
        start_year=start_year,
        end_year=end_year,
        replacement_scenario=bipv_scenario_param_dict["replacement_scenario"],
        panel_replacement_min_age=bipv_scenario_param_dict["panel_replacement_min_age"],
        replacement_frequency_in_years=bipv_scenario_param_dict["replacement frequency"],
        infrastructure_replacement_last_year=bipv_scenario_param_dict["infrastructure_replacement_last_year"],
    )
    # KPI Calculation
    SimFunSolarRadAndBipv.run_kpi_simulation(
        urban_canopy_object=urban_canopy_object,
        path_simulation_folder=path_alternative_simulation_folder,
        bipv_scenario_identifier=alternative_name,
        grid_ghg_intensity=grid_ghg_intensity,
        grid_energy_intensity=grid_energy_intensity,
        grid_electricity_sell_price=grid_electricity_sell_price,
        zone_area=plot_area
    )
    # ----- Save results -----#
    # Export urban_canopy to pickle
    SimulationCommonMethods.save_urban_canopy_object_to_pickle(urban_canopy_object=urban_canopy_object,
                                                               path_simulation_folder=path_alternative_simulation_folder)
    # Export urban_canopy to json
    SimulationCommonMethods.save_urban_canopy_to_json(urban_canopy_object=urban_canopy_object,
                                                      path_simulation_folder=path_alternative_simulation_folder)


def main():
    """

    :return:
    """

    # Run the simulation for all the alternatives in parallel
    with ProcessPoolExecutor(max_workers=len(alternative_dict)) as executor:
        futures = [executor.submit(simulate_alternative, path_simulation_folder, alternative_name,
                         path_geometry_alternative_hbjson_folder_dict[alternative_dict[alternative_name]["geometry_alternative"]],
                         path_gis_context, bipv_scenarios_param_dict[alternative_dict[alternative_name]["bipv_scenario_identifier"]])
                   for alternative_name in alternative_dict.keys()]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Task generated an exception: {e}")



    # test simulate alternative with one building

    # simulate_alternative(path_simulation_folder=path_simulation_folder,
    #                      alternative_name="Balanced_cigs",
    #                      path_geometry_alternative_hbjson_folder=r"D:\Elie\PhD\Sim_ext_paper\Inputs\test_hbjson",
    #                      path_gis_context=path_gis_context,
    #                      bipv_scenario_param_dict=bipv_scenarios_param_dict["Balanced_cigs"])


if __name__ == '__main__':
    main()
