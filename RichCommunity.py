#! usr/bin/python

import sys

input_file = open("input_file.txt", "r")
output_file = open("output_file.txt", "w")

#Counting Number of lines in input file
ln = 0
for i in input_file.read().split("\n"):
    if i:
        ln += 1

#Moving cursor to top of the file
input_file.seek(0,0)

a = []
a_i = 0
for a_i in range(ln):
	a_i = input_file.readline().strip()
	a.append(a_i)
input_file.close();

window_size = 0;
A = []

for test_case in a:
    a = test_case.split("::");

    for item in a[1].split():
        temp = int(item)
        A.append(temp)
    
    #output_file.write("+"\n")

output_file.close()