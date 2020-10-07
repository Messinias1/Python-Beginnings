# This program calculates sales of commission

# Create variable to control loop
keepGoing = "y"

# Calculate a series of commissions
while keepGoing == "y":
    # Get a salespersons sales and c rate
    sales = float(input("Enter the amount of sales: "))
    commRate = float(input("Enter the commission rate: "))

    # Calculate the commission
    commission = sales * commRate

    # Display the commission
    print("The commission is $",
          format(commission, ',.2f'), sep='')

    # See if user wants to do another
    keepGoing = input("Do you want to calculate another "
                      + "Commission (Enter y for yes): ")

