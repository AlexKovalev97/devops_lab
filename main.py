import config
import json
import logger
import time


class LogMaker(object):
    @staticmethod
    def makertxt():
        for i in range(1, 100):
            print('\nSNAPSHOT', i, logger.st, '\nCPU (%) per each core: ',
                  logger.log("cpu"),
                  '\nVirtual Memory available/used/free : ',
                  logger.log("vima"), 'Gb', '/',
                  logger.log("vimu"), 'Gb', '/ ', logger.log("vimf"),
                  'Gb',
                  '\nMemory used/free : ', logger.log("duu"),
                  ' Gb', '/', logger.log("duf"), 'Gb',
                  '\nMemory used by script : ',
                  logger.memoryUse, 'kB',
                  '\nIO read count/write count : ', logger.log("dcr"), '/ ',
                  logger.log("dcw"),
                  '\nNetwork packets sent/packets received : ',
                  logger.log("ncps"), '/ ', logger.log("ncpr"),
                  file=open("log.txt", "a"))
            time.sleep(config.interval * 60)

    @staticmethod
    def makerjson():
        for i in range(1, 8):
            json_dict = {
                'SNAPSHOT': i,
                'Timestamp': logger.st,
                'CPU': logger.log("cpu"),
                'ViMemory': logger.log("vimf"),
                'PMemory': logger.log("duf"),
                'Used': logger.memoryUse,
                'IO': logger.log("dcw"),
                'Network': logger.log("ncpr"),
            }
            logger.json_list.append(json_dict)
            time.sleep(config.interval * 60)
            with open('json_log.json', 'a') as js:
                json.dump(logger.json_list, js)
            print("good")


if config.output == "txt":
    LogMaker.makertxt()
elif config.output == "json":
    LogMaker.makerjson()
