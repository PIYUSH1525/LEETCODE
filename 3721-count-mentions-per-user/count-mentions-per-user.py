from typing import List

class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        events.sort(key=lambda event: (int(event[1]), event[0][2]))
      
        mention_counts = [0] * numberOfUsers
      
        online_until = [0] * numberOfUsers
      
        all_mentions_count = 0
      
        for event_type, timestamp_str, data in events:
            current_time = int(timestamp_str)
          
            if event_type[0] == "O":  
                user_id = int(data)
                online_until[user_id] = current_time + 60
              
            elif data[0] == "A":  
                all_mentions_count += 1
              
            elif data[0] == "H": 
                for user_id, offline_time in enumerate(online_until):
                    if offline_time <= current_time:  
                        mention_counts[user_id] += 1
                      
            else:  
                for mention in data.split():
                    user_id = int(mention[2:])
                    mention_counts[user_id] += 1
        if all_mentions_count:
            for user_id in range(numberOfUsers):
                mention_counts[user_id] += all_mentions_count
              
        return mention_counts