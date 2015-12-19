
def isValid(S):
    dict1 = {']':'[',')':'(','}':'{'};
    stack = [];
    for i in range(0,len(S)):
       if S[i] in dict1.values():
          stack.append(S[i]);
       if S[i] in dict1:
          if (len(stack) == 0 or not stack.pop()== dict1[S[i]] ):
              return False;
    if not len(stack)==0:
       return False;
    return True;
print(isValid('()[][][]'));
