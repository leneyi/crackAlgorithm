def isPalindrome(S):
    if(len(S)==0):
        return True;
    i =0;
    j = len(S)-1;
    while(i<j):
        if not S[i].isalpha() and not S[i].isalnum():
            i +=1;
            continue;
        if not S[j].isalpha() and not S[j].isalnum():
            j -=1;
            continue;
        s1 = S[i].lower();
        s2 = S[j].lower();
        if not s1 == s2:
           return False;
        i +=1;
        j -=1;
    return True;

print(isPalindrome('race a car'));
