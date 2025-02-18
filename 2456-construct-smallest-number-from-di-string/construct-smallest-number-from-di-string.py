class Solution:
    def smallestNumber(self, pattern: str) -> str:
        st = ['1']
        n = 1
        res = ''
        for char in pattern:
            if char == 'I':
                while st:
                    res += st.pop()
            
            n += 1
            st.append(str(n))

        return res + ''.join(st[::-1])