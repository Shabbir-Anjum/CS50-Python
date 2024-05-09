menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
def main():
    order_total = 0.0
    try:
        while True:
            item = input('Item: ').title()
            if item in menu:
                order_total += menu[item]
                print(f"Total: ${order_total:.2f}")
            else:
                EOFError
    except EOFError:
        pass

if __name__ == "__main__":
    main()
