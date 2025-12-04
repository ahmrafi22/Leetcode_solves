class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        result = []
        n = len(arr)
        
        for size in range(n, 1, -1):
            max_idx = arr.index(max(arr[:size]))
            
            if max_idx != size - 1:
                if max_idx != 0:
                    result.append(max_idx + 1)
                    arr[:max_idx + 1] = arr[:max_idx + 1][::-1]
                
                result.append(size)
                arr[:size] = arr[:size][::-1]
        
        return result