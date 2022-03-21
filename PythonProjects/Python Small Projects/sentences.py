import random

def main():

    print(f'{get_determiner(1)} {get_noun(1)} {get_adverb(1)} {get_verb(1, "past")} {get_preposition(1)} {get_prepositional_phrase(1)}')
    print(f'{get_determiner(1)} {get_noun(1)} {get_adverb(1)} {get_verb(1, "present")} {get_preposition(1)} {get_prepositional_phrase(1)}')
    print(f'{get_determiner(1)} {get_noun(1)} {get_adverb(1)} {get_verb(1, "future")} {get_preposition(1)} {get_prepositional_phrase(1)} ')
    print(f'{get_determiner(2)} {get_noun(2)} {get_adverb(1)} {get_verb(1, "past")} {get_preposition(1)} {get_prepositional_phrase(1)} ')
    print(f'{get_determiner(2)} {get_noun(2)} {get_adverb(1)} {get_verb(2, "present")} {get_preposition(1)} {get_prepositional_phrase(1)}')
    print(f'{get_determiner(2)} {get_noun(2)} {get_adverb(1)} {get_verb(1, "future")} {get_preposition(1)}  {get_prepositional_phrase(1)}')


def get_determiner(quantity):
    if quantity == 1:
        words = ["a","one","the"]
    else:
        words = ["two","some","many","the"]
    word = random.choice(words)
    return word

def get_noun(quantity):
    if quantity == 1:
        words = ["bird","boy","car","cat","child",
        "dog", "girl", "man", "rabbit", "woman"]
    else:
        words = ["birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]
    
    word = random.choice(words)
    return word

def get_verb(quantity, tense):
    if tense == "past":
        verbs = ["drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]
    elif tense == "present" and quantity == 1:
        verbs = [ "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"]
    elif tense == "present" and quantity != 1:
        verbs = [ "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"]
    elif tense == "future":
        verbs = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]
    
    word = random.choice(verbs)
    return word

def get_preposition(phrase):
    if phrase  >= 1:
        words = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    word = random.choice(words)
    return word
    

def get_prepositional_phrase(quantity):
    if quantity  == 1:
        sentence = (f'{get_preposition(1)} {get_determiner(1)} {get_noun(1)} ')
    else :
        sentence = (f'{get_preposition(2)} {get_determiner(2)} {get_noun(2)}')
    
    return sentence
   
def get_adverb(phrase):
    if phrase >= 1:
        words = ["boldly","bravely", "brightly", "cheerfully", "deftly", "devotedly", "eagerly", "elegantly", "faithfully", "fortunately", "gleefully", "happily"]
    word = random.choice(words)
     
    return word


    
        

main()
