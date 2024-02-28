from colorama import Fore, Style

def red(text: str) -> None:
    print(Fore.RED + text + Style.RESET_ALL)

def green(text: str) -> None:
    print(Fore.GREEN + text + Style.RESET_ALL)

def blue(text: str) -> None:
    print(Fore.BLUE + text + Style.RESET_ALL)