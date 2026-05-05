class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        current = head
        list_length = 0
        while current:
            list_length += 1
            current = current.next
        k = k % list_length
        if k == 0:
            return head
        fast_pointer = head
        slow_pointer = head
        for _ in range(k):
            fast_pointer = fast_pointer.next
        while fast_pointer.next:
            fast_pointer = fast_pointer.next
            slow_pointer = slow_pointer.next
        new_head = slow_pointer.next
        slow_pointer.next = None
        fast_pointer.next = head
      
        return new_head