
def combinationSum2(candidates, target):
    candidates.sort();
    return search(candidates, 0, target);
    

def search(candidates, start, target):
    if target == 0:
        return [[]];
    res = [];
    for i in range(start, len(candidates)):
        if i != start and candidates[i] == candidates[i-1]:
            continue;
        if candidates[i] > target:
            break;
        for r in search(candidates, i+1, target- candidates[i]):
            res.append([candidates[i]]+r);
    return res;
print(combinationSum2([10, 1, 2, 7, 6, 1, 5],8));
  
