#functions

socks = 0
total = 0.00
PRICE = 9.75

def addsocks():
    global socks
    quantity = int(input("\nEnter the amount of socks you'd like to add: "))
    print("\n")
    if quantity < 0:
        print("Invalid input\n")
    else:
        socks += quantity
        
def vieworder():
    global socks
    global total
    ship = 0
    if socks >= 5:
            ship = 1.5
    else: 
        ship = 2.25
    total = round((socks * PRICE),2) + ship
    print("\nSocks:", socks, "\nTotal:", total)

def removesocks():
    global socks
    removed = int(input("Enter quantity to remove: "))
    socks -= removed
    vieworder()

def checkout():
    vieworder()
    print('Thank you for your order!')

print("The Sock Shop\n")
while True:
    choice = input("1. Add Socks to Order\n2. Remove Socks from Order\n3. View Current Order\n4. Checkout\n\nPlease enter your choice: ")
    if choice == "1":
       addsocks()
    elif choice == "2":
       removesocks()
    elif choice == "3":
       vieworder()
    elif choice == "4":
        break
    else:
        print("\nInvalid data entered. Please select a number 1-4.\n")
checkout()
