import os

def get_files_info(working_directory, directory=None):
    working_directory_absolute_path = os.path.abspath(working_directory)
    directory_absolute_path = os.path.abspath(working_directory + "/" + directory)

    if not directory_absolute_path.startswith(working_directory_absolute_path):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    if not os.path.isdir(directory_absolute_path):
        return f'Error: "{directory}" is not a directory'
    
    return_string_list = []

    contents = os.listdir(directory_absolute_path)
    for content in contents:
        if "." in content:
            # It's a file
            file_path = directory_absolute_path + "/" + content
            file_size_bytes = get_file_size(file_path)
            return_string_list.append(f'- {content}: file_size={file_size_bytes} bytes, is_dir=False')
        else:
            # It's a folder
            folder_path = directory_absolute_path + "/" + content
            folder_size_bytes = get_folder_size(folder_path)
            return_string_list.append(f'- {content}: file_size={folder_size_bytes} bytes, is_dir=True')
    returned_string = "\n".join(return_string_list)
    return returned_string

def get_folder_size(folder):
    contents = os.listdir(folder)
    size_bytes = 0
    for content in contents:
        if "." in content:
            # It's a file
            file_size_bytes = get_file_size(folder + "/" + content)
            size_bytes += file_size_bytes
        else:
            # It's a folder
            folder_size_bytes = get_folder_size(folder + "/" + content)
            size_bytes += folder_size_bytes
    return size_bytes
        

def get_file_size(file):
    return os.path.getsize(file)