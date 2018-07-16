import csv
from matplotlib import pyplot as plt
data_str = []
data_time = []
firstrow=True

#read file
with open('C_C2C3flux.csv', 'rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter='\t')
	for row in spamreader:	
		if firstrow:
			firstrow=False
		else:
			data_str.append(row)
print(data_str)
print('...........................')
#remove whitespaces in data
for pair in data_str:
	for i in range(len(pair)):
		pair[i] = pair[i].replace(" ","")

print(data_str)


#convert data to float and store in new array
data = [None]*len(data_str)
for j in range(len(data_str)):
	pair = data_str[j]
	data[j] = [float(pair[i]) for i in range(len(pair)) if pair[i]!=''] 

ratios = [float(pair[0])/float(pair[1]) for pair in data]

firstrow = True

#read second file
with open('C_JDtime.csv', 'rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter='\t')
	for row in spamreader:	
		if firstrow:
			firstrow=False
		else:
			data_time.append(row)

#remove whitespaces in data from second file
for time in data_time:
	for i in range(len(time)):
		time[i] = time[i].replace(" ","")

times = [float(time[0]) for time in data_time]

#convert data to float and restore in second file
# data_time[j] = [float(time[i]) for i in range(len(time)) if time[i]!=''] 

# time = data_time


plt.plot(ratios, times)
plt.xlabel('Julian Date')
plt.ylabel('Ratio of C2 Flux and C3 Flux')
plt.show()




# make sure both sets of data are the same length, and that you are editing the correct file