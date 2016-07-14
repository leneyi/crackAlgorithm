
def swapInPairs2(head):
    dummy =ListNode(0);
    dummy.next = head;
    curr = dummy;
    while curr.next and curr.next.next:
        first = curr.next;
        sec = curr.next.next;
        first.next = sec.next;
        sec.next = first;
        curr.next = sec;
        curr = sec.next;
    return dummy.next;
        
  
