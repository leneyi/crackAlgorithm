
def swapInPairs(head):
    if head is None or head.next is None:
        return head;
    n = head.next;
    head.next = swapInPairs(head.next.next);
    n.next = head;
    return n;
    
