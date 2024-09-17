class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        ans = 10
        for i in range(2, n + 1):
            tmp = 9

            for j in range(1, i):
                tmp *= 10 - j
            ans += tmp

        return ans
