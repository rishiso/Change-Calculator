money = {"$100 Bill": 10000, "$50 Bill": 5000, "$20 Bill": 2000, "$10 Bill": 1000, "$5 Bill": 500, "$1 Bill": 100, "Quarter": 25, "Dime": 10, "Nickel": 5, "Penny": 1}

def calc_change(cost, money_given):
    if cost > money_given:
        print("Not enough money")
    elif cost == money_given:
        print("No change")
    else:
        change = (money_given - cost) * 100
        print(change / 100)
        for i, v in money.items():
            num = int(change / v)
            if num > 0:
                change -= num * v
                print(f"{str(num)}: {i}")
    print("")

calc_change(76.42, 100)
calc_change(24.35, 50)
calc_change(10, 10)
calc_change(10.63, 10)