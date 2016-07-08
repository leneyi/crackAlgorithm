class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """        
        self.sumi = nums;
        for i in range(1, len(nums)):
            self.sumi[i] += self.sumi[i-1];
    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """        
        if i == 0:
            return self.sumi[j];
        return self.sumi[j]-self.sumi[i-1];
