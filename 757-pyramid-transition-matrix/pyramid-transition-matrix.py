from functools import cache
from collections import defaultdict
from itertools import pairwise, product
from typing import List

class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        transitions_map = defaultdict(list)
        for transition in allowed:
            left_block, right_block, top_block = transition[0], transition[1], transition[2]
            transitions_map[left_block, right_block].append(top_block)
      
        @cache
        def can_build_pyramid(current_level: str) -> bool:
            if len(current_level) == 1:
                return True
            next_level_options = []
            for left_block, right_block in pairwise(current_level):
                possible_blocks = transitions_map[left_block, right_block]
                if not possible_blocks:
                    return False
              
                next_level_options.append(possible_blocks)
            for next_level_combination in product(*next_level_options):
                next_level_string = ''.join(next_level_combination)
                if can_build_pyramid(next_level_string):
                    return True
            return False
        return can_build_pyramid(bottom)