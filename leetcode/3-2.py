class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ss = set()
        l = r = 0
        ans = 0
        tmp = 0
        for r in range(len(s)):
            tmp += 1
            while s[r] in ss:
                ss.remove(s[l])
                l += 1
                tmp -= 1
            ss.add(s[r])
            ans = max(ans,tmp)

        return ans

print(Solution().lengthOfLongestSubstring("abcabcbb"))