
def singleNumber(nums):
    sum = 0;
    for i in range(0,len(nums)):
     sum ^= nums[i];
    return sum;
