class Solution:
    def findScore(self, nums: List[int]) -> int:
        n = len(nums)
        nums = [float('inf')] + nums + [float('inf')] 
        q = [] 
        score = 0
        for i in range(1, n+1):
            if nums[i] == float('inf'):
                continue
            smallest = (nums[i] < nums[i-1]) and (nums[i] <= nums[i+1])
            
            if smallest:
                while q:
                    q.pop()
                    if q:
                        score += nums[q.pop()]
                score += nums[i]
                nums[max(i-1, 1)] = nums[min(i+1, n)] = float('inf') 
            else:
                q.append(i)
        return score