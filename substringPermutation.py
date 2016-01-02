'''
s = "dlwercxhhcd", p = "hdch"
return True
'''

def subPermutation(s,p):
    leng = len(p);
    perm = [];
    for i in range(0,len(s)-leng+1):
        s1 = s[i:i+4];
        if anagram(s1,p):
            return True;
    return False;


def anagram(s,p):
    nums1 = 26*[0];
    nums2 = 26*[0];
    for i in range(0,len(s)):
        nums1[ord(s[i])-ord('a')] +=1;
    for i in range(0,len(p)):
        nums2[ord(p[i])-ord('a')] +=1;       
    return nums1 == nums2;

print(subPermutation("dlwercxhhcd","hdch"));
