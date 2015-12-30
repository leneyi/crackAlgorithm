
def combinations(n,k):
    res = [];
    dfs(n,k,1,[],res);
    return res;
def dfs(n,k,start,path,res):
    if len(path) ==k:
       res.append(path);
       return;
    for i in range(start,n+1):
        dfs(n,k,i+1,path+[i],res);
print(combinations(4,2));
