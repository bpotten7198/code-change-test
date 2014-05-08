import time 
bottles=10 #Sets bottles to 10
for x in range(bottles,0,-1): #Creates a loop which loops 10 times
    print("{0} green bottles, hanging on the wall\n{0} green bottles, hanging on the wall".format(x)) #Prints out how many bottles there are
    print("And if 1 green bottle should accidently fall,\nThere'll be {0} green bottles hanging on the wall.".format(x-1)) #Prints out how many bottles there will be
    time.sleep(1) #Pauses the code for 1 second
