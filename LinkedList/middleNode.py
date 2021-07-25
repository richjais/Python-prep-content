def middleNode(head: ListNode) -> ListNode:
    fastptr = head
    slowptr = head
    while fastptr and fastptr.next:
        fastptr = fastptr.next.next
        slowptr = slowptr.next
    return slowptr

