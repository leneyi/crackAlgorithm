def longestCommonPrefix(strs):
    res = '';
    i = 0;
    j = 0;
    if len(strs) == 0:
         return res;
    if len(strs) == 1:
         print strs[0];
         return strs[0];
    for i in range(len(strs[0])):
        for j in range(1, len(strs)):
            if i >= len(strs[j]) or strs[0][i] != strs[j][i]:
                print res;
                return res;
        res +=strs[0][i];
    print res;
    return res;

longestCommonPrefix(["an", "abd", "abc"]);
