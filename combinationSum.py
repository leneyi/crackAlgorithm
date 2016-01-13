def combinationSum(candidates,target):
    res = [];
    dfs(0,target,candidates,[],res);
    return res;
def dfs(start,target,candidates,path,res):
    if target < 0:
        return;
    if target == 0:
        res.append(path);
        return;
    for i in range(start,len(candidates)):
        dfs(i, target-candidates[i],candidates,path+[candidates[i]],res);


print(combinationSum([2,3,6,7],7));
