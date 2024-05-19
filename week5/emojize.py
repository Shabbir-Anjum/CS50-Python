import emoji

def emojize_input(input_str):
    return emoji.emojize(input_str, language='alias')

def main():
    user_input = input("Input: ")
    emojized_output = emojize_input(user_input)
    print("Output:", emojized_output)

if __name__ == "__main__":
    main()
