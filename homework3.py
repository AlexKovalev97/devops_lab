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
    elif case == "v_mem_available":
        return format(psutil.virtual_memory().available / 1024 ** 3, '.2f')
    elif case == "v_mem_used":
        return format(psutil.virtual_memory().used / 1024 ** 3, '.2f')
    elif case == "v_mem_free":
        return format(psutil.virtual_memory().free / 1024 ** 3, '.2f')
    elif case == "disk_usage_used":
        return format(psutil.disk_usage('/').used / 1024 ** 3, '.2f')
    elif case == "disk_usage_free":
        return format(psutil.disk_usage('/').free / 1024 ** 3, '.2f')
    elif case == "disk_io_read":
        return psutil.disk_io_counters().read_count
    elif case == "disk_io_write":
        return psutil.disk_io_counters().write_count
    elif case == "net_pack_sent":
        return psutil.net_io_counters().packets_sent
    elif case == "net_pack_received":
        return psutil.net_io_counters().packets_recv


st = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
pid = psutil.Process(os.getpid())
memoryUse = pid.memory_full_info().rss >> 10
l = []
if config.output == "txt":
    for i in range(1, 100):
        tt = time.time()
        st = datetime.datetime.fromtimestamp(tt).strftime('%Y-%m-%d %H:%M:%S')
        pid = psutil.Process(os.getpid())
        memoryUse = pid.memory_full_info().rss >> 10
        print('\nSNAPSHOT', i, st, '\nCPU (%) per each core: ', log("cpu"),
              '\nVirtual Memory available/used/free : ',
              log("v_mem_available"), 'Gb', '/',
              log("v_mem_used"), 'Gb', '/ ', log("v_mem_free"),
              'Gb',
              '\nMemory used/free : ', log("disk_usage_used"),
              ' Gb', '/', log("disk_usage_free"), 'Gb',
              '\nMemory used by script : ',
              memoryUse, 'kB',
              '\nIO read count/write count : ', log("disk_io_read"), '/ ',
              log("disk_io_write"),
              '\nNetwork packets sent/packets received : ',
              log("net_pack_sent"), '/ ', log("net_pack_received"),
              file=open("log.txt", "a"))
        time.sleep(config.interval * 60)
elif config.output == "json":
    for i in range(1, 8):
        tt = time.time()
        st = datetime.datetime.fromtimestamp(tt).strftime('%Y-%m-%d %H:%M:%S')
        pid = psutil.Process(os.getpid())
        memoryUse = pid.memory_full_info().rss >> 10
        json_dict = {
            'SNAPSHOT': i,
            'Timestamp': st,
            'CPU': log("cpu"),
            'ViMemory': log("v_mem_free"),
            'PMemory': log("disk_usage_free"),
            'Used': memoryUse,
            'IO': log("disk_io_write"),
            'Network': log("net_pack_received"),
        }
        l.append(json_dict)
        time.sleep(config.interval * 60)
with open('json_log.json', 'a') as js:
    json.dump(l, js)
print("good")
