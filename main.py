#coding:utf-8
#
#	London Tube Visualisation
#

import csv

if __name__ == "__main__":
    with open('stations.csv', 'rb') as csvfile:
        stops = csv.reader(csvfile, delimiter=',', quotechar='"')
        for station in stops:
            print ', '.join(row)