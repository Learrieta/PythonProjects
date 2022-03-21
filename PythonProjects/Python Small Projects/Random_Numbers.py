import random

def main():
    numbers = [16.2, 75.1, 52.3]
    print(numbers)

    append_random(numbers)
    print(numbers)

    append_random(numbers, 3)
    print(numbers)

    words = []

    append_random_words(words)
    print(words)

    append_random_words(words, 4)
    print(words)


def append_random(numbers_list, quantity=1):
    for _ in range (quantity):
        random_number = random.uniform(0, 100)
        rounds = round(random_number, 1)
        numbers_list.append(rounds)

def append_random_words(words_list, quantity=1):
    words = ["car", "friend", "airplane","game", "date"]
    for _ in range(quantity):
        random_words = random.choice(words)
        words_list.append(random_words)

main()