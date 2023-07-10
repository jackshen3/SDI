print("Welcome to the Letter Counter App")

name = input("What is your name? ")
print("Hello", name + "!")
print("I will count the number of times that a specific letter occurs in a message.")
letter_count = input("Please enter a message: ")
occurences = input("Which letter would you like to count the occurences of? ")

count = 0
for x in letter_count:
    if x == occurences:
        count = count + 1

print(name, "your message has", str(count), str(occurences) + "'s")