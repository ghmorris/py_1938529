
def main(): 
    result1 = cubeVolume(2)
    result2 = cubeVolume(10)

    print('Small cube volume: %f' %result1)
    print('Big cube volume: %f' %result2)
def cubeVolume(sideLength): 
    return sideLength ** 2 

main() #calling main function at the end 
