def intersection(nums1, nums2):
    res = [];
    for i in nums1 :
        if i in nums2 and i not in res:
            res.append(i);
    print (res);
    return res;
nums1 = [1,2,2,1,3,5,6];
nums2 = [2,2,4,3,5];
intersection(nums1, nums2);
