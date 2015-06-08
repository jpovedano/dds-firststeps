#!/usr/bin/env python

import rticonnextdds_connector as rti
import time
import os


def print_header():
    os.system("clear")
    print "{0: <10} {1: <10} {2: <10}".format("ID","VALUE","TIMESTAMP")
    print "-" * 80

conn = rti.Connector("MyParticipantLibrary::Console", 'Tutorial.xml')

reader = conn.getInput("TempSubscriber::TempReader")

while 1:
    reader.read()

    print_header()

    nsamples = reader.samples.getLength()
    for i in range(1,nsamples + 1):
        if reader.infos.isValid(i): 
            s = reader.samples.getDictionary(i)
            print "{id: <10} {val: <10} {ts: <10}".format(id=s["id"],val=s["value"],ts=s["timestamp"])

    time.sleep(1)
