import json
import os

from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor

from inputs import *
import simulation_steps


def run_step(
    step_function, run_flag, list_hbjson_folders, pool_processor, num_workers, **kwargs
):
    """

    :param step_function:
    :param run_flag: bool, if True, the step will be executed
    :param list_hbjson_folders:
    :param pool_processor:
    :param num_workers:
    :param kwargs:
    :return:
    """
    if not run_flag:
        print(f"Skipping step: {step_function.__name__}")
        return
    if pool_processor == "thread":
        executor = ThreadPoolExecutor(max_workers=num_workers)
    elif pool_processor == "process":
        executor = ProcessPoolExecutor(max_workers=num_workers)
    else:
        raise ValueError("pool_processor must be 'thread' or 'process'")

    futures = []
    for path_folder_hbjson in list_hbjson_folders:
        name_simulation_folder = path_folder_hbjson.split("\\")[-1]
        path_simulation_folder = os.path.join(
            path_dir_simulation_all_alternatives, name_simulation_folder
        )
        if step_function == simulation_steps.load_buildings:
            future = executor.submit(
                step_function,
                path_simulation_folder=path_simulation_folder,
                path_folder_hbjson=path_folder_hbjson,
                **kwargs,
            )
        else:
            future = executor.submit(
                step_function, path_simulation_folder=path_simulation_folder, **kwargs
            )

        futures.append(future)

    results = [future.result() for future in futures]
    executor.shutdown()
    return


def main():

    ###### Run the simulation for all alternatives ######\
    # Init Urban Canopy and load buildings
    run_step(
        step_function=simulation_steps.load_buildings,
        run_flag=run_load_buildings,
        list_hbjson_folders=list_hbjson_folders,
        pool_processor="process",
        num_workers=num_workers_processes,
        path_context_file_json=path_brep_context,
    )
    # Generate meshes
    run_step(
        step_function=simulation_steps.generate_mesh_on_buildings,
        run_flag=run_mesh_generation,
        list_hbjson_folders=list_hbjson_folders,
        pool_processor="process",
        num_workers=num_workers_processes,
        bipv_on_facades=bipv_on_facades,
        bipv_on_roof=bipv_on_roof,
        roof_grid_size_x=roof_grid_size_x,
        roof_grid_size_y=roof_grid_size_y,
        facades_grid_size_x=facades_grid_size_x,
        facades_grid_size_y=facades_grid_size_y,
        offset_dist=offset_dist,
    )
    # Context selection
    run_step(
        step_function=simulation_steps.perform_context_selection,
        run_flag=run_context_filter,
        list_hbjson_folders=list_hbjson_folders,
        pool_processor="process",
        num_workers=num_workers_processes,
        min_vf_criterion=min_vf_criterion,
        number_of_rays=number_of_rays,
        consider_windows=consider_windows,
        keep_discarded_faces=keep_discarded_faces,
    )
    # Run UBES simulations
    run_step(
        step_function=simulation_steps.run_ubes,
        run_flag=run_ubes,
        list_hbjson_folders=list_hbjson_folders,
        pool_processor="process",
        num_workers=num_workers_processes,
        path_weather_file=path_epw,
        cop_heating=cop_heating,
        cop_cooling=cop_cooling,
    )
    # Run radiation simulations
    run_step(
        step_function=simulation_steps.run_radiation_simulation,
        run_flag=run_radiation_simulation,
        list_hbjson_folders=list_hbjson_folders,
        pool_processor="process",  # Check if it works with processes or threads or only sequential
        # pool_processor="thread",
        num_workers=num_workers_processes,
        # num_workers=1,    # Just in case: if the "thread" option does not work, there change the num_workers to 1
        path_weather_file=path_epw,
    )
    # Run BIPV simulations
    for bipv_scenario_identifier, bipv_scenario_in_dict in bipv_scenarios.items():
        run_step(
            step_function=simulation_steps.run_bipv_simulation,
            run_flag=run_bipv_simulation,
            list_hbjson_folders=list_hbjson_folders,
            pool_processor="process",
            num_workers=num_workers_processes,
            zone_area=zone_area,
            bipv_scenario_identifier=bipv_scenario_identifier,
            **bipv_scenario_in_dict,
        )
    # Extract results
    run_step(
        step_function=simulation_steps.extract_results,
        run_flag=run_results_extraction,
        list_hbjson_folders=list_hbjson_folders,
        pool_processor="thread",
        num_workers=1,
        path_json_results_file=path_json_results_file,
    )


if __name__ == "__main__":
    main()
