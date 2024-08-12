class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        str_x= str(x)
        is_minutes = False
        if str_x[0]  == "-":
            is_minutes = True 
            str_x = str_x[1:]
        ans = "".join(reversed(str_x))
        if self.overFlow(ans):
            return 0
        if is_minutes:
            ans = "-" + ans 
        return int(ans)
    
    def overFlow(self,x):
        MAX_INTEGER = str(2**31)
        if (len(x) < len(MAX_INTEGER)):
            return False
        for i,j in zip(x,MAX_INTEGER):
            if (j > i):
                return False 
            if (i > j):
                return True 
        return False 


print(Solution().reverse(-123))

        
        