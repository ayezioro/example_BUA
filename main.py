import json

from input import *
from run_alternative_fct import run_alternative


def main():

    # Run the simulation for all alternatives

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
