from collections import deque

class TrieNode:
    def __init__(self):
        self.children = {}
        self.fail = None
        self.count = 0  # Tracks how many patterns end at this exact node

class Solution:
    def numOfStrings(self, patterns: list[str], word: str) -> int:
        root = TrieNode()
        
        # ==========================================
        # STEP 1: Build the standard Trie
        # ==========================================
        for p in patterns:
            node = root
            for char in p:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            # Accumulate count to handle duplicate patterns (like ["a", "a"])
            node.count += 1
            
        # ==========================================
        # STEP 2: Build Failure Links using BFS
        # ==========================================
        queue = deque()
        
        # Initialize depth-1 nodes: their failure link always points to root
        for char, child in root.children.items():
            child.fail = root
            queue.append(child)
            
        while queue:
            curr = queue.popleft()
            for char, child in curr.children.items():
                fail_node = curr.fail
                
                # Walk up the failure chain until we find a node that has the same character
                while fail_node is not None and char not in fail_node.children:
                    fail_node = fail_node.fail
                    
                # If we found a valid suffix, point the fail link to it. Otherwise, point to root.
                if fail_node is not None:
                    child.fail = fail_node.children[char]
                else:
                    child.fail = root
                    
                queue.append(child)
                
        # ==========================================
        # STEP 3: Scan the word once and count matches
        # ==========================================
        res = 0
        curr = root
        for char in word:
            # If the current character doesn't match, follow the failure link (the "safety net")
            while curr is not None and char not in curr.children:
                curr = curr.fail
                
            # Move to the next node if a match was found, otherwise reset to root
            if curr is not None:
                curr = curr.children[char]
            else:
                curr = root
                
            # Walk up the failure chain to collect all nested/suffix matches ending at this position
            temp = curr
            while temp is not None and temp != root:
                res += temp.count
                # Set count to 0 so we don't double-count this pattern if it appears again later
                temp.count = 0 
                temp = temp.fail
                
        return res