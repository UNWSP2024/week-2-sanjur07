
def average_age():
    # Get User Input
    friend1 = int(input("Enter age:"))
    friend2 = int(input("Enter age:"))
    friend3 = int(input("Enter age:"))
    friend4 = int(input("Enter age:"))
    friend5 = int(input("Enter age:"))
    # Sum ages
    sum = int((friend1 + friend2 + friend3 + friend4 + friend5))
    # Average the ages
    average = float(sum/5)
    # Print the results
    print(average)


average_age()