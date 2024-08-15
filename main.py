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

text = ''' I found a love, for me
Darling, just dive right in and follow my lead
Well, I found a girl, beautiful and sweet
Oh, I never knew you were the someone waiting for me
'Cause we were just kids when we fell in love
Not knowing what it was
I will not give you up this time
But darling, just kiss me slow
Your heart is all I own
And in your eyes, you're holding mine
Baby, I'm dancing in the dark
With you between my arms
Barefoot on the grass
Listening to our favourite song
When you said you looked a mess
I whispered underneath my breath
But you heard it
Darling, you look perfect tonight
Well, I found a woman, stronger than anyone I know
She shares my dreams, I hope that someday I'll share her home
I found a lover, to carry more than just my secrets
To carry love, to carry children of our own
We are still kids, but we're so in love
Fighting against all odds
I know we'll be alright this time
Darling, just hold my hand
Be my girl, I'll be your man
I see my future in your eyes
Baby, I'm dancing in the dark
With you between my arms
Barefoot on the grass
Listening to our favorite song
When I saw you in that dress, looking so beautiful
I don't deserve this
Darling, you look perfect tonight
Baby, I'm dancing in the dark
With you between my arms
Barefoot on the grass
Listening to our favorite song
I have faith in what I see
Now I know I have met an angel in person
And she looks perfect
I don't deserve this
You look perfect tonight
The club isn't the best place to find a lover
So the bar is where I go
Me and my friends at the table doing shots
Drinking fast and then we talk slow
Come over and start up a conversation with just me
And trust me I'll give it a chance now
Take my hand, stop, put Van the Man on the jukebox
And then we start to dance, and now I'm singing like
Girl, you know I want your love
Your love was handmade for somebody like me
Come on now, follow my lead
I may be crazy, don't mind me
Say, boy, let's not talk too much
Grab on my waist and put that body on me
Come on now, follow my lead
Come, come on now, follow my lead
I'm in love with the shape of you
We push and pull like a magnet do
Although my heart is falling too
I'm in love with your body
And last night you were in my room
And now my bedsheets smell like you
Every day discovering something brand new
I'm in love with your body
(Oh-I-oh-I-oh-I-oh-I)
I'm in love with your body
(Oh-I-oh-I-oh-I-oh-I)
I'm in love with your body
(Oh-I-oh-I-oh-I-oh-I)
I'm in love with your body
Every day discovering something brand new
I'm in love with the shape of you
One week in we let the story begin
We're going out on our first date
You and me are thrifty, so go all you can eat
Fill up your bag and I fill up a plate
We talk for hours and hours about the sweet and the sour
And how your family is doing okay
And leave and get in a taxi, then kiss in the backseat
Tell the driver make the radio play, and I'm singing like
Girl, you know I want your love
Your love was handmade for somebody like me
Come on now, follow my lead
I may be crazy, don't mind me
Say, boy, let's not talk too much
Grab on my waist and put that body on me
Come on now, follow my lead
Come, come on now, follow my lead
I'm in love with the shape of you
We push and pull like a magnet do
Although my heart is falling too
I'm in love with your body
And last night you were in my room
And now my bedsheets smell like you
Every day discovering something brand new
I'm in love with your body
(Oh-I-oh-I-oh-I-oh-I)
I'm in love with your body
(Oh-I-oh-I-oh-I-oh-I)
I'm in love with your body
(Oh-I-oh-I-oh-I-oh-I)
I'm in love with your body
Every day discovering something brand new
I'm in love with the shape of you
Come on, be my baby, come on
Come on, be my baby, come on
Come on, be my baby, come on
Come on, be my baby, come on
Come on, be my baby, come on
Come on, be my baby, come on
Come on, be my baby, come on
Come on, be my baby, come on
I'm in love with the shape of you
We push and pull like a magnet do
Although my heart is falling too
I'm in love with your body
And last night you were in my room
And now my bedsheets smell like you
Every day discovering something brand new
I'm in love with your body
Come on, be my baby, come on
Come on (I'm in love with your body), be my baby, come on
Come on, be my baby, come on
Come on (I'm in love with your body), be my baby, come on
Come on, be my baby, come on
Come on (I'm in love with your body), be my baby, come on
Every day discovering something brand new
I'm in love with the shape of you'''

<<<<<<< Updated upstream
gen(text,6,302)
=======
def gentmod(data):
    l = data.split()
    mod = {}
    for i in range(0,len(l)):
        f = data[i]
        n = data[i+1]
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
    
    currentt = choice(text.split())
    output = ""
    for i in range(0, length):
        newt = getnt(model, currentt)
        output += newt
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


gen(text,6,500)
>>>>>>> Stashed changes
