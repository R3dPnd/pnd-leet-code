class Solution:
    def trailingZeroes(self, n: int) -> int:
        zeros = 0
        five_power = 1
        curr = n
        while curr // pow(5,five_power) > 0:
            print(curr)
            zeros += curr // pow(5,five_power)
            curr = curr//5
            five_power =+ 1

        return zeros