import sys
from random import choice


def make_chains(corpus):
    """Takes input text as string; returns dictionary of markov chains."""

    chains = {}

    words = corpus.split()
    # print(words)

    for i in range(len(words) - 2):
        key = (words[i], words[i + 1])
        # print(key)
        value = words[i + 2]
        # print(value)

        if key not in chains:
            chains[key] = []

        chains[key].append(value)
        # print(chains[key])

    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""
    chain_keys = list(chains.keys()) 
    # print(chain_keys)
    key = chain_keys[0]
    # print(key)
    words = [key[0], key[1]]
    # print(type(words))
    count = 0
    
    count = len(key[0])  +1 + len(key[1])
    # print(words)
    # print(count)

    # Keep doing this until we reach the end or until we go too
    # long for a Twitter message
    while key in chains and count < 140:

        word = choice(chains[key])
        count += len(word) +1 
        if count >= 140: 
            break
        # print(word, len(word))
        words.append(word)
        # print(words, count) 
        key = (key[1], word)

    # print(len(" ".join(words)))
    return " ".join(words)


input_path = sys.argv[1]
input_text = open(input_path).read()
# print(input_text)

chains = make_chains(input_text)

random_text = make_text(chains)

i = 1
while i in range(1,1000): 
    if len(random_text) > 140: 
        print(len(random_text))
        print(random_text) 
    i+= 1

