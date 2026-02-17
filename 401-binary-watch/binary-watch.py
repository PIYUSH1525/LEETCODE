class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        result = []
        for hour in range(12):
            for minute in range(60):
                hour_bits = bin(hour).count('1')
                minute_bits = bin(minute).count('1')
                if hour_bits + minute_bits == turnedOn:
                    time_string = f"{hour}:{minute:02d}"
                    result.append(time_string)
      
        return result