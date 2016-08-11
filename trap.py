
def trap(height):
    left = 0;
    right = len(height)-1;
    maxL = 0;
    maxR = 0;
    maxi = 0;
    while (left< right):
      maxL = max(maxL, height[left]);
      maxR = max(maxR, height[right]);
      if maxL < maxR:
          maxi += maxL - height[left];
          left +=1;
      else:
          maxi += maxR -height[right];
          right -=1;
    return maxi;
print(trap([0,1,0,2,1,0,1,3,2,1,2,1]));
        

