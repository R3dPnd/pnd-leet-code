class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0

        for i in range(len(s)):
            chars = set()
            for j in range(i, len(s)):
                if s[j] in chars:
                    break
                else:
                    length = j-i+1
                    max_len = max(length, max_len)
                    chars.add(s[j])
                    
        return max_len