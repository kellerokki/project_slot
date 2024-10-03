#Started by collecting users input

MAX_LINES = 3 # an all uppercase, global variable

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

#Copied all of the above to below

def get_number_of_lines(): #This function is responsible for determining the amount of lines to bet on.
    while True:
        lines = input("Enter the number of lines to bet on. (1-" + str(MAX_LINES) + ")")
        if lines.isdigit(): #if input is a number, conver it into int
            lines = int(lines) 
            if 1 <= lines <= MAX_LINES: #checks to see if the given lines is in between the range of 1-3.
                break
            else:
                print("Enter a valid number of lines.") #directions for needing to input a valid number of lines.
        else:
            print("Please enter a number.")
    return lines #returns the input value

def main():
    balance = deposit()
    lines = get_number_of_lines()
    print(balance, lines)

main()