class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        arr = [0] * (n-1) + [k-1]
        for i in reversed(range(1, n)):
            arr[i-1] += arr[i] // 2
            arr[i] %= 2
        if arr[0] >= 3:
            return ""
        s = "abc"[arr[0]]
        for i in range(1, n):
            choices = "abc".replace(s[-1], "")
            s += choices[arr[i]]
        return s