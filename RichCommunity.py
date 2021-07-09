#! usr/bin/python
import sys
#function to get the maximum number between the given range of the list.
def rangeMax(start, end, type) :
    res = 0;
    for idx in range(start, end):
        if type == 1 : #to search in input list
            res = max(A[idx], res)
        if type == 2 : #to search in tempeorary list
            res = max(TEMP[idx], res)
    return res;
#Input/Output Handling
input_file = open("input_file.txt", "r")
output_file = open("output_file.txt", "w")
#Counting Number of lines in input file
ln = 0
for i in input_file.read().split("\n"):
    if i:
        ln += 1
#Moving cursor to top of the file
input_file.seek(0,0)

a = [] #input in list format (line-wise)
for a_i in range(ln):
	a_i = input_file.readline().strip()
	a.append(a_i)
input_file.close(); #closing input file

window_size = 0 #max-size of a community
A = [] #List to store people's wealth
ANS = [] #List to store Maximum Possible Wealth.
TEMP = [] #List for storing different combination for each Input person

#Start of main logic.
for test_case in a:
    a = test_case.split("::") #Split the line where :: exsist
    
    window_size = int(a[0]) #Getting max group size.
    #To get the indivisual item from the line 
    #and store it in the list A
    for item in a[1].split():
        A.append(int(item))
    
    count = 0
    #Working on each input one by one.
    for item in A:
        count += 1
        #If number of people less then the max group size then to maximise
        #wealth get the max value of an item and multiply with the count.
        if count <= window_size :
            #Store the max value which will be used in later stages
            ANS.append(rangeMax(0,count,1)*count)
        else :
            #Generate the possible combination form 0 to max-group size.
            for k in range(window_size) :
                TEMP.append(
                    ANS[count-window_size+k-1] #Getting previous maximum wealth for permutation.
                        + rangeMax(count-window_size+k, count, 1)*(window_size-k)) 
            ANS.append(rangeMax(0, window_size, 2)) #Find the max number in the TEMP list.
            TEMP.clear()
    output_file.write("%d"%ANS[count-1]+"\n") #Write the output in the file
    ANS.clear()
    A.clear()
output_file.close() #Closing output file.