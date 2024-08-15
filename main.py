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
    mod[(None,l[0])][l[1]] = 1
    for i in range(1,len(l)-1):
        f = (l[i-1],l[i])
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
    currentt = (None,'The')
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
A red fox lived near a river where it loved to watch the fish swim. One day, it saw a blue bird perched on a branch above the water. The fox asked, "Why do you sit there every day?" The bird replied, "I like to watch the sunset reflected on the water." The fox and the bird became friends and watched the sunsets together every evening.
A rabbit and a squirrel lived in a forest. They loved collecting nuts and berries. One morning, they found a shiny gold acorn. They were so excited that they decided to plant it to see if it would grow into a golden tree. They visited the spot every day to check on their special acorn.
In a faraway desert, a camel and a snake were unlikely friends. The camel loved to walk across the sand, while the snake preferred to hide under rocks. One day, they decided to have a race to see who could cross the desert faster. The camel was fast on the long stretches, but the snake was quick when weaving through the dunes. In the end, they both agreed that they each had their own special talents.
A dog and a cat lived in a cozy house with their owner. Every afternoon, the dog would chase its tail while the cat napped in a sunny spot. One day, they decided to switch roles. The dog tried to nap, but couldn’t sit still. The cat tried chasing its tail, but got dizzy. They both realized they liked their own way of having fun and went back to their usual activities.

A tiger and a bear lived deep in the jungle. The tiger loved to run, and the bear loved to climb trees. One day, they decided to trade skills. The bear tried running but got tired quickly, while the tiger tried climbing but couldn’t reach high branches. They laughed and decided it was best to stick to what they were good at.


A frog and a duck lived by a pond. They were best friends and loved to splash in the water. One day, they decided to have a contest to see who could make the biggest splash. The frog jumped high and landed with a splash, but the duck flapped its wings and made an even bigger one. They both laughed and agreed that splashing together was the most fun of all.
A horse and a goat lived on a farm. The horse loved to gallop through the fields, while the goat preferred to munch on grass. One day, they decided to have a race. The horse ran fast, but the goat found shortcuts through the bushes. They finished the race together and celebrated by sharing some fresh hay.
A koala lived in a tall eucalyptus tree in Australia. It loved to eat leaves and take naps. One day, a kangaroo hopped by and invited the koala to explore the nearby fields. The koala was hesitant but agreed. They had a great adventure, and when they returned, the koala realized that sometimes stepping out of its comfort zone led to fun new experiences.

A boy had a collection of toy animals. He had a bear, a tiger, a snake, and a frog. Every night, he would line them up and tell them a bedtime story. One night, he imagined they all came to life and went on an adventure in the jungle. They faced many challenges, but in the end, they worked together and found a hidden treasure.
A girl loved to draw pictures of rainbows. She would use every color—red, blue, yellow, green, and purple. One day, she decided to add some animals to her rainbow. She drew a cat, a dog, and a bird flying across the sky. Her artwork became so colorful and full of life that everyone in her family admired it.

A lion and a fox were having a conversation in the jungle. The lion was proud of its strength, while the fox was proud of its cleverness. They decided to have a contest to see who could catch a deer first. The lion chased with all its might, but the fox used a trick to outsmart the deer. In the end, they realized both strength and cleverness had their own value.
In a small pond, a frog and a fish were best friends. The frog loved to jump on lily pads, while the fish enjoyed swimming underwater. One day, the frog decided to try diving, and the fish decided to jump. They both tried and realized they were happiest doing what they naturally loved.
A mouse and a rabbit lived near a garden. They loved to nibble on carrots and lettuce. One day, they found a big, shiny red apple in the garden. It was too big for them to carry, so they decided to share it right there. They had a wonderful feast and promised to share all their discoveries from then on.
A cow and a sheep lived in a meadow. The cow loved to graze on the tall grass, while the sheep loved to roll around in the soft flowers. One day, they saw a rainbow in the sky. They followed it and found a field even more beautiful than their own. They decided to visit this special place whenever they wanted to relax and enjoy the view.
A cat and a parrot lived in a big house. The cat loved to sleep, and the parrot loved to sing. One day, the cat tried to mimic the parrot’s song, but it only made funny meowing sounds. The parrot tried to curl up like the cat but couldn’t stop talking. They both laughed and decided they were perfect just the way they were.
A bat and a rat lived in a dark cave. The bat could fly through the night, while the rat scurried along the ground. One night, they decided to explore the cave together. The bat showed the rat secret tunnels high up, and the rat showed the bat hidden passages down below. They both realized that together, they could see the whole cave in ways they never could alone.

A donkey and a turkey lived on a farm. The donkey loved to carry heavy loads, while the turkey loved to strut around the yard. One day, the turkey challenged the donkey to a dance-off. The donkey tried to dance but ended up wobbling clumsily. They both laughed and agreed that each was best at what they naturally did.
A dog and a horse lived in the same barn. The dog loved to chase its tail, while the horse loved to gallop through the fields. One day, they decided to race. The dog ran in circles while the horse raced straight ahead. When they both got tired, they rested together in the shade and realized that having fun was what mattered most.
A snake and a turtle were neighbors in a forest. The snake loved to slither quickly, while the turtle enjoyed taking its time. One day, they decided to travel to the river together. The snake reached the river quickly but had to wait for the turtle to catch up. When the turtle arrived, they both enjoyed the cool water and agreed that sometimes, taking it slow is just as enjoyable.
A cat and a mouse lived in the same house. The cat was supposed to chase the mouse, but they became friends instead. They spent their days playing hide and seek. The mouse would hide in a small hole, and the cat would pretend to look for it. In the evenings, they would sit by the window and watch the sunset together, content in their unlikely friendship.



'''


gen(text,6,100)
print('next')
gent(text,200)
