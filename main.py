#coding:utf-8
#
#	London Tube Visualisation
#

import csv

def x_pos(time_string):
    x = 0
    parts = time_string.split(':')
    if parts[2] == '30':
        x += 1
    x += (int(parts[1])*2)
    x += (int(parts[0])*60)
    return str(x)
    
def line_color(line):
    lines = {'circle':'#ff0000'}
    return lines.get(line,'#999999')
    
if __name__ == "__main__":
    all_stations = []
    svg = '<svg xmlns="http://www.w3.org/2000/svg" version="1.1">'
    with open('stations.csv', 'rb') as csvfile:
        stops = csv.reader(csvfile, delimiter=',', quotechar='"')
        
        # get a list of all the stations
        for journey in stops:
            station_from = journey[0]
            station_to   = journey[2]
            if station_from not in all_stations:
                all_stations.append(station_from)
            if station_to not in all_stations:
                all_stations.append(station_to)
        
        # sort them alphabetically
        # this might not be a good idea?
        all_stations.sort()
        
        
        counter = 15
        station_y = {}
        for station in all_stations:
            station_y[station] = counter
            counter += 20
            
        for station in station_y:
            svg += '<text y="'+str(station_y[station])+'" x="0">'+station+'</text>'
        
        # reset the cursor back to the beginning
        csvfile.seek(0)
        
        # start to make the lines between stations
        for journey in stops:
            station_from = journey[0]
            station_to   = journey[2]
            start_time = journey[1]
            end_time   = journey[3]
            line       = journey[4]
            
            svg += '<line x1="'+x_pos(start_time)+'" y1="'+str(station_y[station_from])+'" x2="'+x_pos(end_time)+'" y2="'+str(station_y[station_to])+'" style="stroke:'+line_color(line)+';stroke-width:2"/>'
        
    print svg+'</svg>'
    
