#Program that converts amount of change into respective coin amounts
change = int(input("Please enter an amount in cents less than a dollar. \n"))
print("Your change will be: ")
print("Q:", change//25)
change = change%25
print("D:", change//10)
change = change%10
print("N:", change//5)
change = change%5
print("P:", change//1)
