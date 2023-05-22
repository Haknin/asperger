'''
import re

#thank to OR-Yaeer for the help for making this code work

word=input("enter a word: ")
with open("file.txt","r") as file1:

    for line in file1:
        if re.search(word,line):
            print(line)

'''
k==0
k for k in range(0,10,2):
    print(k)
    k+=1
'''
import re
file= "file.txt"
word= input("enter a word")
with open(file,"r") as file_one:
    for line in file_one:
        if re.search(word, line):
            print(line)
'''