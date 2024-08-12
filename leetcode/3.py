class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        dic = {s[0] : 0}
        ans = 1
        tmp = 1
        l = 0
        for r in range(1,len(s)):
            ok = False
            if not s[r] in dic :
                ok = True
            else:
                if dic[s[r]] < l:
                    ok = True
            if ok:
                tmp += 1
            else:
                tmp -= dic[s[r]] - l # l：1 -> 3 ,then tmp -= 2
                l = dic[s[r]] + 1
            dic[s[r]] = r 
            ans = max(tmp,ans)
        return ans

print(Solution().lengthOfLongestSubstring("aab"))






 