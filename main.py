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
    currentt = "The"
    output = "The "
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

A cat and a dog were best friends. One day, they found a red ball and decided to play together. The cat would chase the ball, and the dog would catch it. They had so much fun that they didn’t even notice the sun setting. They promised to play again the next day

A rabbit loved to hop around the garden. One day, it found a shiny silver coin buried in the dirt. The rabbit showed it to a mouse, and they both decided to hide it under a big rock. They would check on their treasure every week.


A yellow butterfly flew over a field of flowers. It met a green frog sitting on a leaf. The frog asked, “Can you teach me to fly?” The butterfly laughed and said, “You’re meant to hop, not fly!” They both agreed that hopping was just as fun as flying.

A boy and a girl loved to draw with colored chalk. One day, they drew a big purple sun with a smiling face on the sidewalk. Everyone who walked by stopped to admire their work. The kids were so proud of their drawing that they decided to do more art every weekend.
A small bird was learning to fly. It was scared at first, but its mother encouraged it. “Just try,” she said. After a few attempts, the bird soared into the sky and felt so happy. The mother was proud and cheered as her little one flew higher and higher.
In a quiet village, a black cat liked to sit on a fence and watch the moon rise every night. It felt peaceful under the soft glow of the moonlight. One night, the cat saw a shooting star and made a wish to have more nights just like this one.


A horse and a donkey lived on a farm. The horse loved to run, and the donkey loved to relax. One day, the horse asked the donkey to race. They ran across the field, but the donkey stopped halfway and decided to take a nap instead. The horse laughed and joined the donkey under a shady tree.
A sheep and a cow were grazing in a green meadow. The cow noticed a butterfly and decided to follow it. The sheep joined in, and they both wandered through the field, enjoying the fresh air and sunshine. They spent the whole afternoon chasing butterflies and enjoying nature.
A pig and a goat were best friends. They loved to play in the mud. One day, they had a contest to see who could get the muddiest. The pig rolled and splashed, while the goat stomped around. In the end, they both looked like walking piles of mud and couldn’t stop laughing.
A duck and a hen lived near a pond. They loved to chat and share stories. One day, they decided to have a tea party by the water. They invited the frog and the turtle. They all sat together, sipping tea and telling funny stories until the sun went down.

A tiger lived in the jungle. It was known as the fastest animal in the forest. One day, it challenged a fox to a race. The fox knew it couldn’t win, but it accepted anyway. As they raced, the fox took a shortcut and surprised the tiger by finishing first! The tiger laughed and said, “You’re clever, little fox!”
A koala and a deer lived in a forest. They were curious about what lay beyond the trees. One day, they decided to explore. They walked for hours and found a beautiful clearing with colorful flowers and a sparkling stream. They loved it so much that they visited the spot every weekend.

A bear and a wolf were good friends. They liked to tell stories by the fire at night. One evening, the bear told a story about a hidden treasure deep in the forest. The next day, they set out to find it. They searched and searched, and in the end, they found a big, shiny gold coin buried under a tree. They decided to keep it as a memory of their adventure.
A frog and a crab met by a pond. The crab was sad because it couldn’t jump like the frog. The frog said, “But you can walk sideways! That’s cool!” The crab smiled and showed the frog how it could scuttle across the rocks. They spent the rest of the day playing and showing off their unique skills.

A lion was the king of the jungle. Every morning, it would roar loudly to greet the day. One day, a camel visited the jungle. The lion asked, “Why don’t you roar?” The camel replied, “I like to stay quiet and enjoy the peace.” The lion understood and decided to have a quiet morning with the camel, just enjoying the beauty of the jungle.
A girl loved to read books about space. Her favorite was about the stars and the planets. One night, she looked through her telescope and saw a bright star twinkling. She imagined it was sending her a message, saying, “Keep dreaming!” From that night on, she promised herself to always reach for the stars.

A boy had a toy car that he loved very much. He would race it around his room, imagining it was the fastest car in the world. One day, he decided to build a little ramp to see how far it could jump. When he launched the car, it flew through the air and landed perfectly. The boy cheered and decided to build even bigger ramps.

A girl had a doll with curly hair. She would style it in different ways every day. One day, she decided to throw a fashion show for her doll. She invited her friends and showed off all the outfits she had created. Everyone clapped and said her doll was the most stylish in town.

A boy and a girl went to the park with their favorite toys. The boy brought a kite, and the girl brought a ball. They played for hours, taking turns flying the kite and kicking the ball. As the sun set, they agreed that this was the best day ever and couldn’t wait to come back.
A snake lived near a tree. It liked to slither through the grass and watch the animals pass by. One day, it met a bird that was building a nest. The snake asked, “Why do you work so hard?” The bird said, “I’m making a home for my family.” The snake thought about it and realized that having a safe place to live was the most important thing of all.


'''


gen(text,6,100)
print('next')
gent(text,200)
