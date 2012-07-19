from itty import get, run_itty
from CPUDataFileReader import CPUDataFileReader

dataReader = CPUDataFileReader("/home/ubuntu/Laser/cpuusage")

@get('/data')
def index(request):
    return dataReader.read()

@get('/')
def index(request):
    htmlfile = open('graph.html', 'r')
    contents = htmlfile.readlines()
    htmlfile.close()
    return contents

run_itty(host='0.0.0.0')

