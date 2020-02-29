"""Typecasting and input from console"""

def oddeven(num):
    if num%2==0:
        print("Even")
    else:
        print("Odd")
    return

def main():
    print("running")
    n = int(input("Enter a number to check even or odd : "))
    print("THIS IS MAIN FUCNTION")
    oddeven(num)

if __name__ == ' __main__':
    main()
