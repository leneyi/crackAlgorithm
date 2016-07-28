
def strStr(haystack, needle):
    hlen = len(haystack);
    nlen = len(needle);
    if nlen > hlen:
        return -1;
    if haystack == "" and needle == "":
        return 0;
    j = 0;
    for i in range(hlen-nlen+1):
        while j < nlen:
            if haystack[i+j] == needle[j]:
                j +=1;
            else:
                j = 0;
                break;
        if j == nlen:
           return i;
    return -1;

        
            
        

