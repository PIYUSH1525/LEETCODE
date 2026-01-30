from typing import List
from functools import cache
from math import inf
class TrieNode:
    __slots__ = ["children", "word_id"]
  
    def __init__(self):
        self.children: List[TrieNode | None] = [None] * 26
        self.word_id = -1
class Solution:
    def minimumCost(self,source: str,target: str,original: List[str],changed: List[str],cost: List[int],) -> int:
        num_transformations = len(cost)
        max_nodes = num_transformations << 1  
        graph = [[inf] * max_nodes for _ in range(max_nodes)]
        for i in range(max_nodes):
            graph[i][i] = 0
        trie_root = TrieNode()
        word_counter = 0
      
        def insert_word(word: str) -> int:
            nonlocal word_counter
            current_node = trie_root
            for char in word:
                char_index = ord(char) - ord('a')
                if current_node.children[char_index] is None:
                    current_node.children[char_index] = TrieNode()
                current_node = current_node.children[char_index]
            if current_node.word_id < 0:
                current_node.word_id = word_counter
                word_counter += 1
              
            return current_node.word_id
      
        @cache
        def find_min_cost(position: int) -> int:
            if position >= len(source):
                return 0
            result = find_min_cost(position + 1) if source[position] == target[position] else inf
            source_node = trie_root
            target_node = trie_root
          
            for end_pos in range(position, len(source)):
                source_char_index = ord(source[end_pos]) - ord('a')
                target_char_index = ord(target[end_pos]) - ord('a')
              
                source_node = source_node.children[source_char_index]
                target_node = target_node.children[target_char_index]
                if source_node is None or target_node is None:
                    break
                if source_node.word_id < 0 or target_node.word_id < 0:
                    continue
                transformation_cost = graph[source_node.word_id][target_node.word_id]
                result = min(result, find_min_cost(end_pos + 1) + transformation_cost)
          
            return result
        for orig_str, changed_str, trans_cost in zip(original, changed, cost):
            orig_id = insert_word(orig_str)
            changed_id = insert_word(changed_str)
            graph[orig_id][changed_id] = min(graph[orig_id][changed_id], trans_cost)
        for k in range(word_counter):
            for i in range(word_counter):
                if graph[i][k] >= inf:
                    continue
                for j in range(word_counter):
                    if graph[i][k] + graph[k][j] < graph[i][j]:
                        graph[i][j] = graph[i][k] + graph[k][j]
        min_cost = find_min_cost(0)
        return -1 if min_cost >= inf else min_cost
