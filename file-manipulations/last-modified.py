import os
import json
import pwd

from datetime import datetime

def get_last_modified_time(directory):
    directory = os.path.expanduser(directory)
    files_info_list = []
    
    try:
        files = [file for file in os.listdir(directory) if os.path.isfile(os.path.join(directory, file))] 
        for file in files:
            file_path = os.path.join(directory, file)
            file_modified_time = os.path.getmtime(file_path)
            file_user_id = os.stat(file_path).st_uid
            readable_time = datetime.fromtimestamp(file_modified_time).strftime('%Y-%m-%d %H:%M:%S')
            file_modified_user_name = pwd.getpwuid(file_user_id).pw_name
            
            files_info_list.append({
                "filename": file,
                "last_modified_at": readable_time,
                "last_modified_by": file_modified_user_name
            })
        files_info_list.sort(key=lambda x: x["last_modified_at"], reverse=True)
        
        with open("file_info.json", "w") as file:
            json.dump(files_info_list, file, indent=4)
        print("File information has been saved to file_info.json")
    except FileNotFoundError:
        print(f"Directory {directory} not found.")

get_last_modified_time("~/Downloads")