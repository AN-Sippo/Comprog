class Solution:
    def minimumSubarrayLength(self, nums: list[int], k: int) -> int:
        n = len(nums)
        bits = [0] * 32

        l = 0
        r = 0

        def bits_add(num):
            for i in range(len(bits)):
                if num >> i & 1:
                    bits[i] += 1

        def bits_sub(num):
            for i in range(len(bits)):
                if num >> i & 1:
                    bits[i] -= 1

        def bits_sum():
            res = 0
            for i, v in enumerate(bits):
                if v > 0:
                    res |= 1 << i
            return res

        ans = 10**5 + 1
        while r < n:
            r_num = nums[r]
            bits_add(r_num)
            while l < r and bits_sum() >= k:
                ans = min(ans, r - l + 1)
                bits_sub(nums[l])
                l += 1
            if bits_sum() >= k:
                ans = min(ans, r - l + 1)
            r += 1
        if ans == 10**5 + 1:
            return -1
        return ans
