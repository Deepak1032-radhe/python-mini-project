import time
sentence = "The python is very easy."
print("Welcome to the Typing Game!")    
print(f"Type the following sentence as quickly as you can:\n{sentence}")
start_time = time.time()
user_input = input("Your typing: ")
end_time = time.time()
typing_time = end_time - start_time
if user_input == sentence:
    print(f"Congratulations! You typed the sentence correctly in {typing_time:.2f} seconds.")
else:
    print("Sorry, your typing was incorrect.")