import os

# path_simulation_folder = r"C:\WorkingFolder\BUA_Python\BUA_00_Default"
# path_simulation_folder = r"C:\WorkingFolder\BUA_Python\BUA_Class_TMP"
# path_simulation_folder = r"C:\WorkingFolder\BUA_Python\BUA_Class_TMP_1"
# path_simulation_folder = r"C:\WorkingFolder\BUA_Python\BUA_01_Context_Targets_FilterContext"
# path_simulation_folder = r"C:\WorkingFolder\BUA_Python\BUA_02_Grid_Irradiation"
# path_simulation_folder = r"C:\WorkingFolder\BUA_Python\BUA_03_UBES"
# path_simulation_folder = r"C:\WorkingFolder\BUA_Python\BUA_Test_04"
path_simulation_folder = r"C:\WorkingFolder\BUA_Python\BUA_Test_All"

path_folder_data = r"C:\WorkingFolder\BUA_Python\Models_Context"
path_folder_data1 = r"C:\WorkingFolder\BUA_Python\Models_Context\hbjson_models"
path_folder_data2 = r"C:\WorkingFolder\BUA_Python\Models_Context\hbjson_models\Buil_Res_0.hbjson"

path_context_file_json = os.path.join(path_folder_data,"geometry_from_brep.json")

path_building_hbjson = os.path.join(path_folder_data1, "Buil_Res_0.hbjson")
# path_building_hbjson = os.path.join(path_folder_data1, "Buil_Res_1.hbjson")
# path_building_hbjson = os.path.join(path_folder_data1, "Buil_Res_2.hbjson")
# path_building_hbjson = os.path.join(path_folder_data1, "Buil_Res_3.hbjson")

path_epw = r"C:\IsraelWeatheFiles_2007-2021_WindStandarized\ISR_TA_Tel.Aviv-Sde.Dov_.AP_.401762_TMYx.2007-2021_WindStandardized_Modified IMS.epw"

cop_heating = 3
cop_cooling = 3

zone_area = 7202.56    # Plot Area
