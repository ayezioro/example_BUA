import os
from input_data import *

def main():
    path = path_alternatives_folders
    path_simulation = path_simulation_folders

    # Dictionary to store folder names and their .hbjson files (with full paths)
    hbjson_files = {}

    # Ensure simulation output base folder exists
    if not os.path.exists(path_simulation):
        os.makedirs(path_simulation)

    # List only subdirectories
    folders = [name for name in os.listdir(path)
               if os.path.isdir(os.path.join(path, name))]

    for folder in folders:
        folder_path = os.path.join(path, folder)
        files = []

        for f in os.listdir(folder_path):
            full_file_path = os.path.join(folder_path, f)
            if f.lower().endswith('.hbjson') and os.path.isfile(full_file_path):
                files.append((f, full_file_path))

        if files:
            hbjson_files[folder] = files

            # === Create simulation folder ===
            sim_folder = os.path.join(path_simulation, folder)
            if not os.path.exists(sim_folder):
                os.makedirs(sim_folder)
                print(f"Created simulation folder: {sim_folder}")
            else:
                print(f"Simulation folder already exists: {sim_folder}")

    # Optional: print results
    for folder, file_list in hbjson_files.items():
        print(f"In folder '{folder}':")
        for file_name, full_path in file_list:
            #print(f"    Full path: {full_path}")
            pass

if __name__ == '__main__':
    main()
