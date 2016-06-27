class ListNode(object):
     def __init__(self, x):
        self.val = x
        self.next = None
class Solution(object):
        def reverseLinkedList(head, m, n):
            dummyNode = ListNode(0)
            pre = dummyNode;
            dummyNode.next = head;

        # if m == n return it.
            if m == n:
                return head;
        #find the pre, which is before cur
            for i in range(0,m-1):
                pre = pre.next;

            reverse = None;
            curr = pre.next;

            for i in range(0, n-m+1):
                 next = curr.next;
                 curr.next = reverse;
                 reverse = curr;
                 curr = next;

            pre.next.next = curr;
            pre.next = reverse;
            print dummyNode.next.val;
            print dummyNode.next.next.val
            print dummyNode.next.next.next.val
            return dummyNode.next;
        if __name__=="__main__":
            head = ListNode(5);
            a = ListNode(6);
            b = ListNode(7);
            c = ListNode(8);
            d = ListNode(9);
            head.next = a;
            a.next = b;
            b.next = c;
            c.next = d;
            d.next = None;
            reverseLinkedList(head, 2, 4);
