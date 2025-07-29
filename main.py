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
    :param num_processes:
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

    # Loop over all the alternatives
    for path_folder_hbjson in list_hbjson_folders:
        # Get the path to the simulation folder
        name_simulation_folder = path_folder_hbjson.split("\\")[-1]
        path_simulation_folder = os.path.join(
            path_dir_simulation_all_alternatives, name_simulation_folder
        )
        # Check if simulated already in the json file
        print(
            "Path folder hbjson: \n",
            path_folder_hbjson,
            "\n name ",
            name_simulation_folder,
            "\n Path simulation folder: ",
            path_simulation_folder,
        )
        # print(path_simulation_folder,'\n',
        #                 path_folder_hbjson,'\n',
        #                 path_brep_context,'\n',
        #                 path_epw,'\n',
        #                 cop_heating,'\n',
        #                 cop_cooling,'\n',
        #                 zone_area)

        # #########################################################
        get_results_only = True  # Pay attention to this one  ###
        # TRUE if you want to get results ONLY. Don't run cases ###
        # FALSE if you need to run all cases                    ###
        # #########################################################

        if name_simulation_folder not in json_dict.keys():
            # run all the alternatives
            result_dict = run_alternative(
                path_simulation_folder=path_simulation_folder,
                path_folder_hbjson=path_folder_hbjson,
                path_context_file_json=path_brep_context,
                path_weather_file=path_epw,
                cop_heating=cop_heating,
                cop_cooling=cop_cooling,
                zone_area=zone_area,
                get_results_only=get_results_only,
            )

            json_dict[name_simulation_folder] = result_dict

            with open(path_json_results_file, "w") as outfile:
                json.dump(json_dict, outfile)

            print(json_dict[name_simulation_folder]["ubes"]["heating"]["yearly"])

    # Create json result file
    if not os.path.isfile(path_json_results_file):
        json_dict = {}
        with open(path_json_results_file, "w") as outfile:
            json.dump(json_dict, outfile)

    with open(path_json_results_file, "r") as infile:
        json_dict = json.load(infile)


if __name__ == "__main__":
    main()
