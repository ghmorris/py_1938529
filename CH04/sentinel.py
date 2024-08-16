total = 0 
count = 0 
salary = 0 

while salary >= 0: 
    salary = float(input('Enter -1 to quit or salary:'))

    if salary >= 0.0: 
        total += salary 
        count += 1 

average = 0 

if count > 0: 
    average = total / count 

print('The average salary is %f' %(average))