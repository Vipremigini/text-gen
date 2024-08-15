from random import choice

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
    print(l)
    mod = {}
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
    currentt = choice(text.split())
    output = ""
    for i in range(0, length):
        newt = getnt(model, currentt)
        output += newt + " "
        currentt = newt
    print(output)




text = '''Once, a girl and a boy walked by a green field. They saw a yellow ball. The girl said, "Let's play!" The boy agreed, so they ran to get the ball.

They kicked it, and it flew over a fence where a dog and a cat were chasing a rabbit. The dog stopped to watch the ball bounce, while the cat jumped onto a rock.

The rabbit then ran away into the bushes.

After playing, they sat down to drink some water. They talked about their favorite colors—the girl liked pink, while the boy liked blue.

As the sun set, they thanked each other for a fun day, and said, "See you again!"

A small fox lived near a deep river. Every day, it would walk to the water to see its reflection. One day, a tall bear came by and asked, “Why do you come here every day?” The fox said, “I like to look at my red fur.” The bear smiled and said, “You are as bright as the sun. You don’t need a reflection to know that.” The fox felt happy and thanked the bear before heading back home.

In a big forest, a rabbit and a deer were good friends. They would run and jump through the trees every morning. One day, they found a round stone that was shiny like gold. They decided to keep it as a treasure. After a long day of playing, they put the stone under a tree and promised to meet there again the next day. The rabbit said, “Let’s thank the forest for giving us this gift!” And they both danced happily under the moonlight.

A dog named Max loved to chase balls. His favorite was a blue one his owner gave him. One sunny day, Max ran outside with the ball in his mouth. He saw a cat sitting by a tree and decided to play. He dropped the ball, and the cat batted it with her paw. They took turns playing until they both got tired and sat in the shade. Max and the cat became best friends that day, and they played together every day from then on.
In a faraway village, a young girl loved to watch the birds fly. Her favorite was a red bird that sang the sweetest songs. Every morning, the bird would sit on her window and sing a melody. One day, the girl asked the bird, “Can you teach me to sing like you?” The bird chirped happily and showed her how to whistle. From that day on, they sang together every morning, bringing joy to everyone who passed by.

There was a small pond where a frog lived. The frog liked to hop on lily pads and catch flies. One day, a duck and a hen visited the pond. The frog asked them, “Would you like to see my special trick?” The duck and hen nodded. The frog then did a big jump and spun in the air before landing on a lily pad. The duck and hen clapped their wings and said, “That was amazing!” They all became friends and played at the pond every afternoon.

'''


gen(text,6,100)
print('next')
gent(text,100)
