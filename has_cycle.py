def has_cycle(head):
    """
    Check if a linked list has a cycle.
    """

    slow, fast = head
    
    while slow.next is not None:
        slow = slow.next 
        fast = fast.next.next
        
        if current.data == tracker.data:
            return True 
    
    return False