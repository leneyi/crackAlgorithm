
def removeDuplicates(num):
    if len(nums) ==0 or len(nums) == 1:
        return len(nums);
    currP = 1;
    rightP = 0;
    while currP < len(nums):
        if nums[currP] != nums[rightP]:
            rightP +=1;
            nums[rightP] = nums[currP];
        currP +=1;
    return rightP+1;
        
            
        

