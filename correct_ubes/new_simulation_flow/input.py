import os

# path_dir_with_hbjson_alternatives = r"C:\Users\User\OneDrive - Technion\GH\Tanya\14\Alternatives_JSONs"
path_dir_with_hbjson_alternatives = r"C:\Users\User\OneDrive - Technion\GH\Tanya\14\TestAllRuns_Pycharm\Alternatives_JSONs"

list_hbjson_folders = [os.path.join(path_dir_with_hbjson_alternatives, dir_name) for dir_name in
                       os.listdir(path_dir_with_hbjson_alternatives) if
                       os.path.isdir(os.path.join(path_dir_with_hbjson_alternatives, dir_name))]

# path_brep_context = r"C:\Users\User\OneDrive - Technion\GH\Tanya\14\Alternatives_JSONs\Context_from_brep.json"
path_brep_context = r"C:\Users\User\OneDrive - Technion\GH\Tanya\14\TestAllRuns_Pycharm\Alternatives_JSONs\Context_from_brep.json"

# path_dir_simulation_all_alternatives = r"C:\Users\User\OneDrive - Technion\GH\Tanya\14\TestAllRuns_Pycharm\Simulations"
path_dir_simulation_all_alternatives = r"C:\WorkingFolder\BUA_Python\14\TestAllRuns_Pycharm"

path_json_results_file = os.path.join(path_dir_simulation_all_alternatives, "results.json")

path_epw = r"C:\IsraelWeatheFiles_2007-2021_WindStandarized\ISR_TA_Tel.Aviv-Sde.Dov_.AP_.401762_TMYx.2007-2021_WindStandardized_Modified IMS.epw"

cop_heating = 3
cop_cooling = 3

zone_area = 7202.56    # Plot Area



