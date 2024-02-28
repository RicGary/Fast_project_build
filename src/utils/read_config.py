import configparser

def read_config_file(file_path):
    # Initialize the ConfigParser object
    config = configparser.ConfigParser()

    # Read the configuration file
    config.read(file_path)

    # Access sections and their options
    for section in config.sections():
        print(f"[{section}]")
        for option in config.options(section):
            value = config.get(section, option)
            print(f"{option} = {value}")
