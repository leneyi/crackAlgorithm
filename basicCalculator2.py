
def calculate(S):
    stack = [];
    sign = '+';
    num = 0;
    for i in range(0,len(S)):
        if S[i].isdigit():
            num = 10*num +ord(S[i])-ord('0');
        if not S[i].isdigit() and not S[i] == '' or i == len(S)-1:
            if sign =='+':
                stack.append(num);
            elif sign =='-':
                stack.append(-num);
            elif sign =='*':
                stack.append(stack.pop()*num);
            else:
                temp = stack.pop();
                if temp/num <0 and temp%num!=0:
                   stack.append(temp/num+1);
                else:
                   stack.append(temp/num);

            sign = S[i];
            num =0;
    return sum(stack);
print(calculate('3+3/2'));
