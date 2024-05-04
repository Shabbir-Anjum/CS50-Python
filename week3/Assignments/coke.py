def main():
    coke_price = 50
    amount_due = coke_price
    while amount_due > 0:
        print("Amount Due:", amount_due)
        coin = int(input("Insert Coin: "))
        if coin == 25 or coin == 10 or coin == 5:
            amount_due -= coin
    change_owed = abs(amount_due)
    print("Change Owed:", change_owed)
if __name__ == "__main__":
    main()
