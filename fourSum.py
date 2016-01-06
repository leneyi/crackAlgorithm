
def fourSum(nums,target):
    res = [];
    nums.sort();
    findNsum(nums,target,4,[],res);
    return res;

def findNsum(nums,target,N,result,res):       
    if N<2 or N> len(nums) or target>nums[-1]*N or target< nums[0]*N:
       return;
    if N ==2:
       i =0;
       j = len(nums)-1;
       while(i<j):
           sum = nums[i]+nums[j];
           if sum == target:
              res.append(result+[nums[i],nums[j]]);
              while (i<j and nums[i] == nums[i+1]):
                   i +=1;
              while (i<j and nums[j] == nums[j-1]):
                   j -=1;
              i +=1;
              j -=1;
           elif sum<target:
              i +=1;
           else:
              j -=1;                  
    else:
       
      for i in range(0,len(nums)-N+1):
        if i>0 and nums[i]==nums[i-1]:
           continue;
        
        findNsum(nums[i+1:],target-nums[i], N-1, result+[nums[i]],res);

print(fourSum([1,0,-1,0,2,-2],0));
