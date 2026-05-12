class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        sorted_tasks = sorted(tasks, key=lambda task: task[0] - task[1])
        total_initial_effort = 0 
        current_energy = 0  
        for actual_effort, minimum_effort in sorted_tasks:
            if current_energy < minimum_effort:
                effort_deficit = minimum_effort - current_energy
                total_initial_effort += effort_deficit
                current_energy = minimum_effort
            current_energy -= actual_effort
      
        return total_initial_effort