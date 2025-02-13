import heapq
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapify(nums)
        num=heappop(nums)
        count=0
        while(num<k):
            i=num*2+heappop(nums)
            num=heappushpop(nums,i)
            count+=1
        return count