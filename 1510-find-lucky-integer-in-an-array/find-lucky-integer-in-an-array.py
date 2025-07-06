class Solution:
    def findLucky(self, arr: List[int]) -> int:
        arr.sort(reverse=True)
        i = 0
        while i < len(arr):
            count = arr.count(arr[i])
            if arr[i] == count:
                return arr[i]
            i += count
        return -1