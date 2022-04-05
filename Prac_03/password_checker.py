MIN_lEN=3
def main():
    passwrd = def_pass(MIN_lEN)
    passwrd_secret(sequence)


def def_pass(min_len):
    passwrd = input("Enter Password:  ".format(min_len))
    while len(passwrd) < min_len:
        print("Password too short, use more then 3 characters")
        passwrd = input("Enter Password: ".format(min_len))
    return passwrd


def passwrd_secret(sequence):
    print('*' * len(sequence))


main()