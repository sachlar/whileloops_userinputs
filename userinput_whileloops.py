# user input and while loops

name = "Tell me your name: "
name += "\nWhat is your first name? "
prompt = input(name)
print(f"\nHello {prompt}!")

age = input("How old are you? : ")
print(age)

age = int(age)
print(type(age))

# odd or even

number  = int(input("enter a number and i will tell you if its odd or even: "))
if number % 2 == 0:
    print(f"you entered {number}, this number is even")
else:
    print(f"you entered {number}, this number is odd")

# while loops

current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

# while loop to run a thing until the user tells us to quit

prompt = "\nTell me something, I will repeat it back to you: "
prompt += "\nEnter 'quit' to exit the program. "

message = ""
while message != "quit":
    message = input(prompt)
    if message != "quit":
        print(message)

# add a flag to a while loop 
active = True
while active:
    message = input(prompt)
    if message == "quit":
        active = False
    else:
        print(message)

# using break in a while loop
prompt = "\nTell me the name of a city you have visited: "
prompt += "\nEnter 'quit' to exit the program. "
while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")

# using continue in a while loop
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0: # if its even continue through the loop don't print  
        continue
    print(current_number)