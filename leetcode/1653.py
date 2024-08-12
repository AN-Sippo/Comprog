class Solution(object):
    def minimumDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        totalA = 0
        for si in s:
            if si == "a":
                totalA += 1

        l = [[0,0] for _ in range(len(s) + 1)]
        l[0] = [totalA,0]
        for i in range(len(s)):
            si = s[i]
            if si == "a":
                l[i + 1][0] = l[i][0] - 1
                l[i + 1][1] = l[i][1]
            if si == "b":
                l[i + 1][0] = l[i][0]
                l[i + 1][1] = l[i][1] + 1

        ans = 10**10
        for pair in l:
            ans = min(ans,sum(pair))
        return ans

print(Solution().minimumDeletions("aababbab"))