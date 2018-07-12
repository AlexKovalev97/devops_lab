import datetime
import os
import psutil
import time


def log(case):
    if case == "cpu":
        return psutil.cpu_percent(1, True)
    elif case == "vima":
        return format(psutil.virtual_memory().available / 1024 ** 3, '.2f')
    elif case == "vimu":
        return format(psutil.virtual_memory().used / 1024 ** 3, '.2f')
    elif case == "vimf":
        return format(psutil.virtual_memory().free / 1024 ** 3, '.2f')
    elif case == "duu":
        return format(psutil.disk_usage('/').used / 1024 ** 3, '.2f')
    elif case == "duf":
        return format(psutil.disk_usage('/').free / 1024 ** 3, '.2f')
    elif case == "dcr":
        return psutil.disk_io_counters().read_count
    elif case == "dcw":
        return psutil.disk_io_counters().write_count
    elif case == "ncps":
        return psutil.net_io_counters().packets_sent
    elif case == "ncpr":
        return psutil.net_io_counters().packets_recv


st = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
pid = psutil.Process(os.getpid())
memoryUse = pid.memory_full_info().rss >> 10
json_list = list()
