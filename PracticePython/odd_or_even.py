""" takes a num as input and prints if its odd or even"""

def main():
    """ main """
    while True:
        try:
            number = int(input("Please enter the number: "))
            break
        except ValueError:
            print("Please enter a valid number")

    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")

    main()

main()
