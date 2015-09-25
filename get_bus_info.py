import json
import sys
import csv
import urllib2

if __name__=='__main__':
    #your_key = 'b988b6ae-6da2-4e25-9b40-6038b226fe0e'
    #bus = 'M42'
    url = 'http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s' % (sys.argv[1],sys.argv[2])
      
    request = urllib2.urlopen(url)
    metadata = json.loads(request.read())
    
    buses =metadata['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
    
    #file = 'M42.csv'
    with open(sys.argv[3], 'wb') as csvFile:
        writer = csv.writer(csvFile)
        headers = ['Latitude', 'Longitude', 'StopName','StopStatus']
        writer.writerow(headers)
        
        for i in buses:
            Latitude = buses['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
            Longitude = buses['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
            if buses['MonitoredVehicleJourney']['OnwardCalls'] =="":
                StopName = 'N/A'
                StopStatus = 'N/A'
            else:
                StopName = buses['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']
                StopStatus = buses['MonitoredVehicleJourney']['MonitoredCall']['Extensions']['Distances']['PresentableDistance']
                
                writer.writerow([Latitude, Longitude, StopName,StopStatus])
                