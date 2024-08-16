season = "summer"
temperature = 90.0 
air_conditioner = False 

if season == "summer":
    if temperature > 72: 
        air_conditioner = True 
    else: 
        air_conditioner = False 

if air_conditioner: 
    print ('Air conditioner is on')
else: 
    print('Air conditioner is off')