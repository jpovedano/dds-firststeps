#!/usr/bin/env python 

import time
import random

class Sensor(object):
    def __init__(self, name):
        self.id = name
        self.value = 0

    def readvalue(self):
        # We simulate a sensor by generating random values
        self.value = random.randint(0,100)
        self.timestamp = time.time()
        return self.value
        

if __name__ == '__main__':
    
    import rticonnextdds_connector as rti
    import time
    import argparse
    

    cliparser = argparse.ArgumentParser(description="Connect Sensor simulator")
    cliparser.add_argument("--id", help="sensor identifier", default=0)

    args = cliparser.parse_args()

    connector = rti.Connector("MyParticipantLibrary::Sensor", 'Tutorial.xml')
    writer = connector.getOutput("TempPublisher::TempWriter")


    # Create a sensor
    sensor = Sensor("SENSOR#{}".format(args.id))
        
    while 1:
        sensor.readvalue() 
        writer.instance.setString('id', sensor.id)
        writer.instance.setNumber('value', sensor.value)
        writer.instance.setNumber('timestamp', sensor.timestamp)

        print "[{ts}] Updating sensor {id} value: {value}".format(ts=sensor.timestamp,id=sensor.id, value=sensor.value)
        writer.write()
        time.sleep(1)

