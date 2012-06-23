__author__ = 'thomas@thomas-maier.net'

import os, re, time

class CPUDataCrawler():

    def __init__(self, configuration):
        self.hosts = configuration["hosts"]
        self.user = configuration["user"]
        self.keyfile = configuration["keyfile"]

    def collectData(self):
        hostdata = []
        for host in self.hosts:
            command = "ssh %s@%s -i %s \"top -b -n 1 | grep 'Cpu(s):'\"" % (self.user, self.hosts[host], self.keyfile)
            cpustr = os.popen(command).read()
            contents = cpustr.split(",")
            cpusum = 0
            for elem in contents:
                if re.search('%us|%sy', elem):
                    elem = re.sub('[^0-9.]', '', elem)
                    cpusum += float(elem)
            hostdata.append((host, self.hosts[host], cpusum))
        return (time.localtime(), hostdata)
