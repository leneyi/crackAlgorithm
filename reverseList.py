
def reverseList(S):
    if S is None or S.next is None:
        return S;
    pre = None;
    curr = S;
    while (not curr is None):
        next = curr.next;
        curr.next = pre;
        pre = curr;
        curr = next;
    return pre;
        

