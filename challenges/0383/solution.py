class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letter_pile = {}

        for i in range(len(magazine)):
            letter = magazine[i]
            if letter not in letter_pile.keys():
                letter_pile[letter] = 0

            letter_pile[letter] += 1
        for i in range(len(ransomNote)):
            letter = ransomNote[i]
            print(letter_pile)
            print
            if not letter in letter_pile.keys() or letter_pile[letter] == 0:
                return False
            letter_pile[letter] -= 1
        return True     