class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        value_index_pairs = sorted(enumerate(nums), key=lambda x: x[1])
        
        groups = []
        current_group = [value_index_pairs[0]]
        
        for pair in value_index_pairs[1:]:
            if pair[1] - current_group[-1][1] <= limit:
                current_group.append(pair)
            else:
                groups.append(current_group)
                current_group = [pair]
        
        groups.append(current_group)
        
        result = nums.copy()
        for group in groups:
            sorted_indices = sorted(idx for idx, _ in group)
            sorted_values = sorted(val for _, val in group)
            
            for sorted_idx, sorted_val in zip(sorted_indices, sorted_values):
                result[sorted_idx] = sorted_val
        
        return result