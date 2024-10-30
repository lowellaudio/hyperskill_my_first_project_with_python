# Write your code here
def earned_amount():
    bubblegum = 202
    toffee = 118
    ice_cream = 2250
    milk_chocolate = 1680
    doughnut = 1075
    pancake = 80

    print(
        f"""
Earned amount:
Bubblegum: ${bubblegum}
Toffee: ${toffee}
Ice cream: ${ice_cream}
Milk chocolate: ${milk_chocolate}
Doughnut: ${doughnut}
Pancake: ${pancake}
Income: ${float(bubblegum + toffee + ice_cream + milk_chocolate + doughnut + pancake)}

"""
    )
    income = float(bubblegum + toffee + ice_cream + milk_chocolate + doughnut + pancake)
    return income

def expenses_count():
    print("Staff expenses:")
    staff_expenses = int(input())
    print("Other expenses:")
    other_expenses = int(input())
    net_income = (
            earned_amount()
            - staff_expenses
            - other_expenses
    )
    print(f"Net income: ${net_income}")


earned_amount()
expenses_count()
