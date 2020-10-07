keepGoing = 'y'

# Infinite loop
while keepGoing == 'y':
    # Get salesperson's sales and commission rate
    sales = float(input('Enter the amount of sales: '))
    commRate = float(input('Enter the commission rate: '))

    # Calculate the commission
    commission = sales * commRate

    # Display comm
    print('The commission is $',
          format(commission, ',.2f'), sep='')