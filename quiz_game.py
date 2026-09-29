print("======QUIZ GAME======")
print("Answer the following 5 questions!")
Questions = ["What is the currency of India called?",
            "What is 90*24?",
            "State true or false, 'Python is an object oriented language.'",
            "How many days are there in a week?",
            "Which planet is called 'The Red Planet?'"]
print (Questions)
Answers = ["rupee",
          "2160",
          "true",
          "7 days",
          "Mars"]
score = 0
for i in range (len(Questions)):
    print(Questions[i])
    user_answer = input("Your answer: ")
    
    if user_answer == Answers[i]:
        print("Correct!")
        score = score + 1
    else:
       print("Wrong!")
print("Your final score is:", score)