#! usr/bin/python

import sys

def rangeMax(start, end, type) :
    res = 0;
    for idx in range(start, end):
        if type == 1 :
            res = max(A[idx], res)
        if type == 2 :
            res = max(TEMP[idx], res)
    return res;

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
ANS = []
TEMP = []
for test_case in a:
    a = test_case.split("::");
    
    window_size = int(a[0])

    for item in a[1].split():
        temp = int(item)
        A.append(temp)
    
    count = 0;
    for item in A:
        count += 1;
        if count <= window_size :
            ANS.append(rangeMax(0,count,1)*count)
        else :
            for k in range(window_size) :
                TEMP.append(ANS[count-window_size+k-1] + rangeMax(count-window_size+k, count, 1)*(window_size-k))
            ANS.append(rangeMax(0, window_size, 2));
            TEMP.clear();
    output_file.write("%d"%ANS[count-1]+"\n")
    ANS.clear()
    A.clear()
output_file.close()