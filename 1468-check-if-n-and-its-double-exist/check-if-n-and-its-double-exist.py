class Solution(object):
    def checkIfExist(self, arr):
        seen = set()

        for num in arr:
            if num << 1 in seen:
                return True

            if not num & 1 and num >> 1 in seen:
                return True

            seen.add(num)

        return False