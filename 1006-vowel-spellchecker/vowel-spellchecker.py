class Solution:
    def __init__(self):
        self.exact_words = set()  
        self.case_map = {}      
        self.vowel_map = {}       

    def to_lower(self, s):
        return s.lower()

    def mask_vowels(self, s):
        return ''.join('*' if self.is_vowel(c) else c for c in s)

    def is_vowel(self, c):
        return c in 'aeiou'

    def check_for_match(self, query):
        if query in self.exact_words:
            return query
        lower_query = self.to_lower(query)
        if lower_query in self.case_map:
            return self.case_map[lower_query]

        masked_query = self.mask_vowels(lower_query)
        if masked_query in self.vowel_map:
            return self.vowel_map[masked_query]

        return ""

    def spellchecker(self, wordlist, queries):
        self.exact_words.clear()
        self.case_map.clear()
        self.vowel_map.clear()

        for word in wordlist:
            self.exact_words.add(word)

            lower_word = self.to_lower(word)
            self.case_map.setdefault(lower_word, word) 

            masked_word = self.mask_vowels(lower_word)
            self.vowel_map.setdefault(masked_word, word) 

        result = [self.check_for_match(query) for query in queries]
        return result