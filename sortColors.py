
def sortColors(S):
    red = -1;
    white = -1;
    blue = -1;
    
    for i in range(0,len(S)):
        if S[i] == 0:
           blue +=1;
           S[blue] =2;
           white +=1;
           S[white]=1;
           red +=1;
           S[red] = 0;
        elif S[i] ==1:
           blue +=1;
           S[blue] = 2;
           white +=1;
           S[white] =1;
        elif S[i] == 2:
           blue +=1;
           S[blue] = 2;
           

