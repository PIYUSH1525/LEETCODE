class Solution:
    def minJumps(self, arr: List[int]) -> int:
        value_to_indices = defaultdict(list)
        for index, value in enumerate(arr):
            value_to_indices[value].append(index)
        queue = deque([0])
        visited = {0}
        steps = 0
        while True:
            for _ in range(len(queue)):
                current_index = queue.popleft()
                if current_index == len(arr) - 1:
                    return steps
                next_indices = [current_index + 1, current_index - 1]
                same_value_indices = value_to_indices.pop(arr[current_index], [])
              
                for next_index in (*next_indices, *same_value_indices):
                    if 0 <= next_index < len(arr) and next_index not in visited:
                        queue.append(next_index)
                        visited.add(next_index)
            steps += 1