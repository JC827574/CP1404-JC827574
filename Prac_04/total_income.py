"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""
incomes = []
month_cycle = int(input("How many months? "))


def main(month_cycle, income):
    """Display income report for incomes over a given number of months."""

    for month_cycle in range(1, month_cycle + 1):
        income = float(input("Enter income for month " + str(month_cycle) + ": "))
        incomes.append(income)


def results(month_cycle, income):
    print("\nIncome Report\n-------------")
    total = 0
    for month_cycle in range(1, month_cycle + 1):
        income = incomes[month_cycle - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month_cycle, income, total))


main(month_cycle, incomes)
results(month_cycle, incomes)
