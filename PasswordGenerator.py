import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#password = " "

#for chr in range(0,nr_letters):
#    random_chr = random.choice(letters)
#    password += random_chr
#    print(password)
#for chr in range(0,nr_symbols):
#    random_sym =  random.choice(symbols)
#    password += random_sym
#    print(password)
#for chr in range(0,nr_numbers):
#    random_num= random.choice(numbers)
#    password += random_num
#    print(password)

#print(password)

password_l = []
for chr in range(0,nr_letters):
    password_l.append(random.choice(letters))
for chr in range(0,nr_symbols):
    password_l.append(random.choice(symbols))
for chr in range(0,nr_numbers):
    password_l.append(random.choice(numbers))

print(password_l)
random.shuffle(password_l)
print(password_l)

password = " "
for chr in password_l:
    password += chr

print(f"Your Password is : {password}")
