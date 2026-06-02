class Solution:
    def earliestFinishTime(
        self,
        landStartTime: List[int],
        landDuration: List[int],
        waterStartTime: List[int],
        waterDuration: List[int],) -> int:
        def calculate_finish_time(
            first_stage_start: List[int],
            first_stage_duration: List[int],
            second_stage_start: List[int],
            second_stage_duration: List[int]) -> int:
            min_first_stage_end = min(
                start + duration
                for start, duration in zip(first_stage_start, first_stage_duration)
            )
            min_total_time = min(
                max(start, min_first_stage_end) + duration
                for start, duration in zip(second_stage_start, second_stage_duration)
            )

            return min_total_time

        land_then_water = calculate_finish_time(
            landStartTime, landDuration,
            waterStartTime, waterDuration
        )
        water_then_land = calculate_finish_time(
            waterStartTime, waterDuration,
            landStartTime, landDuration
        )

        return min(land_then_water, water_then_land)