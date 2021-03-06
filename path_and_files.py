
import os


def get_file_path(file_path):
    file_paths = []
    root_dir = os.walk(file_path)

    for sub_dir, folder_name, file_list in root_dir:
        for file_name in file_list:
            file_path = os.path.join(sub_dir, file_name)
            file_paths.append(file_path)
    file_paths = sorted(file_paths)
    return file_paths


def get_file_path_with_type(file_path, file_type):
    file_paths = []
    root_dir = os.walk(file_path)

    for sub_dir, folder_name, file_list in root_dir:
        for file_name in file_list:
            file_path = os.path.join(sub_dir, file_name)
            if file_type in file_path:
                file_paths.append(file_path)
    file_paths = sorted(file_paths)
    return file_paths


def check_path(path):
    if not os.path.isdir(path):
        os.makedirs(path)
    return path


def get_file_name(file_path):
    file_full_name = os.path.basename(file_path)
    file_name, extension_name = os.path.splitext(file_full_name)
    if os.path.isfile(file_path):
        return file_name
    else:
        return False

