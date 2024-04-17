#def hello(name, last='anjum'):
    #print('hello', name, last)
#hello('good')
#name=input('Your Name: ')
#last=input('Your name last: ')
#print(name)
#hello(name,last)
def main():
    x=int(input('value: '))
    print ('value is : ', square(x))
def square(x):
    #return x*x
    #return x**2
    return pow(x,2)
main()