
def maxSubArray(S):
    if len(S) == 0:
        return 0;
    dp = len(S)*[0];
    dp[0] = S[0];
    maxi = dp[0];
    for i in range(1,len(S)):
        if dp[i-1]>0:
            dp[i] = dp[i-1]+S[i];
        else:
            dp[i] = S[i];
        maxi= max(dp[i],maxi);
    return maxi;

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]));
