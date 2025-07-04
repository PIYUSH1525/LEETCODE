class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        if all(op == 0 for op in operations):
            return 'a'
        lens = [1]
        for op in operations:
            lens.append(lens[-1] * 2)

        shift = 0
        for i in reversed(range(len(operations))):
            half = lens[i]
            op = operations[i]
            if k > half:
                k -= half
                if op == 1:
                    shift += 1

        return chr((ord('a') - ord('a') + shift) % 26 + ord('a'))
        