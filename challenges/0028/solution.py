class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        window = len(needle)
        pile = len(haystack)

        if pile < window:
            return -1
        
        for i in range(pile-window+1):
            hand_full = haystack[i: i+window]
            print(hand_full)
            if hand_full == needle:
                return i
        return -1