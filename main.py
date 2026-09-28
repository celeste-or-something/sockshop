#functions

socks = 0

def addsocks():
    global socks
    amount = int(input("\nEnter the amount of socks you'd like to add: "))
    if amount < 0:
        print("Invalid input")
        return 0
    else:
        return amount

print("The Sock Shop\n")
while True:
    choice = input("1. Add Socks to Order\n2. Remove Socks from Order\n3. View Current Order\n4. Checkout\n\nPlease enter your choice: ")
    if choice == "1":
       addsocks()
    elif choice == "2":
        pass
       # removesocks()
    elif choice == "3":
        pass
       # vieworder()
    elif choice == "4":
        break
    else:
        print("\nInvalid data entered. Please select a number 1-4.\n")

    
