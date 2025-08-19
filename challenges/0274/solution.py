from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        list.sort(citations)
        i = 0
        while i<len(citations) and citations[len(citations)-1-i]>i:
            i+=1
        return i