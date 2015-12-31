
def wordBreak(s,wordDict):
    dp = [False]*(len(s)+1);
    dp[0] = True;
    for i in range(1,len(s)+1):
      for j in range(0,i):
          if s[j:i] in wordDict and dp[j] is True:
              dp[i] = True;
              break;
    return dp[len(s)];
print(wordBreak("leetcode",["leet","code"]));
