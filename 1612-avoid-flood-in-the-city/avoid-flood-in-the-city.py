from typing import List
from sortedcontainers import SortedList

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        result = [-1] * n
        sunny_days = SortedList()
        last_rain_day = {}
      
        for day, lake in enumerate(rains):
            if lake > 0:  
                if lake in last_rain_day:
                    sunny_day_idx = sunny_days.bisect_right(last_rain_day[lake])
                    if sunny_day_idx == len(sunny_days):
                        return []
                    dry_day = sunny_days[sunny_day_idx]
                    result[dry_day] = lake
            
                    sunny_days.discard(dry_day)
              
                last_rain_day[lake] = day
            else: 
                sunny_days.add(day)
                result[day] = 1
      
        return result
