import random
import sys

filename = '_finalresults.txt'
f = open(filename, 'w')
file1 = open('results1.txt')
lines1 = file1.readlines()
lines1 = [string.strip() for string in lines1]
file1.close()
file2 = open('results2.txt')
lines2 = file2.readlines()
lines2 = [string.strip() for string in lines2]
file2.close()
file3 = open('results3.txt')
lines3 = file3.readlines()
lines3 = [string.strip() for string in lines3]
file3.close()
for i in range (0, 4):
    temp_string1 = lines1[i]
    temp_string2 = lines2[i]
    temp_string3 = lines3[i]
    number1 = temp_string1.split(' : ')[1]
    number2 = temp_string2.split(' : ')[1]
    number3 = temp_string3.split(' : ')[1]
    sum = float(number1) + float(number2) + float(number3)
    result = float(sum) / 3
    string = (str(result) + '\n')
    print(string)
    f.write(string)
f.close()
