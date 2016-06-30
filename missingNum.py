
def missingNum(nums):
    num = len(nums);
    sumi = 0;
    for i in range(num+1):
        sumi +=i;
    sumNums = 0;
    for i in range(len(nums)):
        sumNums += nums[i];
    res = sumi - sumNums;
    print res;
    return res;
a = [0,1,2,4];
missingNum(a);
