def topKFrequent(nums, k):
    dictEle = {};
    for i in nums:
        if i not in dictEle:
            dictEle[i] = 1;
        else:
            dictEle[i] +=1;
    arr1 = sorted(dictEle.items(), key = lambda a:a[1], reverse = True);
    arr2 = [];
    for i in range(len(arr1)):
        arr2.append(arr1[i][0]);
    print arr2[0:k];
    return arr2[0:k];
nums = [1,1,3,5,1,2,2,3,3,4];
topKFrequent(nums,3);
