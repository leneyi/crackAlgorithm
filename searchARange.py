
def searchRange(nums, target):
    ranges = [len(nums),-1];
    search(nums,target,0,len(nums)-1,ranges);
    if ranges[0] > ranges[1]:
        range[0] = -1;
    return ranges;

def search(nums, target,left, right, ranges):
    if left> right:
        return;
    mid = left + (right-left)/2;
    if nums[mid] == target:
        if (mid< ranges[0]):
           ranges[0] =mid;
           search(nums, target, left, mid-1,ranges);

        if mid >ranges[1]:
           ranges[1]= mid;
           search(nums, target, mid+1,right, ranges);
    elif nums[mid]<target:
         search(nums, target, mid+1,right,ranges);
    else:
        search(nums,target, left, mid-1,ranges);

print(searchRange([5,7,7,8,8,10],8));
