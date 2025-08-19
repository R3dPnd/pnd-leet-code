class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")

        res = ""

        for i in range(len(words)):
            word = words[len(words) - i -1]
            if word and not word.isspace():
                print(word)
                res += word.replace(" ", "") + " "

        return res.strip(" ")