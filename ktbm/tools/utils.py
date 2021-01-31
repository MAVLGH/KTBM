import os
import fnmatch


def get_all_files(root, pattern='*', extension='.csv', lowerize=False):
    """

    Get all the tree path from a root path filtering by a pattern an a extension

    :param root:
    :param pattern:
    :param extension:
    :param lowerize:
    :return:
    """
    path_files = []
    root = os.path.normpath(root)
    pattern = pattern.lower() if lowerize else pattern
    for root, dirs, files in os.walk(root):
        for f in files:
            full_path_file = os.path.join(root, f)
            full_path_file_ = full_path_file.lower() if lowerize else full_path_file
            if fnmatch.fnmatch(full_path_file_, pattern) and extension in full_path_file:
                path_files.append(full_path_file)
    return path_files
