COUNTRY = 6 
MEDALS = 3 

countries = [
    'Canada',
    'China',
    'Korea',
    'Japan',
    'Russia',
    'United States',
]

counts = [ 
    [1,0,1],
    [1,1,0],
    [0,0,1],
    [1,0,0], 
    [1,1,0],
    [1,1,1],
]

print('\t\tCountry \t Gold \t Silver \t Bronze \t total')

for i in range(COUNTRY): 
    print('\t\t',countries[i], end='')
    total = 0 
    for j in range(MEDALS): 
        total += counts[i][j]
        print('\t',counts[i][j], end='')

    print('\t',total, end='')
    print()