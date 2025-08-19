class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split(" ")
        i = -1
        last_word = words[i]

        while abs(i) <= len(words):
            if last_word.strip():
                print(last_word)
                return len(last_word)
            i -= 1
            last_word = words[i]
        print(i)
        return 0