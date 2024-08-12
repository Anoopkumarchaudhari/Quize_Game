print()
print('**  Quize Game  **')
print()
name = input('Enter your name: ').upper()
print('Hii! WELCOME {}'.format(name))
print()
print('---All the best for quize---')

questions = ("1. What is the value of  2*4+5.",
             "2. How many state in India.",
             "3. How many district in Bihar.",
             "4. what is the value of (8/2 * 3 +1)",
             "5. What is the capital of India.")
options=(("A. 12","B. 13","C. 18","D. 24"),
         ("A. 38","B. 24 ","C. 28","D. 29"),
         ("A. 24","B. 38","C. 39","D. 40"),
         ("A. 3","B. 4","C. 13","D. 1"),
         ("A. Bihar","B. New Delhi","C. Patna","D. Bettah"))

answers = ("B","C","B","C","B")

guesses = []
score=0
question_num=0

for question in questions:
    print(question)
    for option in options[question_num]:
        print(" " ,option)

    guess = input("  Enter your Ans : ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("  CURRECT")
    else:
        print("  INCURRECT")   
        print(f"  {answers[question_num]} is the currect answer.")
    question_num += 1
    print("-----------------------------------------------------")

print("**************")
print("   RESULTS")
print("**************")    

print("answers:",end=" ")
for answer in answers:
    print(answer,end=" ")
print()

print("guess : ",end=" ")
for guess in guesses:
    print(guess,end=" ")
print()    

score = int(score / len(questions)*100)
print(f"Your Score is : {score}%")