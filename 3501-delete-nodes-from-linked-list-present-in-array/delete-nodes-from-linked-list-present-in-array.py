from typing import List, Optional
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        values_to_remove = set(nums)
        dummy_node = ListNode(next=head)

        current = dummy_node
        while current.next:
            if current.next.val in values_to_remove:
                current.next = current.next.next
            else:
                current = current.next
        return dummy_node.next