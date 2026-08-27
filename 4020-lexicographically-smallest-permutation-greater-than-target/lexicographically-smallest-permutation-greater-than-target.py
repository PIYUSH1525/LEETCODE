class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        pool = [0] * 26
        for char in s:
            pool[ord(char) - ord('a')] += 1
        
        n = len(s)

        def build(index):
            if index == n:
                return ""
            
            targetChar = target[index]
            targetIndex = ord(targetChar) - ord("a")

            if pool[targetIndex] > 0:
                pool[targetIndex] -= 1
                result = build(index + 1)

                if result != "":
                    return targetChar + result
                
                pool[targetIndex] += 1

            
            for i in range(targetIndex + 1, 26):
                if pool[i] > 0:
                    pool[i] -= 1
                    remaining = []

                    for j in range(26):
                        if pool[j] > 0:
                            remaining.append(chr(j + ord('a')) * pool[j])
                    
                    return chr(i + ord('a')) + "".join(remaining)
            return ""

        return build(0)

