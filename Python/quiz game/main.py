#python quiz game


questions = ("What is the capital city of France?",
             "Which planet is known as the 'Red Planet'?",
             "Who painted the Mona Lisa?",
             "What is the chemical symbol for gold?",
             "What is the largest ocean on Earth?")

options = (("A. London"             , "B. Paris"        , "C. Rome"                 , "D. Berlin"),
           ("A. Mars"               , "B. Venus"        , "C. Jupiter"              , "D. Saturn"),
           ("A. Vincent van Gogh"   , "B. Pablo Picasso", "C. Leonardo da Vinci"    , "D. Michelangelo"),
           ("A. Au"                 , "B. Ag"           , "C. Fe"                   , "D. Pb"),
           ("A. Atlantic Ocean"     , "B. Indian Ocean" , "C. Arctic Ocean"         , "D. Pacific Ocean"))

answers = ("B", "A", "C", "A", "D")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("--------------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter your answer: ").upper()
    guesses.append(guess)

    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer!")
    question_num += 1

print("--------------------------------------")
print("----------------RESULT----------------")
print("--------------------------------------")

print(f"ANSWER: {answers}")
print(f"GUESS: {guesses}")