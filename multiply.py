
def multiply(self,num1, num2):
    result = [0]*(len(num1)+len(num2));
    curr = len(result) -1;
    for n1 in reversed(num1):
        tempPos = curr;
        for n2 in reversed(num2):
            result[tempPos] += int(n1)*int(n2);
            result[tempPos-1] += result[tempPos]/10;
            result[tempPos] %= 10;
            tempPos -=1;
        curr -=1;
    pos = 0;
    while (pos< len(result)-1 and result[pos] == 0):
        pos +=1;
    return ''.join(map(str,result[pos:]));

    

