class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hash = {}

        for i in range(len(s)):
            curr = s[i]
            if curr not in s_hash.keys():
                s_hash[curr] = []
            s_hash[curr].append(curr)

        for i in range(len(t)):
            curr = t[i]
            if curr not in s_hash.keys():
                return False
            if len(s_hash[curr]) == 1:
                s_hash.pop(curr)
            else:
                s_hash[curr].pop()
        return len(s_hash.values()) == 0