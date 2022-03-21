from sentences import get_determiner, get_noun, get_prepositional_phrase, get_verb, get_preposition, get_adverb
import random
import pytest

def test_get_determiner():
    single_determiners = ["a","one","the"]

    for _ in range(4):
        word = get_determiner(1)
        assert word in single_determiners
    
    plural_determiners = ["two","some","many","the"]
    for _ in range(4):
        quantity = random.randint(2, 11)
        word = get_determiner(quantity)
        assert word in plural_determiners

def test_get_noun():
    single_determiners = ["bird","boy","car","cat","child",
        "dog", "girl", "man", "rabbit", "woman"]
    
    for _ in range (9):
        word = get_noun(1)
        assert word in single_determiners
    

    plural_determiners = ["birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]

    for _ in range(10):
        quantity = random.randint(2, 11)
        word = get_noun(quantity)
        assert word in plural_determiners


def test_get_verb():
    past = ["drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]
    
    for _ in range(10):
        word = get_verb(1, "past")
        assert word in past


    present  = [ "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"]
    
    for _ in range(10):
        word = get_verb(1, "present")
        assert word in present
    
    plural = [ "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"]
    
    for _ in range(10):
        number = random.randint(2,11)
        word  = get_verb(number, "present")
        assert word in plural

    future = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]
    
    for _ in range(10):
        word = get_verb(1, "future")
        assert word in future

def test_get_preposition():
    propositional = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]

    for _ in range(10):
        number = random.randint(1,10)
        word = get_preposition(number)
        assert word in propositional

def test_get_prepositional_phrase():
    for _ in range(10):
        number = 1
        word = get_prepositional_phrase(number)
        assert word 

    for _ in range(10):
        number = random.randint(2,10)
        word = get_prepositional_phrase(number)
        assert word

def test_get_adverb():
    for _ in range (10):
        number = random.randint(2,10)
        word = get_adverb(number)
        assert word


      


pytest.main(["-v", "--tb=line", "-rN", __file__])

