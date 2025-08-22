class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits)-1
        digits[i]+=1
        while digits[i] > 9:
            digits[i] = 0
            print(i)
            if i >= 1:
                digits[i-1] +=1
                i-=1
            else:
                digits.insert(0, 1)
        return digits