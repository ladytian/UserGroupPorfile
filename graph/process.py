import os
import csv
import pylab as plt
import string
import time
import networkx as nx
import matplotlib.pyplot as plt

def timestamp_datetime(associationTime):
	format = '%Y-%m-%d %H:%M:%S %w'
	value = time.localtime(int(associationTime) / 1000)
	dt = time.strftime(format, value)
	return dt

def getDayTime(time):
	info = time.split(':')
	return int(info[0]) * 60 + int(info[1])

def indexDayTime(time):
	dayTime = getDayTime(time)
	if dayTime >= getDayTime('7:00:00') and dayTime <= getDayTime('9:40:00'):
		return 1
	elif dayTime > getDayTime('9:40:00') and dayTime <= getDayTime('10:10:00'):
		return 2
	elif dayTime > getDayTime('10:10:00') and dayTime <= getDayTime('11:50:00'):
		return 3
	elif dayTime > getDayTime('11:50:00') and dayTime <= getDayTime('14:00:00'):
		return 4
	elif dayTime > getDayTime('14:00:00') and dayTime <= getDayTime('15:40:00'):
		return 5
	elif dayTime > getDayTime('15:40:00') and dayTime <= getDayTime('16:10:00'):
		return 6
	elif dayTime > getDayTime('16:10:00') and dayTime <= getDayTime('17:50:00'):
		return 7
	elif dayTime > getDayTime('17:50:00') and dayTime <= getDayTime('21:00:00'):
		return 8
	else:
		return 0

def getDuration(asstime, updtime):
	dur = (int(updtime) - int(asstime)) / (1000 * 60)
	return dur

def getLocation(ap_name):
	if len(ap_name.split('-')) <= 2:
		loc = ap_name
	else:
		loc = ap_name.split("-")[0] + "-" + ap_name.split("-")[1]
	return loc

def getNodes(information):
	mac = []
	for f in information:
		mac.append(f[0])
	return mac

def  getEdges(information):

	list_edges = []

	for i in range(0, len(information)):
		w = 0
		for j in range(i+1, len(information)):
			if information[i][1] == information[j][1]: 
				if information[i][3] == information[j][3]:
					if information[i][4] == information[j][4]:
						list_edges.append((i, j, {'weight':w}))

	return list_edges

			

def main():

	info = []
	reader = csv.reader(open('./20180304.csv'))
	
	data_list = []
	clientname =""

	mac = []
	list_date = []
	list_week = []
	list_per = []
	list_dur = []
	list_loc = []

	reader.next()
	for ids, clientMacAdd, associationTime, updateTime, AP_Name, status in reader:
		if associationTime == '0' or len(AP_Name) < 1:
			continue

		if clientMacAdd not in mac:
			data_list.append(clientname)
			data_list.append(list_date)
			data_list.append(list_week)
			data_list.append(list_per)
			data_list.append(list_dur)
			data_list.append(list_loc)

			if len(data_list[0]) > 0:
				info.append(data_list)

			mac.append(clientMacAdd)

			data_list = []
			list_date = []
			list_week = []
			list_per = []
			list_dur = []
			list_loc = []

			clientname = clientMacAdd
			
			list_date.append(timestamp_datetime(associationTime).split(' ')[0])
			list_week.append(timestamp_datetime(associationTime).split(' ')[2])
			list_per.append(indexDayTime(timestamp_datetime(associationTime).split(' ')[1]))
			list_dur.append(int(getDuration(associationTime, updateTime)))
			list_loc.append(getLocation(AP_Name))

		elif clientMacAdd in mac:
			list_date.append(timestamp_datetime(associationTime).split(' ')[0])
			list_week.append(timestamp_datetime(associationTime).split(' ')[2])
			list_per.append(indexDayTime(timestamp_datetime(associationTime).split(' ')[1]))
			list_dur.append(int(getDuration(associationTime, updateTime)))
			list_loc.append(getLocation(AP_Name))

	getEdges(info)


	#print len(info), info[0:10]
	#print "success!"
'''
	nodes = getNodes(info)
	#print len(nodes)
	g = nx.Graph()
	g.add_nodes_from(nodes)

	#to draw the network
	nx.draw_random(g, node_size=5)
	#nx.draw(g, node_size=5)

	plt.show()
'''

if __name__ == '__main__':
	main()