def removeNthFromEnd(head, n):
    if head is None:
        return head;
    fast = head;
    slow = head;
    curr = head;
    count = 0;
    while curr is not None:
      curr = curr.next;
      count +=1;
    if n == count:
        return head.next;
    for i in range(n):
      fast = fast.next;
    while fast is not None and fast.next is not None:
       fast = fast.next;
       slow = slow.next;
    slow.next = slow.next.next;
    return head;
