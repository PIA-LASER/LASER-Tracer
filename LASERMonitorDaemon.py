__author__ = 'thomas@thomas-maier.net'

from CPUDataCrawler import CPUDataCrawler
from CPUDataRingBuffer import *
from CPUDataFileWriter import CPUDataFileWriter
import time

hosts = {
    "master":"ec2-46-137-56-240.eu-west-1.compute.amazonaws.com"
}

config = {
    "refresh_data_time":2,
    "save_snapshot_factor":2,
    "buffer_size": 25,
    "hosts":hosts,
    "user":"ubuntu",
    "keyfile":""
}

ringbuffer = RingBuffer(config["buffer_size"])
fileWriter = CPUDataFileWriter("/var/laserstats/cpuusage")

j = 0
while True:
    data = CPUDataCrawler(config).collectData()
    ringbuffer.append(data)
    time.sleep(config["refresh_data_time"])
    if j == config["save_snapshot_factor"]:
        j = 0
        fileWriter.write(ringbuffer.get())
    j += 1

