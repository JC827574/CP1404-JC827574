out_file = open("namman.txt", "w")
name = input("What is your name? ")
print(name, file=out_file)  # or out_file.write(name)
out_file.close()

in_file = open("namman.txt", "r")
name = in_file.read().strip()
in_file.close()
print("Your name is", name)


with open("namman.txt", "r") as in_file:
    name = in_file.read().strip()
print("Your name is", name)


in_file = open("imreading.txt", "r")
number1 = int(in_file.readline())
number2 = int(in_file.readline())
in_file.close()
print(number1 + number2)


in_file = open("imreading.txt", "r")
total = 0
for line in in_file:
    number = int(line)
    total += number
in_file.close()
print(total)