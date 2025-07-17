import os

path_simulation_folder = r"C:\WorkingFolder\BUA_Python\Simulation"
path_folder_data = r"C:\WorkingFolder\BUA_Python\HBJSON_Models"

path_context_file_json = os.path.join(path_folder_data,"geometry_from_brep.json")
path_folder_building_hbjson = os.path.join(path_folder_data,"_No_Context")

path_epw = ""

cop_heating = 3
cop_cooling = 3
