RATE = 5.0 
INITIAL_BALANCE = 10000.0 

balance = INITIAL_BALANCE
numYears = int(input('Enter the number of years:'))

for i in range(1, 1+numYears): 
    interest = balance * RATE/100 
    balance += interest 

    print('%4d %10.2f' %(i, balance))