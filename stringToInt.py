
def stringToInt(str):
    # deal with blank space, sign and overflow
    index = 0;
    res = 0;
    sign = 1;
    if len(str) == 0:
        return 0;
    while index< len(str) and str[index] == ' ':
        index +=1;
    if str[index] == '+' or str[index] == '-':
        sign = 1 - 2*(str[index] == '-');
        index +=1;
    while index< len(str) and ord(str[index])>= ord('0') and ord(str[index])<= ord('9'):
        temp = int(str[index]);
        if res> 214748364 or (res == 214748364 and temp>7 ):
            if sign == 1:
                print 2147483647;
                return 2147483647;
            if sign == -1:
                print -2147483648;
                return -2147483648;       
        res = res*10 + temp;
        index +=1;
    #print sign*res;
    return sign*res;
stringToInt('-2147483649');
