class Solution:
    def minimumDistance(self, word: str) -> int:
      
        def calculate_distance(char1: int, char2: int) -> int:
           
            row1, col1 = divmod(char1, 6)
            row2, col2 = divmod(char2, 6)
            return abs(row1 - row2) + abs(col1 - col2)
      
        word_length = len(word)
        dp = [[[float('inf')] * 26 for _ in range(26)] for _ in range(word_length)]
        first_char_index = ord(word[0]) - ord('A')
        for finger_pos in range(26):
            dp[0][first_char_index][finger_pos] = 0  
            dp[0][finger_pos][first_char_index] = 0  
        for i in range(1, word_length):
            prev_char_index = ord(word[i - 1]) - ord('A')
            curr_char_index = ord(word[i]) - ord('A')
            distance_between_chars = calculate_distance(prev_char_index, curr_char_index)
          
            for other_finger in range(26):
                dp[i][curr_char_index][other_finger] = min(
                    dp[i][curr_char_index][other_finger],
                    dp[i - 1][prev_char_index][other_finger] + distance_between_chars
                )
                dp[i][other_finger][curr_char_index] = min(
                    dp[i][other_finger][curr_char_index],
                    dp[i - 1][other_finger][prev_char_index] + distance_between_chars
                )
                if other_finger == prev_char_index:
                    for previous_position in range(26):
                        distance_to_current = calculate_distance(previous_position, curr_char_index)
                        dp[i][curr_char_index][other_finger] = min(
                            dp[i][curr_char_index][other_finger],
                            dp[i - 1][previous_position][prev_char_index] + distance_to_current
                        )
                        dp[i][other_finger][curr_char_index] = min(
                            dp[i][other_finger][curr_char_index],
                            dp[i - 1][prev_char_index][previous_position] + distance_to_current
                        )
        last_char_index = ord(word[-1]) - ord('A')
        min_left_finger = min(dp[word_length - 1][last_char_index])
        min_right_finger = min(dp[word_length - 1][j][last_char_index] for j in range(26))
      
        return int(min(min_left_finger, min_right_finger))