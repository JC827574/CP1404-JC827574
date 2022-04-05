def main():
    score = float(input("Enter score: "))
    grades(score)


def grades(score):
    if score > 100 or score < 0:
        print("The score you entered is invalid")
    elif score >= 90:
        print("Excellent!")
    elif score >= 50:
        print("Passable.")
    elif score < 50:
        print("BAD..")


main()
