class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        tot,store = set(arr),{}
        q,res = deque(),0
        for num in arr:
            store[num] = defaultdict(int)
            while q and q[0]<=num//2:
                del store[q.popleft()]
            for i in q:
                if num-i in tot:
                    store[num][i] = store[i][num-i] + 1
                    if store[num][i]+2>res:
                        res = store[num][i]+2
            q.append(num)
        return res