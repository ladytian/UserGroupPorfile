import csv
import time

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

def main():
	personinfo = []

	reader = csv.reader(open('./wifi_20180303.csv'))
	reader.next()
	for ids, clientMacAdd, associationTime, updateTime, AP_Name, Status in reader:

		if associationTime == 0 or updateTime == 0:
			break

		data_dict = {}
		location = getLocation(AP_Name)

		data_dict['client_mac'] = clientMacAdd
		data_dict['location'] = location
		data_dict['asstime'] = timestamp_datetime(associationTime)[0:-2]		# Y-M-D
		data_dict['week'] = timestamp_datetime(associationTime).split(' ')[2]
		data_dict['period'] = indexDayTime(timestamp_datetime(associationTime).split(' ')[1])
		data_dict['duration'] = getDuration(associationTime, updateTime)
		data_dict['status'] = Status

		if data_dict not in personinfo:
			personinfo.append(data_dict)

	output = open('all.csv', 'w')
	for i in personinfo[0]:
		output.write(str(i)+',')	
	output.write('\n')

	for info in personinfo:
		for i in info:
			output.write(str(info[i])+',')
		output.write('\n')

if __name__ == '__main__':
	main()
