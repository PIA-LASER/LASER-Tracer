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
            command = "ssh %s@%s -i %s \"cat /proc/loadavg\"" % (self.user, self.hosts[host], self.keyfile)
            cpustr = os.popen(command).read()
            contents = cpustr.split(" ")
            hostdata.append((host, self.hosts[host], float(contents[0])))
        return (time.localtime(), hostdata)
