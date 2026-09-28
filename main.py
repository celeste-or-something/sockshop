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
        
def vieworder():
    global socks
    print("Socks:", socks)

print("The Sock Shop\n")
while True:
    choice = input("1. Add Socks to Order\n2. Remove Socks from Order\n3. View Current Order\n4. Checkout\n\nPlease enter your choice: ")
    if choice == "1":
       addsocks()
    elif choice == "2":
        pass
       # removesocks()
    elif choice == "3":
       vieworder()
    elif choice == "4":
        break
    else:
        print("\nInvalid data entered. Please select a number 1-4.\n")

def addsocks():
    global quantity
    qty = int(input("Enter quantity to add: "))
    quantity = quantity + qty
    display()

def remove():
    global quantity 
    qty = int(input("Enter quantity to remove: "))
    quantity = quantity - qty
    display()

def vieworder():
    global quantity
    global socks
    global ship
    socks = 9.75 
    if quantity >= 5:
        ship = 1.5
    else: 
        ship = 2.25
    quantity*=socks 
    total = ship+quantity  
    
    print("The total(quantity) is",quantity)

while True:
    choice = menu()
    if choice == 1:
        add()
    elif choice == 2:
        remove()
    elif choice == 3:
        display()
    elif choice == 4:
        break
    else:
        print("Invalid entry.")

    
