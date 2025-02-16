class Solution:
    def constructDistancedSequence(self, n: int) -> list[int]:
        seq = [0] * (2 * n - 1)
        len_seq = 2 * n - 1
        
        def backtrack(pos: int, used: int) -> bool:
            while pos < len_seq and seq[pos]: 
                pos += 1
            if pos == len_seq: 
                return True

            for num in range(n, 0, -1):
                if used & (1 << num): 
                    continue
                if num > 1:
                    if pos + num >= len_seq or seq[pos + num]: 
                        continue
                    seq[pos] = seq[pos + num] = num
                else:
                    seq[pos] = num
                if backtrack(pos + 1, used | (1 << num)): 
                    return True
                seq[pos] = 0
                if num > 1: 
                    seq[pos + num] = 0

            return False
            
        backtrack(0, 0)
        return seq