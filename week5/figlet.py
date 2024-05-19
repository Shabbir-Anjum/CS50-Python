import sys
import random
import pyfiglet

def print_usage_error():
    print("Invalid usage")
    sys.exit(1)

def get_random_font():
    return random.choice(pyfiglet.FigletFont.getFonts())

def main():
    if len(sys.argv) == 1:
        font_name = get_random_font()
    elif len(sys.argv) == 3 and (sys.argv[1] == '-f' or sys.argv[1] == '--font'):
        font_name = sys.argv[2]
    else:
        print_usage_error()

    if font_name not in pyfiglet.FigletFont.getFonts():
        print_usage_error()

    user_input = input("Enter text: ")
    figlet = pyfiglet.Figlet(font=font_name)
    print(figlet.renderText(user_input))

if __name__ == "__main__":
    main()
