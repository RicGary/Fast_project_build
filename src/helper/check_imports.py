import os

try:
    import colorama
except ModuleNotFoundError as error:
    os.system("pip install colorama")

try:
    import configparser
except ModuleNotFoundError as error:
    os.system("pip install configparser")