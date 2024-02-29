import os

def list_files_in_folder(folder_path, store_cmd, db_argument):
    try:
        # Get a list of all files and directories in the specified folder
        files = os.listdir(folder_path)
        
        # Filter out only the files (not directories) from the list
        files_list = [file for file in files if os.path.isfile(os.path.join(folder_path, file))]
        
        # Print the list of file names
        print("Files in the folder:")
        for file_name in files_list:
            print(f"{store_cmd}/{file_name} {db_argument}")
    
    except FileNotFoundError:
        print(f"The specified folder '{folder_path}' was not found.")
    except PermissionError:
        print(f"You don't have permission to access the folder '{folder_path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage: Provide the path to the folder you want to list the files from
folder_path = "D:/Work/Org/GitLocal/hr_documents"
store_cmd = "poetry run store-pdf --id posh --file-path /mnt/d/Work/Org/GitLocal/hr_documents"
db_argument = "--db-name pdf-query"

list_files_in_folder(folder_path, store_cmd, db_argument)
