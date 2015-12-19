
def permute(nums):
    res = [];
    generate([],res,nums);
    return res;

def generate(path, res, nums):
    if not nums:
      res.append(path);
    for i in range(len(nums)):
        generate(path + [nums[i]], res, nums[:i]+nums[i+1:]);
    

print(permute([1,2,3]));
