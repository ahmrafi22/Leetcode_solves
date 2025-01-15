class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        ctn=0
        newNum=0
        for i in range(32):
            if num2 & 1<<i:
                ctn+=1
        # print(ctn)
        for i in range(32):
            if num1& 1<<(31-i):
                newNum= newNum | 1<<(31-i)
                # print(newNum)
                ctn-=1
            if(ctn==0):
                break

        for i in range(32):
            if(ctn==0):
                break 
            if num1& 1<<i ==0 :
                newNum= newNum | 1<<i
                # print(newNum)
                ctn-=1
                
             
        return newNum                  