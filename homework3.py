# from __future__ import print_function
import config
import datetime
import json
import os
import psutil
import time
print(config.interval)
print(config.output)


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
l = list()
if config.output == "txt":
    for i in range(1, 100):
        tt = time.time()
        st = datetime.datetime.fromtimestamp(tt).strftime('%Y-%m-%d %H:%M:%S')
        pid = psutil.Process(os.getpid())
        memoryUse = pid.memory_full_info().rss >> 10
        print('\nSNAPSHOT', i, st, '\nCPU (%) per each core: ', log("cpu"),
              '\nVirtual Memory available/used/free : ', log("vima"), 'Gb', '/',
              log("vimu"), 'Gb', '/ ', log("vimf"),
              'Gb',
              '\nMemory used/free : ', log("duu"), ' Gb', '/', log("duf"), 'Gb',
              '\nMemory used by script : ',
              memoryUse, 'kB',
              '\nIO read count/write count : ', log("dcr"), '/ ', log("dcw"),
              '\nNetwork packets sent/packets received : ', log("ncps"), '/ ', log("ncpr"),
              file=open("log.txt", "a"))
        time.sleep(config.interval * 60)
elif config.output == "json":
    for i in range(1, 8):
        st = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
        pid = psutil.Process(os.getpid())
        memoryUse = pid.memory_full_info().rss >> 10
        json_dict = {
            'SNAPSHOT': i,
            'Timestamp': st,
            'CPU': log("cpu"),
            'ViMemory': log("vimf"),
            'PMemory': log("duf"),
            'Used': memoryUse,
            'IO': log("dcw"),
            'Network': log("ncpr"),
        }
        l.append(json_dict)
        time.sleep(config.interval * 60)
with open('json_log.json', 'a') as js:
    json.dump(l, js)
print("good")
