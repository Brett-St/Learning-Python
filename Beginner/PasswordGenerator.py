import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

p_letters = ""
p_symbols = ""
p_numbers = ""
password = ""

for _ in range(nr_letters):
    chosen = random.choice(letters)
    password += chosen
    p_letters += chosen

for _ in range(nr_symbols):
    chosen = random.choice(symbols)
    password += chosen
    p_symbols += chosen

for _ in range(nr_numbers):
    chosen = random.choice(numbers)
    password += chosen
    p_numbers += chosen


scrambled_list = list(password)
random.shuffle(scrambled_list)
scrambled_password = "".join(scrambled_list)

print("Letters only:", p_letters)
print("Symbols only:", p_symbols)
print("Numbers only:", p_numbers)
print("Combined (before scrambling):", p_letters + p_symbols + p_numbers)
print("Scrambled password:", scrambled_password)
