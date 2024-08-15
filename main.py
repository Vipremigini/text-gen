from random import choice
import math
import re


f = open("text.txt", "r" )
text = f.read()
text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
text = text.lower()
s = text.split()
lst = []
for i in range(len(s)-2):
    k = [s[i],s[i+1],s[i+2]]
    k = tuple(k)
    lst.append(k)



def gentmod(lst):
    mod = {}
    for i in range(len(lst)):
        
        f = (lst[i][0],lst[i][1])
        n = lst[i][2]
        if f not in mod:
            mod[f] = {}
        if n not in mod[f]:
            mod[f][n] = 1
        else:
            mod[f][n] += 1
    return mod

def getnt(mod, f):
    tokens = []
    for token in mod[f].keys():
        for times in range(0, mod[f][token]):
            tokens.append(token)
    return choice(tokens)

def gent(lst,length, mod):
    currentt = choice(list(mod.keys()))
    output = currentt[0]+ " " +currentt[1] + " " 
    for i in range(0, length):
        newt = getnt(mod, currentt)
        output += newt + " "
        currentt = (currentt[1],newt)
    return output


