#Started by collecting users input

def deposit(): #This function is responsible for collecting user input
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit(): #if input is a number, conver it into int
            amount = int(amount) 
            if amount > 0: #if the input is greater than 0, break the while loop.
                break
            else:
                print("The amount must be greater than 0.") #directions for needing to input greater number than 0.
        else:
            print("Please enter a number.")
    return amount #returns the input value

deposit()