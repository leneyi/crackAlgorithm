
def intersect(nums1,nums2):
     dict1 = {}
     list1 = [];
     for i in nums1:
         if i not in dict1:
             dict1[i] = 1;
         else:
             dict1[i] +=1;
     for i in nums2:
        if i in dict1 and dict1[i]>0:
           list1.append(i);
           dict1[i] -=1;
     print list1;
     return list1;
    
nums1 = [1,2,2,3,2,4,1];
nums2 = [2,2,3,3,4];
intersect(nums1,nums2);
           
 
