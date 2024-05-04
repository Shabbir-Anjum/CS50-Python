def main():
    text = input('Input: ')
    output = ''
    for char in text:
        if char.lower() not in 'aeiou':
            output += char
    print(output)

if __name__ == "__main__":
    main()
