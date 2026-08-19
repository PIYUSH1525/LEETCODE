from collections import defaultdict
from typing import List

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        reserved_by_row = defaultdict(int)
        for row, seat in reservedSeats:
            reserved_by_row[row] |= 1 << (10 - seat)
        family_group_masks = (0b0111100000, 0b0000011110, 0b0001111000)
        total_families = (n - len(reserved_by_row)) * 2
        for row_reservation in reserved_by_row.values():
            for mask in family_group_masks:
                if (row_reservation & mask) == 0:
                    row_reservation |= mask
                    total_families += 1
      
        return total_families
