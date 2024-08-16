

values = [1]

userInput = input("Enter a value or Q to quit")

while userInput.upper() != 'Q': 
    values.append(float(userInput))
    userInput = input("Enter a value or Q to quit")


for element in values: 
    print('element, end=''') 

if element == max(values):
    print('<< Max Val', end='')

if element == min(values):
    print('<< Min Val', end='')
    
    print()