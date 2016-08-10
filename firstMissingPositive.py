
def firstMissingPositive(nums):
    if len(nums) ==0:
        return 1;
    #move the num to the corresponding index
    for i in range(len(nums)):
        curr = nums[i];
        while curr <= len(nums) and curr >0 and curr != nums[curr-1]:
           temp = nums[curr-1];
           nums[curr-1] = curr;
           curr = temp;
    #find the num which is not on the right index
    for i in range(len(nums)):
        if nums[i] != i+1:
            return i+1;
    return len(nums)+1;
print(firstMissingPositive([3,4,-1,1]));


           
    


