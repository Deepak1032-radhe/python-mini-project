print("=====QUIZ GAME=====")
score = 0
print("\n1. python kisne banai thi?")
print("a) Guido van Rossum")
print("b) James Gosling")   
print("c) Bjarne Stroustrup")
answer1 = input("Enter your answer (a, b, c): ")
if answer1.lower() == "a":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is a) Guido van Rossum.")  
print("\n2. python ka logo kis cheez ka hai?")
print("a) Snake")   
print("b) Coffee cup")
print("c) Two snakes intertwined")
answer2 = input("Enter your answer (a, b, c): ")
if answer2.lower() == "c":
    print("Correct!")
    score += 1  
else:
    print("Wrong! The correct answer is c) Two snakes intertwined.")
    print("your final score is:", score, "/ 2")