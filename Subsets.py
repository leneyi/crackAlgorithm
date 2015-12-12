

def subsets(S):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    ans = [[]];
    if not S:
      return ans;
    else:
      # non-descending order
      S.sort();
      ans = subsets(S[1:]);
      return ans+[[S[0]] + ele for ele in ans];
subsets([1,2,3]);
