class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = ''
        for i in digits:
            res += str(i) 
        instres = int(res)
        instres += 1

        res2 = []
        for i in str(instres):
            res2.append(int(i)) 
        
        return res2