import os,glob
import re


#v= input("please enter the directory to scan for example: /home/python/    ")
p= input("please enter the pattern to match: ")
v= "C:\\users\\yaul\\"
#p="to"

#ee is the list of files
ee =  glob.glob(str(v)+'*.txt')

i = 0
while i<len(ee):
    print (ee[i])
    i+=1

count = 0
i = 0
x= 0
while x < len(ee):
    myfile = open(ee[x],"r")
    print (ee[x])
    lines = myfile.readlines()
    print(lines[0])
    count = 0
    for line in lines:
        lines_string = ''.join(lines[count])
        match = re.search(p,lines_string)
        if match:
            print(p,"was Found in line:",count,":")
        else:
            print(p,", wan not found in line: ",count)
        count +=1
    x +=1



#    print("line{}: {}".format(count, line.strip