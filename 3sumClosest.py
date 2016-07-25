def threeSumClosest(nums,target):
    nums.sort();
    res = nums[0] + nums[1] + nums[2];
    if res == target :
        return target;
    for i in range(0,len(nums)-2):
        j = i+1;
        k = len(nums)-1;
        while j < k:
            temp = nums[i] + nums[j] + nums[k];
            if temp == target:
                return target;
            if abs(temp - target) < abs(res - target):
                res = temp;
            if temp < target:
                j +=1;
            elif sum > target:
                k -=1;
    return res;
            
            
            
    


