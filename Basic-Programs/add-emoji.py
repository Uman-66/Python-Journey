print("Welcome to the emoji adder")
entry = input("Write a sentence full of emojis 😂,🧚,🧌,😊")

emojis = ["😂","🧚","🧌","😊"]

for emoji in emojis:
    numbers = entry.count(emoji)
    print(f"{emoji} is {numbers} times in the sentence.")