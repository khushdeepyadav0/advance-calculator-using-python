# myself khushdeep yadav this is my project using python nowadays i just started coding from few 3 days and making this advance calculator using python.

import math

# code for input a value
value1 = float(input( 'Enter a value' '\n' ))
factorial = 0

# code for operation details 
print( '\n''Choose operation you want to perform' '\n' '1 for Addition' '\n' '2 for Substraction' '\n' '3 for Multiplication' '\n' '4 for Division' '\n' '5 for Power' '\n' '6 for Factorial' '\n' )

# code for selected option
option = float(input( 'Enter operation value 1 to 6 ' '\n'))

# code for specific operation choosed by user
if option == 1:
    value2 = float(input( '\nEnter another value for adding with '+ str(value1) + '\n' ))
    answer = value1 + value2
    print('\nAnswer is ',answer)
    
elif option ==2:
    value2 = float(input( '\nEnter another value for subtracting with '+ str(value1) + '\n' ))
    answer = value1 - value2
    print('\nAnswer is ',answer)
    
elif option ==3:
    value2 = float(input( '\nEnter another value for multiplying with '+ str(value1) + '\n' ))
    answer = value1 * value2
    print('\nAnswer is ',answer)
    
elif option == 4:
    value2 = float(input( '\nEnter another value for dividing with '+ str(value1) + '\n' ))
    answer = value1 / value2
    print('\nAnswer is ',answer)
    
elif option == 5:
    value2 = float(input( '\nEnter another value for power of '+ str(value1) + '\n' ))
    answer = value1 ** value2
    print('\nAnswer is ',answer)
    
else:
    answer=math.factorial(int(value1))
    print('\nAnswer is ',answer)
