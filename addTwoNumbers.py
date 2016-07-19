
def addTwoNumbers(l1,l2):
    l3 = ListNode(0);
    curr = l3;
    carry = 0;
    while l1 or l2 or carry:
        val1 = 0;
        val2 = 0;
        if l1:
           val1 = l1.val;
           l1 = l1.next;
        if l2:
           val2 = l2.val;
           l2 = l2.next;
        temp = val1 + val2 + carry;
        if temp >=10:
            temp -=10;
            carry = 1;
        else:
            carry = 0;
        curr.next = ListNode(temp);
        temp = 0;
        curr = curr.next;
    return l3.next;
           
        

