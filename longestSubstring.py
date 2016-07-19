def longestSub(s):
    start = 0;
    leng = 0;
    dictIndex = {};
    for i in range(len(s)):
        if s[i] in dictIndex and start <=dictIndex[s[i]]:
            start = dictIndex[s[i]]+1;
        else:
            leng = max(leng,i-start+1);
        dictIndex[s[i]] = i;
    print leng;
    return leng;
longestSub("pwwkew");
