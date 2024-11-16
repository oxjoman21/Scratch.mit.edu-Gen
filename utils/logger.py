from colorama import Fore

class Logger:
    def suc(self, message, type):
        print(f"{Fore.LIGHTMAGENTA_EX}[Joman21] {Fore.MAGENTA}[{type}] {Fore.LIGHTGREEN_EX}[SUC]{Fore.LIGHTBLACK_EX} --> {Fore.LIGHTGREEN_EX}{message}{Fore.RESET}")

    def err(self, message, type):
        print(f"{Fore.LIGHTMAGENTA_EX}[Joman21] {Fore.MAGENTA}[{type}] {Fore.LIGHTRED_EX}[ERR]{Fore.LIGHTBLACK_EX} --> {Fore.LIGHTRED_EX}{message}{Fore.RESET}")

    def inf(self, message, type):
        print(f"{Fore.LIGHTMAGENTA_EX}[Joman21] {Fore.MAGENTA}[{type}] {Fore.LIGHTBLUE_EX}[INF]{Fore.LIGHTBLACK_EX} --> {Fore.LIGHTBLUE_EX}{message}{Fore.RESET}")