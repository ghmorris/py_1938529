
def pyramidVolume(height, baseLength): #dont forget the colon 
    baseArea = baseLength **2 
    return height * baseArea

def main():
    result1 = pyramidVolume(9,10)
    result2 = pyramidVolume(0,0)

    print('Expected 900')
    print (result1)
    print('Expected 0')
    print (result2)
    
main()