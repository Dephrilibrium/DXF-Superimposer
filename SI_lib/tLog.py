from time import time, strftime, gmtime
from colorama import Fore
from datetime import datetime, timedelta


t0 = time()


def LogLine(Text):
    _t = time() - t0
    _timeStr = str.format("{:3d}d {:02d}h {:02d}m {:02d}.{:03d}s", int((_t)         // 86400),     # days
                                                                    int((_t % 86000) // 3600),      # hours
                                                                    int((_t % 3600)  // 60),        # minutes
                                                                    int((_t)          % 60),       # seconds
                                                                    int((_t % 1)      * 100),        # milliseconds
                                                                    )
    print(f"{Fore.BLUE}[{_timeStr}]{Fore.RESET}: ".ljust(38) + Text)
    return