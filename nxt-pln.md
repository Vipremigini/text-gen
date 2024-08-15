## current state
I have currently made a text generator using markov chains. This generated text is then fed into a text gpt (like chatGPT) to generate legible and coherent text.
As i have observed this workflow generates a new response every time. GPT models usually generate same/similar responses when prompted with same/similar prompts. 
However this code that i wrote, seems to generate something new every time.

## how it works
the code is trained on sample text that resemble or contain some amount of target output. The code generates a markov transition matrix for the text. 
(The current model considers 2 tokens/words at a time and generates frequency/probablilty for the next word)
Based on the markov matrix generated, text output is generated based on a random starting seed phrase.
The text output thus created is mangled and often meaningless for humans to read.
Although based on randomness and probablity, the model generates text that is based on the training text, and often contains some jumbled sentences that might have some unclear meanings
Because the generated text is trained on the training text, the generated text will resemble the original text.
This new text is fed into an GPT, and given some instructions on how to interpret the generated text and how to generate desired output.
Due to randomness of the markov model, each time the gpt has new data to work upon.

## future plans
1) i'm planning to work upon this and write a research paper upon this concept
2) I have to test this on multiple training data and outputs
3) figure out new ways in which i can use this concept to help people.
