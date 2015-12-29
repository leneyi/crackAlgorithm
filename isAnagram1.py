
def isAnagram1(s,t):
    numArrays = [0]*26;
    numArrayt = [0]*26;
    for i in range(0,len(s)):
        numArrays[ord(s[i])-ord('a')] +=1;       
    for i in range(0,len(t)):
        numArrayt[ord(t[i])-ord('a')] +=1;
    return numArrays == numArrayt;
print(isAnagram1('good','godoo'));
