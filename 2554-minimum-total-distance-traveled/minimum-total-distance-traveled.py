class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        @cache
        def dp(robot_idx: int, factory_idx: int) -> int:
            if robot_idx == len(robot):
                return 0
            if factory_idx == len(factory):
                return float('inf')
            min_distance = dp(robot_idx, factory_idx + 1)
            cumulative_distance = 0
            factory_position = factory[factory_idx][0]
            factory_capacity = factory[factory_idx][1]
            for num_robots in range(factory_capacity):
                if robot_idx + num_robots >= len(robot):
                    break
                cumulative_distance += abs(robot[robot_idx + num_robots] - factory_position)
                min_distance = min(
                    min_distance,
                    cumulative_distance + dp(robot_idx + num_robots + 1, factory_idx + 1)
                )
          
            return min_distance
        robot.sort()
        factory.sort()
        result = dp(0, 0)
        dp.cache_clear()
      
        return result 