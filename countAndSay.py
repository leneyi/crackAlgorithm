def countAndSay(n):
    res = '1';
    for i in range(n-1):
        res = generator(res);
    return res;

def generator(strin):
    count = 1;
    res ='';
    i =0;
    while i < len(strin)-1:
        if strin[i] == strin[i+1]:
            count +=1;
        else:
            res +=str(count) + strin[i];
            count = 1;
        i +=1;
    res +=str(count) + strin[i];
    return res;
