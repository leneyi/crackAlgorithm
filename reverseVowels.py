
def reverseVowels(s):
    vowels = 'aeiouAEIOU'
    listS = list(s);
    voIndex = [i for i,j in enumerate (s) if j in vowels]
    i = 0;
    j = len(voIndex) -1;
    while i < j:
        listS[voIndex[i]],listS[voIndex[j]] = listS[voIndex[j]], listS[voIndex[i]]
        i +=1;
        j -=1;
    print  ''.join(listS);
    return ''.join(listS);
    
reverseVowels('leetcode');
