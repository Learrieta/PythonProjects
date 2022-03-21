NEGATIVE = -1
POSITIVE = 1

def main():
    a = """This program is an implementation of the Rosenberg
Self-Esteem Scale. This program will show you ten
statements that you could possibly apply to yourself.
Please rate how much you agree with each of the
statements by responding with one of these four letters:

D means you strongly disagree with the statement.
d means you disagree with the statement.
a means you agree with the statement.
A means you strongly agree with the statement."""
    
    print(a)

    score = 0
    score += ask_question(
        "1. I feel that I am a person of worth,"
        " at least on an equal plane with others.", POSITIVE)
    score += ask_question(
        "2. I feel that I have a number of good qualities.", POSITIVE)
    score += ask_question(
        "3. All in all, I am inclined to feel that I am a failure.",
        NEGATIVE)
    score += ask_question(
        "4. I am able to do things as well as most other people.",
        POSITIVE)
    score += ask_question(
        "5. I feel I do not have much to be proud of.", NEGATIVE)
    score += ask_question(
        "6. I take a positive attitude toward myself.", POSITIVE)
    score += ask_question(
        "7. On the whole, I am satisfied with myself.", POSITIVE)
    score += ask_question(
        "8. I wish I could have more respect for myself.", NEGATIVE)
    score += ask_question(
        "9. I certainly feel useless at times.", NEGATIVE)
    score += ask_question(
        "10. At times I think I am no good at all.", NEGATIVE)

    print()
    print(f"Your score is {score}.")
    print("A score below 15 may indicate problematic low self-esteem.")


def ask_question(statement, por_or_neg):
    print(statement)
    answer = input("Enter D, d, a, or A: ")
    score = 0
    if answer == "D":
        score = 0
    elif answer == "d":
        score = 1
    elif answer == "a":
        score = 2
    elif answer == "A":
        score = 3

    if por_or_neg == NEGATIVE:
        score = 3 - score
    
    return score
    

        



main()
    
