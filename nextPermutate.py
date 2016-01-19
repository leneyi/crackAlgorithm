def nextPermute(nums):
    # find  a small in the front and a big in the back
    if len(nums) == 0 or len(nums)==1:
        return;    
    i = len(nums)-1;
    j = len(nums)-2;
    while (j>=0):
        if nums[j] >= nums[j+1]:
            j -=1;
        else:
            break;
    if(j>=0):
        while nums[i] <= nums[j]:
            i -=1;
        swap(nums,i,j);
    reverse(nums, j+1,len(nums)-1);                
    print(nums);
def swap(nums,i,j):
    temp = nums[i];
    nums[i] = nums[j];
    nums[j] = temp;
    
def reverse(nums,i,j):
    while(i<j):
        swap(nums,i,j);
        i +=1;
        j -=1;
nextPermute([1,2,3])    

