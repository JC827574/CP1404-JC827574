"""
CP1404/CP5632 - Practical
Broken program to determine score status

known information: The intention is that the score must be between 0 and 100 inclusive; 90 or more is excellent;
50 or more is a pass; below 50 is bad.
"""

# TODO: Fix this!
#new code-
score = float(input("Enter score: "))
if score > 100 or score < 0:
    print("The score you entered is invalid")
elif score >= 90:
    print("Excellent!")
elif score >= 50:
    print("Passable.")
elif score < 50:
    print("BAD..")

# the old code-
#if score >= 50:
    #print("Passable")

#if score >= 90:
    #print("Excellent")

#if score < 50:
    #print("Bad")

#else:
    #if score < 0:
        #print("Invalid score")
    #if score > 100:
        #print("Invalid score")
