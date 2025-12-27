class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        busy_rooms = []
        available_rooms = list(range(n))
        heapify(available_rooms)
        meeting_count = [0] * n
        for start_time, end_time in meetings:
            while busy_rooms and busy_rooms[0][0] <= start_time:
                freed_room = heappop(busy_rooms)[1]
                heappush(available_rooms, freed_room)
            if available_rooms:
                room_id = heappop(available_rooms)
                meeting_count[room_id] += 1
                heappush(busy_rooms, (end_time, room_id))
            else:
                earliest_end_time, room_id = heappop(busy_rooms)
                meeting_count[room_id] += 1
                new_end_time = earliest_end_time + (end_time - start_time)
                heappush(busy_rooms, (new_end_time, room_id))
        most_used_room = 0
        for room_id, count in enumerate(meeting_count):
            if meeting_count[most_used_room] < count:
                most_used_room = room_id
      
        return most_used_room