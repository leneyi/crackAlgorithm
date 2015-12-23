
def twoSum(S,target):
    if len(S) <=1:
        return False;
    dict = {}
    for i in range(0,len(S)):
      if (target - S[i]) in dict:
          return [dict[target-S[i]]+1,i+1];
      else:
          dict[S[i]] = i;
    return None;

print(twoSum([3,2,4],7));
