
def romanToInt(s):
    res = 0;
    dictR = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000};
    for i in range(0, len(s)-1):
        if dictR[s[i]]<dictR[s[i+1]]:
            res -= dictR[s[i]] ;
        else:
            res += dictR[s[i]];
    res +=dictR[s[len(s)-1]];
    print res;
    return res;
romanToInt('LXXX');
        
      
