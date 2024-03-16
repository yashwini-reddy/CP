def removeElements(ListNode):
    prev=ListNode(0)
    temp=prev
    while head:
        if head.val!=val:
            prev.next=head
            prev=prev.next
        head = head.next
    prev.next=None
    return temp.next
