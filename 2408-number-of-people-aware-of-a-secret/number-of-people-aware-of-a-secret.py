class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        buffer_size = (n << 1) + 10
        people_knowing_secret = [0] * buffer_size
        new_people_each_day = [0] * buffer_size
        new_people_each_day[1] = 1
        for day in range(1, n + 1):
            if new_people_each_day[day] > 0:
                people_knowing_secret[day] += new_people_each_day[day]
                people_knowing_secret[day + forget] -= new_people_each_day[day]
                start_sharing_day = day + delay
                stop_sharing_day = day + forget
                for sharing_day in range(start_sharing_day, stop_sharing_day):
                    new_people_each_day[sharing_day] += new_people_each_day[day]
        MOD = 10**9 + 7
        total_people_knowing = sum(people_knowing_secret[:n + 1])
      
        return total_people_knowing % MOD