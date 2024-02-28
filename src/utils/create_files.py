import os

def create_directory(project_location: str, new_directory: str) -> str:
    """ Create new directory

    Args:
        project_location (str): Path to the project location.
        new_directory (str): Directory name.

    Returns:
        str: Name/path of directory created
    """
    if not os.path.exists(os.path.join(project_location, new_directory)):
        os.makedirs(os.path.join(project_location, new_directory))
    
    return os.path.join(project_location, new_directory)

def create_file(project_location: str, file_name:str, content:str = "") -> str:
    """ Create new file.

    Args:
        project_location (str): Path to the project location.
        file_name (str): File name
        content (str): Content of the file

    Returns:
        str: Name/path of file created
    """
    if not os.path.isfile(os.path.join(project_location, file_name)):
        with open(os.path.join(project_location, file_name), 'w') as f:
            f.write(content)
    
    return os.path.join(project_location, file_name)