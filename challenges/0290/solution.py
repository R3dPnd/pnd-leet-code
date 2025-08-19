class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word_pattern_hashMap = {}
        pattern_word_hashMap = {}

        words = s.split(" ")

        if len(words) != len(pattern):
            return False

        for i in range(len(pattern)):
            word = words[i]
            if word in word_pattern_hashMap.keys() and word_pattern_hashMap[word] != pattern[i]:
                return False
            if pattern[i] in pattern_word_hashMap.keys() and pattern_word_hashMap[pattern[i]] != word:
                return False
            word_pattern_hashMap[word] = pattern[i]
            pattern_word_hashMap[pattern[i]] = word
        return True