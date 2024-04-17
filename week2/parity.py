def main():
    x= int(input('enter: '))
    if x%2==0:
        print('even')
    else:
        print("Odd")
    def even(n):
        return True if n%2==0 else False
    n=int(input('Enter value of n: '))
    value=even(n)
    print(value)
main()