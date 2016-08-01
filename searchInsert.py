
def searchInsert(nums, target):
    low = 0;
    high = len(nums) -1;
    while low <= high:
        mid = low + (high-low)/2;
        if target == nums[mid]:
            return mid;
        if target < nums[mid]:
            high = mid-1;
        elif target >= nums[mid]:
            low = mid +1;
    return low;
