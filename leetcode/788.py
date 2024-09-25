class Solution:
    def rotatedDigits(self, n: int) -> int:
        self.valid_different = set(["2", "5", "6", "9"])
        self.valid_same = set(["0", "1", "8"])
        length = len(str(n))
        ans = 0
        for digit in range(1, length):
            ans += self.count0182569(digit) - self.count018(digit)

        for i in range(10 ** (length - 1), n + 1):
            ans += self.valid(i)

        return ans

    def valid(self, n: int):
        n = str(n)
        flag = False
        for ni in n:
            if ni in self.valid_different:
                flag = True
                continue
            elif ni in self.valid_same:
                continue
            else:
                break
        else:
            return flag
        return False

    def count0182569(self, digits):
        ans = 6
        for _ in range(1, digits):
            ans *= 7
        return ans

    def count018(self, digits):
        ans = 2
        for _ in range(1, digits):
            ans *= 3
        return ans


print(Solution().rotatedDigits(6))
