
'''
@author: Chuan-Heng(Henry) Lin
@project: HW2_bus_line

You can type 
    
    python show_bus_location.py api_key bus_line

on your command line to execute this program

'''

from sys import argv
import requests
import json
from pprint import pprint


# def get_bus_line(input_key, bus_line):
    
#     parameter = {
#       'key': input_key,
#       'version': "2",
#       'LineRef': bus_line,
#       }

#     url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json"
#     response = requests.get(url,params=parameter)
#     data = response.json()
#     return data

def get_bus_line(input_key, bus_line):
    
    url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key="+input_key+"&VehicleMonitoringDetailLevel=calls&LineRef="+bus_line
    response = requests.get(url)
    data = response.json()
# dump json file to local 
    # with open('data.json', 'w') as outfile:
    #     json.dump(data, outfile)
    return data



def get_bus_line_from_local():
    
    with open('data.json') as data_file:    
        data = json.load(data_file)
    
    # get bus line numbers
    pprint(len(data["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"]))
    
    # get lat, lon
    a = data["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"][0]

    print(a["MonitoredVehicleJourney"]["VehicleLocation"])


def print_result(data,bus_line):

    print ("Bus Line : {}".format(bus_line))
    #get bus line numbers 
    num_of_bus = len(data["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"])
    
    print ("Number of Active Buses : {}".format(num_of_bus))
    
    # get lat, lon
    for index,bus in enumerate(data["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"]):
        lat = bus["MonitoredVehicleJourney"]["VehicleLocation"]["Latitude"]
        lon = bus["MonitoredVehicleJourney"]["VehicleLocation"]["Longitude"]
        print ("Bus {} is at latitude {} and longitude {}".format(index,lat,lon))


    #a = data["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"][0]

    #print(a["MonitoredVehicleJourney"]["VehicleLocation"])

if __name__ == '__main__':
    
    #get_bus_line_from_local()

    input_key = argv[1]
    bus_line = argv[2]
    data= get_bus_line(input_key,bus_line)
    print_result(data,bus_line)
    # print (data)