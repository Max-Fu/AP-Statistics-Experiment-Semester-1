from __future__ import print_function

import random 
import csv

grade9students = 69 
grade10students = 64
grade11students = 69
grade12students = 66

totalstudents = grade9students+grade10students+grade11students+grade12students

print("total students: ", totalstudents)

def gradeAndNumber(selection):
	if selection>totalstudents-grade12students:
		return ["Grade 12", selection-(totalstudents-grade12students), selection]
	if selection>totalstudents-grade12students-grade11students:
		return ["Grade 11", selection-(totalstudents-grade12students-grade11students), selection]
	if selection>grade9students:
		return ["Grade 10", selection-grade9students, selection]
	else:
		return ["Grade 9", selection, selection]

index = []

def checkSelection(randomInt): #selection without repeat
	for x in index:
		if x[2] == randomInt:
			return False
	return True

sample_size = raw_input("what is the desire sample size?")
sample_size = int(sample_size)

i=1
while i<=sample_size:
	print("selection: ", i)
	randomInt = random.randint(1, totalstudents+1)
	if checkSelection(randomInt):
		result = gradeAndNumber(randomInt)
		print(result)
		index.append(result)
		i+=1

file=open('Selection.csv','w')
writer = csv.writer(file)
writer.writerows(index)
file.close() 