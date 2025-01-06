class Solution:
    def minOperations(self, boxes: str) -> list[int]:
        n = len(boxes)
        res = [0] * n

        # Left-to-right pass
        lb, lc = 0, 0
        for i in range(n):
            res[i] += lc
            if boxes[i] == '1':
                lb += 1
            lc += lb

        # Right-to-left pass
        rb, rc = 0, 0
        for i in range(n - 1, -1, -1):
            res[i] += rc
            if boxes[i] == '1':
                rb += 1
            rc += rb

        return res
