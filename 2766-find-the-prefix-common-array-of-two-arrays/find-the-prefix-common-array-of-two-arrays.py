class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        duplicate = set()
        count = 0
        C = []
        for i in range(len(A)):
            if A[i] in duplicate:
                count += 1
            else:
                duplicate.add(A[i])
            if B[i] in duplicate:
                count += 1
            else:
                duplicate.add(B[i])
            C.append(count)
        return C
            