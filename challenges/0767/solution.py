class Solution:
    def reorganizeString(self, s: str) -> str:
        pq = []

        for char, count in Counter(s).items():
            heappush(pq, (-count, char))

        res = ""
        while len(pq) > 1:
            count1, char1 = heappop(pq)
            count2, char2 = heappop(pq)

            res += char1 + char2

            if count1 + 1:
                heappush(pq, (count1 + 1, char1))
                