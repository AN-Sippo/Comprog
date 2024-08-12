class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        MAXINT  = pow(2,31) - 1
        rev = 0
        minus = 1
        if x < 0:
            minus = -1
        x = abs(x)
        while x:
            digit = x % 10
            if rev > MAXINT//10 or (rev == MAXINT // 10 and MAXINT % 10 < digit):
                return 0
            rev = 10 * rev + digit
            x -= digit
            x //= 10
        return  minus * rev

print(Solution().reverse(120))