from typing import List
from sortedcontainers import SortedList


class TaskManager:
    def __init__(self, tasks: List[List[int]]):
        self.task_info = {}
        self.priority_queue = SortedList()
        for task in tasks:
            self.add(task[0], task[1], task[2])

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.task_info[taskId] = (userId, priority)
        self.priority_queue.add((-priority, -taskId))

    def edit(self, taskId: int, newPriority: int) -> None:
        user_id, old_priority = self.task_info[taskId]
        self.priority_queue.discard((-old_priority, -taskId))
        self.task_info[taskId] = (user_id, newPriority)
        self.priority_queue.add((-newPriority, -taskId))

    def rmv(self, taskId: int) -> None:
        _, priority = self.task_info[taskId]
        self.task_info.pop(taskId)
        self.priority_queue.remove((-priority, -taskId))

    def execTop(self) -> int:
        if not self.priority_queue:
            return -1
        task_id = -self.priority_queue.pop(0)[1]
        user_id, _ = self.task_info[task_id]
        self.task_info.pop(task_id)
      
        return user_id
