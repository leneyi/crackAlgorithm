def reverseWords(s):
    """
    :type s: str
    :rtype: str
    """
    s = s.strip();
    if len(s) == 0:
        return '';   
    s1 = s.split();
    temp = '';
    for i in range(len(s1)-1,0,-1):
        temp +=s1[i]+ ' ';
    temp +=s1[0];
    return temp;

print(reverseWords(""));
