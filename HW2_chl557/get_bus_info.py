
'''
@author: Chuan-Heng(Henry) Lin
@project: HW2_bus_line

You can type 
    
    python get_bus_info.py api_key bus_line bus_line.csv

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


# for test purpose
def get_bus_line_from_local():
    
    with open('data.json') as data_file:    
        data = json.load(data_file)
    
    # get bus line numbers
    #pprint(len(data["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"]))
    
    # get lat, lon
    #a = data["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"][0]

    #print(a["MonitoredVehicleJourney"]["OnwardCalls"]["OnwardCall"][1]["StopPointName"])    a = []
    a = []
    for bus in data["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"]:


        lat = bus["MonitoredVehicleJourney"]["VehicleLocation"]["Latitude"]
        lon = bus["MonitoredVehicleJourney"]["VehicleLocation"]["Longitude"]
        if len(bus["MonitoredVehicleJourney"]["OnwardCalls"]["OnwardCall"]) <1:
            stop_name = "N/A"
            status = "N/A"
        else:
            stop_name = bus["MonitoredVehicleJourney"]["OnwardCalls"]["OnwardCall"][1]["StopPointName"]
            status = bus["MonitoredVehicleJourney"]["OnwardCalls"]["OnwardCall"][1]["Extensions"]["Distances"]["PresentableDistance"]
        a.append((lat,lon,stop_name,status))

    with open ("test.csv" ,"w") as f:
        f.write("Latitude, Longitude, Stop Name, Stop Status \n")
        for line in a:
            f.write (', '.join(map(str, line)) + "\n")

def print_result(data,csvname):

    a = []
    for bus in data["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"]:


        lat = bus["MonitoredVehicleJourney"]["VehicleLocation"]["Latitude"]
        lon = bus["MonitoredVehicleJourney"]["VehicleLocation"]["Longitude"]
        if len(bus["MonitoredVehicleJourney"]["OnwardCalls"]["OnwardCall"]) <1:
            stop_name = "N/A"
            status = "N/A"
        else:
            stop_name = bus["MonitoredVehicleJourney"]["OnwardCalls"]["OnwardCall"][1]["StopPointName"]
            status = bus["MonitoredVehicleJourney"]["OnwardCalls"]["OnwardCall"][1]["Extensions"]["Distances"]["PresentableDistance"]
        a.append((lat,lon,stop_name,status))
    with open (csvname ,"w") as f:
        f.write("Latitude,Longitude,Stop Name,Stop Status \n")
        for line in a:
            f.write (', '.join(map(str, line)) + "\n")



    # # get lat, lon
    # for index,bus in enumerate(data["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"]):
    #     lat = bus["MonitoredVehicleJourney"]["VehicleLocation"]["Latitude"]
    #     lon = bus["MonitoredVehicleJourney"]["VehicleLocation"]["Longitude"]
    #     print ("Bus {} is at latitude {} and longitude {}".format(index,lat,lon))


    #a = data["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"][0]

    #print(a["MonitoredVehicleJourney"]["VehicleLocation"])

if __name__ == '__main__':
    
    #get_bus_line_from_local()

    input_key = argv[1]
    bus_line = argv[2]
    filename = argv[3]
    data= get_bus_line(input_key,bus_line)
    print_result(data,filename)
    #print (data)