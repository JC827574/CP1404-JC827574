"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
state = input(str("enter the name of the state")).upper()
if state in CODE_TO_NAME:
    print(state, "is", CODE_TO_NAME[state])
else:
    print("invalid input try again!")



