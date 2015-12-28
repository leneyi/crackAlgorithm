
def threeSum(nums):
     # use three pointers to traverse the elment
     # i j = i+1 k = len-1
     # to avoid the duplicate, firstly sort, then traverse, avoid duplicates
     # use a list to store result
     nums.sort();
     res = [];
     for i in range(0,len(nums)-2):
         if (i>0 and nums[i]== nums[i-1]):
             continue;
         j = i+1;
         k = len(nums)-1;
         sum = 0-nums[i];
         while(j<k):
             if nums[j]+nums[k] == sum:
                res.append((nums[i],nums[j],nums[k]));
                while(j<k and nums[j] == nums[j+1]): j +=1;
                while(j<k and nums[k] == nums[k-1]): k -=1;
                j +=1;
                k -=1;
             elif nums[j]+nums[k]< sum:
                 j +=1;
             else:
                k -=1;
     return res;
                 

print(threeSum([-1, 0, 1,6, 4,-3,-5,7]));
