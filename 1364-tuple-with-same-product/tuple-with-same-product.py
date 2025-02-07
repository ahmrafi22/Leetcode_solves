class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        n=len(nums)
        if n<4: return 0
        newdict=defaultdict(int)
        for i in range(n):
            for j in range (i+1,n):
                product=nums[i]*nums[j]
                newdict[product]+=1
        countt=0
        for count in newdict.values():
            if i>=2:
                countt+=(count * (count-1))//2 
        return countt*8