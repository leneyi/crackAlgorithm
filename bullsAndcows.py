
def getHint(secret, guess):
    nums = [0]*10;
    bulls = 0;
    cows = 0;
    for i in range(0,len(secret)):
        if secret[i] == guess[i]:
            bulls +=1;
        else:
            if nums[int(secret[i])]<0:
                cows +=1;
            if nums[int(guess[i])]>0:
                cows +=1;
            nums[int(secret[i])] +=1;
            nums[int(guess[i])] -=1;
    print (str(bulls) + "A" + str(cows)+ "B");        
    return str(bulls) + "A" + str(cows)+ "B"
getHint("1807", "7810");
