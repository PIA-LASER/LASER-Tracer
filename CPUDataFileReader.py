__author__ = 'thomas@thomas-maier.net'

import os, json

class CPUDataFileReader:
    def __init__(self, _filePath):
        self.filePath = _filePath

    def read(self):
        os.system("cp %s %s.tmp" % (self.filePath, self.filePath))
        f = open("%s.tmp" % self.filePath, 'r')
        jsondata = {}
        firstLine = f.readline().rstrip('\n').split(',')
        linedata = []
        for line in f:
            linedata.append(line)
        for i,host in enumerate(firstLine):
            if i == 0: continue
            hostdata = []
            for j,line in enumerate(linedata):
                values = line.rstrip('\n').split(',')
                hostdata.append([values[0], float(values[i])])
            jsondata[host] = hostdata
        f.close()
        os.system("rm %s.tmp" % (self.filePath))
        return json.dumps(jsondata)
