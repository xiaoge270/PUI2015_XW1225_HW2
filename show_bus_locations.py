import json
import sys
import urllib2

if __name__=='__main__':
    #your_key = 'b988b6ae-6da2-4e25-9b40-6038b226fe0e'
    #bus = 'M42'
    url = 'http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s' % (sys.argv[1],sys.argv[2])
      
    request = urllib2.urlopen(url)
    metadata = json.loads(request.read())
    
    print "Bus Line : %s " %(sys.argv[2])
    count = len(metadata['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'])
    print "Number of Active Buses : %s" %(count)        
    
    for i in range(count):
        latitude = metadata['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
        longitude = metadata['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
        print "Bus %s is at latitude %s and longitude %s" %(i,latitude,longitude)
        count +=1
    
    
    