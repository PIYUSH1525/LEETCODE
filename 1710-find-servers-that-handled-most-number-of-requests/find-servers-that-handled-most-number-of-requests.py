import heapq

class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:

        available_servers = list(range(k))
        busy_servers = []
        cnt = [0] * k

        for i in range(len(arrival)):
            start, duration = arrival[i], load[i]
            while busy_servers and busy_servers[0][0] <= start:
                _, server = heapq.heappop(busy_servers)
                heapq.heappush(available_servers, i + (server - i) % k)
            if available_servers:
                server = heapq.heappop(available_servers) % k
                cnt[server] += 1
                heapq.heappush(busy_servers, (start + duration, server))

        mx = max(cnt)
        return [i for i in range(len(cnt)) if cnt[i] == mx]
        
        


