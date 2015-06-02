#!/usr/bin/env python 

import rticonnextdds_connector as rti
import time
import random


connector = rti.Connector("MyParticipantLibrary::Sensor", 'Tutorial.xml')

writer = connector.getOutput("TempPublisher::TempWriter")


sensorid = "SENSOR#0"

    
while 1:
    sensorvalue = random.randint(0,100)

    writer.instance.setString('id', sensorid)
    writer.instance.setNumber('value', sensorvalue)
    print "Updating sensor {id} value: {value}".format(id=sensorid, value=sensorvalue)
    writer.write()
    time.sleep(1)

