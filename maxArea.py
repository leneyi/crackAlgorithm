def maxArea(height):
    maxarea = 0;
    left = 0;
    right = len(height)-1;
    while(left < right):
        maxarea = max(maxarea,(right-left)*min(height[right],height[left]));
        if(height[left]>height[right]):
           right -=1;
        else:
           left +=1;
    return maxarea;

print(maxArea([1,6,5,8,3]));
