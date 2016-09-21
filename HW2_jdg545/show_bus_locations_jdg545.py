from __future__ import print_function
import json
import urllib2
import os
import sys

#Set variables
MTAkey = sys.argv[1]
busLine = sys.argv[2]

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s"%(MTAkey,busLine)

response = urllib2.urlopen(url)
data = response.read().decode("utf-8")

dataDict = json.loads(data)

vehicleInformation = dataDict['Siri']['ServiceDelivery']['VehicleMonitoringDelivery']
numberOfBuses = len(vehicleInformation[0]['VehicleActivity'])

vehicleInformation = dataDict['Siri']['ServiceDelivery']['VehicleMonitoringDelivery']
numberOfBuses = len(vehicleInformation[0]['VehicleActivity'])

print ("Bus Line: " + str(busLine))
print ("Number of Active Buses: " + str(numberOfBuses))

for i in range (0, numberOfBuses):
    print ("Bus " + str(i) + \
           " is at latitude " \
           + str(vehicleInformation[0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude'])\
           + " and longitude " \
           + str(vehicleInformation[0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']))
    
