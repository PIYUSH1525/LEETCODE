class Solution:
    def minimumTeachings(
        self, n: int, languages: List[List[int]], friendships: List[List[int]]
    ) -> int:
        def can_communicate(user1: int, user2: int) -> bool:
            user1 = languages[user1 - 1]
            user2 = languages[user2 - 1]
            for lang1 in user1:
                for lang2 in user2:
                    if lang1 == lang2:
                        return True
            return False
        users_needing = set()
        for user1, user2 in friendships:
            if not can_communicate(user1, user2):
                users_needing.add(user1)
                users_needing.add(user2)
        language_count = Counter()
        for user in users_needing:
            for language_id in languages[user - 1]:
                language_count[language_id] += 1
        if language_count:
            return len(users_needing) - max(language_count.values())
        else:
            return 0