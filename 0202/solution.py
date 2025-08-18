class Solution:
    def isHappy(self, n: int) -> bool:
        track = []
        curr = n
        while curr not in track:
            track.append(curr)
            curr = self.digit_square_sum(curr)
            if curr == 1:
                return True
            print(f"{track}:{curr}")
        return False
        
    def digit_square_sum(self, n:int):
        digits = []
        curr = n
        while curr > 0:
            digit = curr % 10
            digits.append(digit)
            curr = curr//10

        sum = 0
        for i in range(len(digits)):
            digit = digits[len(digits)-i-1]
            sum+= pow(digit, 2)
        return sum