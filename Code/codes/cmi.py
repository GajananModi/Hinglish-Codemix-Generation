# CMI Index calculation
# Find CMI for each sentence by traversing through the file
# input file: contains tags of sentences
# Finding CMI using only tags
# N - total number of tokens exclusing independent tags
# max_cnt - count of words occuring in maximum language
# P - number of switches between langauges
# CMI of a utternace Cu = ((N-max_cnt+P)*100)/(2*N)
import os
import sys
import json
f = open('3_CMI_values.txt', 'w')




tags = {'0':'en', '1':'hi', '2':'unk'}
def utteranceCMI(sentence):
	count = [0,0,1]
	listOfUtterance = sentence.split(" ")
	print(listOfUtterance)
	count[0] = listOfUtterance.count("en")
	count[1] = listOfUtterance.count("hi")
	count[2] = listOfUtterance.count("unk")
	print(count)
	max_cnt = max(count)
	N = count[0]+count[1]
	if N==0:
		return 0
	P = 0
	prev = listOfUtterance[0]
	for i in range(1, len(listOfUtterance)):
		if listOfUtterance[i]!='UN':
			if prev!=listOfUtterance[i]:
				P+=1
				prev = listOfUtterance[i]
	Cu = ((N-max_cnt+P)*100.0)/(2.0*N)
	return Cu



def findCMI(filename):
	f1 = open(filename, 'r')
	avg=[]
	for line in f1:
		if line == '':
			f.write('0')
			f.write('\n')
		else:
			Cu = utteranceCMI(line.strip('\n'))
			avg.append(Cu)
			f.write(str(Cu))
			f.write('\n')
	print(sum(avg)/len(avg))


def M_Idex(k,Pj):
	temp=1-np.sum(np.array(Pj)**2)
	MI=(k-1)*np.sum(np.array(Pj)**2)
	MI=temp/MI
	return MI


def entropy(pj):
	cross_entropy_over_time = - np.dot(pj, np.log2(pj))
	return cross_entropy_ove6r_time



filename=sys.argv[1]
findCMI(filename)
