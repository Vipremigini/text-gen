from random import choice
import math
import re
from nltk import ngrams

f = open("text.txt", "r" )
text = f.read()
text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
text = text.lower()
lst = ngrams(text.split(), 3)
lst = list(n_grams)


def gentmod(lst):
    mod = {}
    for i in range(0,len(lst)):
        f = lst[i][0:2]
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

def gent(text,length):
    model = gentmod(text)
    currentt = choice(mod.keys())
    output = currentt[0]+currentt[1]
    for i in range(0, length):
        newt = getnt(model, currentt)
        output += newt + " "
        currentt = newt
    print(output)




f = open("text.txt", "r" )
text = f.read()
text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
text = text.lower()
print(text)
gen(text,6,100)
print('next')
gent(text,200)
