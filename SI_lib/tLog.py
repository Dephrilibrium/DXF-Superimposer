from time import time
from colorama import Fore


t0 = time()


def LogLine(t0, Text):
    print(f"{Fore.BLUE}[{str(time()-t0)}{Fore.RESET}]: ".rjust(15) + Text)