__author__ = 'thomas@thomas-maier.net'

class CPUDataFileWriter:
    def __init__(self, _filePath):
        self.filePath = _filePath

    def write(self, data):
        fileString = "timestamp,"
        for i,host in enumerate(data[0][1]):
            fileString +=  "%s(%s)" % (host[0], host[1])
            if i < len(data[0][1]) - 1:
                fileString +=  ","
        fileString += "\n"
        for elem in data:
            time = "%s:%s:%s" % (elem[0].tm_hour, elem[0].tm_min, elem[0].tm_sec)
            fileString += "%s," % time
            for i,host in enumerate(elem[1]):
                fileString += "%f" % host[2]
                if i < len(elem[1]) - 1:
                    fileString +=  ","
            fileString +=  "\n"

        f = open(self.filePath, 'w')
        f.write(fileString.rstrip('\n'))
        f.close()