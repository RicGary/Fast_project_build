""" 
Descontinued
"""

import os
import sys

from src.helper.check_imports import *
from src.utils.create_files import create_directory, create_file
from src.utils.color_text import *

desired_directory = sys.argv[1]
desired_project_name = sys.argv[2]

def create_project_structure(directory: str, project_name: str) -> None:
    """
    Creates the directory structure and necessary files for a project.

    Args:
        directory (str): The directory path where the project will be created.
                         If set to ".", the current working directory is used.
        project_name (str): The name of the project.

    Returns:
        None

    Raises:
        SystemExit: If the user chooses not to proceed when prompted.

    Note:
        This function assumes that necessary helper functions, create_directory
        and create_file, are defined elsewhere in the code.

    """

    if directory == ".":
        directory = os.getcwd()

    else:
        wrong_dir = input(f"Creating inside {os.path.join(os.getcwd(), directory)}, are you sure? (y/n) \n")
        if wrong_dir == "n":
            print(Fore.RED + "Exiting...")
            sys.exit()
    
    directories_created = []
    files_created = []

    gitignore_content = open(r"D:\Programming\Codes\Fast_project_structure\assets\gitignore.txt").read()

    root_dir = os.path.join(directory, project_name)
    # Project root directory
    if not os.path.exists(root_dir):
        os.makedirs(root_dir)
        directories_created.append(root_dir)

    # Directories    
    directories_created.append(create_directory(root_dir, 'src'))
    directories_created.append(create_directory(root_dir, 'src/helper'))
    directories_created.append(create_directory(root_dir, 'src/utils'))
    directories_created.append(create_directory(root_dir, 'tests'))
    directories_created.append(create_directory(root_dir, 'docs'))

    # Files
    files_created.append(create_file(root_dir, 'README.md'))
    files_created.append(create_file(root_dir, 'requirements.txt'))
    files_created.append(create_file(root_dir, 'main.py'))
    files_created.append(create_file(root_dir, '.gitignore', gitignore_content))
    files_created.append(create_file(root_dir, '.env'))
    files_created.append(create_file(root_dir, '.config'))
    
    # Created files
    print("Created Directories:")
    for directory in directories_created:
        red(directory)
    blue(25 * "-")
    print("Created files:")
    for file_ in files_created:
        red(file_)

# Example usage
if __name__ == "__main__":
    create_project_structure(desired_directory, desired_project_name)
