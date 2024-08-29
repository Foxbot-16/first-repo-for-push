# create the questions
questions = ("How many elements are there in the periodic table?",      # index 0
             "Which animal lay the largest egg?",                       # index 1
             "Which element is the most abboundent in the atmpsphere?", # index 2
             "How many bones are in the human body",                    # index 3
             "Which planet is the hottest in the solar system?")        # index 4

# create the answers
options = (("A. 116", "B. 118", "C. 120", "D. 122"),                    # index 0
           ("A. Whale", "B. Giraffe", "C. Elefant", "D. Ostrich"),      # index 1
           ("A. Nitrogen", "B. CO2", "C. Oxygen", "D. Sulfur"),         # index 2
           ("A. 589", "B. 206", "C. 95", "D. 205"),                     # index 3
           ("A. Mercury", "B. Venus", "C. Mars", "D. Earth"))           # index 4

# create the variables
guesses = []
score = 0
question_num = 0
answers = ("C", "D", "A", "B", "B")

#iterate thoruogh the questions
for question in questions:
    print("-------------------")
    print(f"{question}\n")
    # itreate thorough every option in the question
    for option in options[question_num]:
        print(option)
    # request the guess
    guess = input("Enter your guess: ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        print("CORRECT ✅")
        score += 1
    else:
        print("INCORRECT ❌")
        print(f"{answers[question_num]} is the corrext answer")
    # increment the counter that track the question
    question_num += 1

#calculate the score in %
tot_score = int((score / len(questions)) * 100)

# print the result
print("-------------------")
print("      RESULTS      ")
print("-------------------")
print(f"Total points: {tot_score}%")