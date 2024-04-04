
valid_coin = {5, 10, 25}
def main():
    inserted_amount = 0
    amount_due = 50
    while inserted_amount < 50:
        print(f"Amount Due: {amount_due}")
        coin = int(input("Insert coin: "))
        if coin in valid_coin:
            inserted_amount += coin
            amount_due -= coin

    change = inserted_amount - 50
    print("Change Owed:", change)

if __name__ == "__main__":
    main()