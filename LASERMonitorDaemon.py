__author__ = 'thomas@thomas-maier.net'

from CPUDataCrawler import CPUDataCrawler
from CPUDataRingBuffer import *
from CPUDataFileWriter import CPUDataFileWriter
import time

hosts = {
	"master":"localhost",
	"slave1":"slave1",
	"slave2":"slave2",
	"slave3":"slave3",
	"slave4":"slave4"
}

config = {
    "refresh_data_time":1,
    "save_snapshot_factor":1,
    "buffer_size": 50,
    "hosts":hosts,
    "user":"ubuntu",
    "keyfile":"/home/ubuntu/.ssh/id_rsa"
}

ringbuffer = RingBuffer(config["buffer_size"])
fileWriter = CPUDataFileWriter("/home/ubuntu/Laser/cpuusage")

j = 0
while True:
    data = CPUDataCrawler(config).collectData()
    ringbuffer.append(data)
    time.sleep(config["refresh_data_time"])
    if j == config["save_snapshot_factor"]:
        j = 0
        fileWriter.write(ringbuffer.get())
    j += 1

