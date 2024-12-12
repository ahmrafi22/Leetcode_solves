class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        res = [-i for i in gifts]
        heapq.heapify(res)
        for i in range(k):
            temp = -heapq.heappop(res)
            temp = int(math.sqrt(temp))
            heapq.heappush(res, -temp)
        ans = [-i for i in res]
        return int(sum(ans)) 