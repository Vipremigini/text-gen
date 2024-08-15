from random import choice
import math
def genmod(data, order):
    mod = {}
    for i in range(0, len(data)-order):
        f = data[i:i+order]
        n = data[i+order]
        if f not in mod:
            mod[f] = {}
        if n not in mod[f]:
            mod[f][n] = 1
        else:
            mod[f][n] += 1
    return mod


def getn(mod, f):
    letters = []
    for letter in mod[f].keys():
        for times in range(0, mod[f][letter]):
            letters.append(letter)
    return choice(letters)

def gen(text, order, length):
    model = genmod(text, order)
    currentf = text[0:order]
    output = ""
    for i in range(0, length-order):
        newc = getn(model, currentf)
        output += newc
        currentf = currentf[1:] + newc
    print( output)


def gentmod(data):
    l = data.split()
    mod = {}
    print(mod)
    for i in range(0,len(l)-1):
        f = l[i]
        n = l[i+1]
        if f not in mod:
            mod[f] = {}
        if n not in mod[f]:
            mod[f][n] = 1
        else:
            mod[f][n] += 1
    mod[l[-1]] = "/n"
    return mod

def getnt(mod, f):
    tokens = []
    for token in mod[f].keys():
        for times in range(0, mod[f][token]):
            tokens.append(token)
    return choice(tokens)

def gent(text,length):
    model = gentmod(text)
    print(model)
    currentt = 'The'
    output = "The "
    for i in range(0, length):
        newt = getnt(model, currentt)
        output += newt + " "
        currentt = newt
    print(output)




f = open("text.txt", "r" )
text = f.read()
gen(text,6,100)
print('next')
gent(text,200)
