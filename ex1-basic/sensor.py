#!/usr/bin/env python 

import rticonnextdds_connector as rti
import time
import random


class Sensor(object):
    def __init__(self, name):
        self.id = name
        self.value = 0

    def readvalue(self):
        # We simulate a sensor by generating random values
        self.value = random.randint(0,100)
        return self.value
        

if __name__ == '__main__':
    
    connector = rti.Connector("MyParticipantLibrary::Sensor", 'Tutorial.xml')
    writer = connector.getOutput("TempPublisher::TempWriter")

    # Create a sensor
    sensor = Sensor("SENSOR#0")
        
    while 1:
        sensor.readvalue() 
        writer.instance.setString('id', sensor.id)
        writer.instance.setNumber('value', sensor.value)
        writer.instance.setNumber('timestamp', time.time())

        print "Updating sensor {id} value: {value}".format(id=sensor.id, value=sensor.value)
        writer.write()
        time.sleep(1)

