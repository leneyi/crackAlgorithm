
def threeSumClosest(nums, target):
    #firstly sort
    nums.sort();
    result = nums[0]+nums[1]+nums[2];

    for i in range(len(nums)-2):
      j = i+1;
      k = len(nums)-1;
      while j <k:
          sum = nums[i]+nums[j]+nums[k];
          if sum == target:
            return sum;
          if abs(sum-target) < abs(result-target):
            result = sum;
          if sum < target:
              j +=1;
          elif sum>target:
              k -=1;
    return result;

print(threeSumClosest([0,0,0,8,6,-9,-4,-7],5));
          
 
