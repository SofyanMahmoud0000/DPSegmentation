#!/home/sofyan/anaconda3/bin/python3
######################################
# PROGRAMMING ASSIGNMENT
# PROBLEM 1
# AUTHOR    : NAME => SOFYAN MAHMOUD
#           : SEC.: 1
#           : ID => 25
# Time Complexity => (n^2) where (n) is the length of the string 
#################################################################


###################################################
#   LIBRARIES
###################################################
import numpy as np
import re
import datetime
import sys
import json
import csv
from english_words import english_words_set
import math

###################################################
# VARIABLE
###################################################
global cache 
cache = np.zeros((10000,10000))-1


###################################################
#   LOAD INPUT FROM JSON    
###################################################
def ReadJson():
    number = input("Enter the number of example in json file: ")
    f = open("Input.json")
    JsonFile= json.load(f)
    Input= "NoSpaceInput"+str(number)
    Original = "OriginalInput"+str(number)
    if(Input not in JsonFile or Original not in JsonFile):
        return None,None
    return  JsonFile[Input],JsonFile[Original]


###################################################
#   BUILD DICTIONARY    
###################################################
def ReadWords():
    with open('words.csv', mode='r') as infile:
        reader = csv.reader(infile)
        Words = dict((rows[0],rows[1]) for rows in reader)

        Words[","] = 1
        Words["."] = 1
        Words[":"] = 1
        Words[";"] = 1
        Words["?"] = 1
        Words["'"] = 1
        Words["!"] = 1

    return Words

###################################################
#   DYNAMIC PROGRAMMING CODE
###################################################
def DynamicProgramming(Current, Prev):
    if(Current == len(testCase)):
        if(Current == Prev):
            return 0
        return -1e15

    if(cache[Current][Prev] != -1):
        return cache[Current][Prev]

    # Option_1
    Cont = DynamicProgramming(Current+1, Prev)

    # Option_2
    Stop = 0
    if(testCase[Prev:Current+1].lower() in Words):
        Prob = (int((Words[testCase[Prev:Current+1].lower()]))*(math.pow(30,Current+1-Prev)))
        Stop = DynamicProgramming(Current+1, Current+1)+Prob

    cache[Current][Prev] = max(Stop,Cont)
    return cache[Current][Prev]

###################################################
#   BUILD THE OUTPUT OF DYNAMIC PROGRAMMING
###################################################
def Print(Current, Prev):
    global Output
    if(Current == len(testCase)):
        if(Current == Prev):
            return
        return

    # Option_1
    Cont = DynamicProgramming(Current+1, Prev)

    # Option_2
    Stop = 0
    if(testCase[Prev:Current+1].lower() in Words):
        Prob = (int((Words[testCase[Prev:Current+1].lower()]))*(math.pow(30,Current+1-Prev)))
        Stop = DynamicProgramming(Current+1, Current+1)+Prob

    Optimal = DynamicProgramming(Current,Prev)

    if(Optimal == Cont):
        Print(Current+1, Prev)
    elif(Optimal == Stop):
        Output+=testCase[Prev:Current+1]+" "
        Print(Current+1,Current+1)

###################################################
#   REGEX ON THE OUTPUT    
###################################################
def Regex():
    global Output
    Output = re.sub("\s([?]\s)","? ",Output)
    Output = re.sub("\s([,]\s)",", ",Output)
    Output = re.sub("\s([.]\s)",". ",Output)
    Output = re.sub("\s([:]\s)",": ",Output)
    Output = re.sub("\s([;]\s)","; ",Output)
    Output = re.sub("\s([']\s)","' ",Output)
    Output = re.sub("\s([!]\s)","! ",Output)

def OutputF():
    global Output
    Output = re.sub("\s{2,}"," ",Output)
    OutputList = list(re.sub("[.,!?;:']","",Output).split(" "))
    OriginalList = list(re.sub("[.!,;:?']","",Original).split(" "))

    count = 0
    for i in OutputList:
        if i in OriginalList:
            count+=1

    accurecy = (count/len(OutputList)) * 100
    print("============================|")
    print("The input is ")
    print("============================|")
    print(testCase)
    print()
    print("============================|")
    print("The expected output")
    print("============================|")
    print(Original)
    print()
    print("============================|")
    print("The actual output")
    print("============================|")
    print(Output)
    print()
    print("============================|")
    print("The list of the output")
    print("============================|")
    print(OutputList)
    print("============================|")
    print("Some statistics")
    print("============================|")
    print("The accurecy is: ",accurecy,"%")
    print("The number of matched words: ",count)
    print("The number of unmatched words: ",len(OutputList)-count)
    print("The number of all words: ",len(OutputList))
    print("The number of characters: ",len(Output)-Output.count(" "))
    print("The time needed: ",(End-Start).total_seconds(), "seconds")


###################################################
#   MAIN
###################################################
if __name__ == "__main__":

    Words = ReadWords()
    testCase,Original = ReadJson()
    if(testCase is None):
        print("This input doesn't exist in the file json")
        exit()

    testCase = re.sub("\s{2,}"," ",testCase)
    Output = ""

    Start = datetime.datetime.now()
    Print(0,0)
    End = datetime.datetime.now()
    Regex()
    OutputF()