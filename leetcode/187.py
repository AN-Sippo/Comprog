from collections import defaultdict as dd


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        freq_map = dd(int)
        ans = []
        for i in range(len(s) - 9):
            si = s[i : i + 10]
            freq_map[si] += 1
            if freq_map[si] == 2:
                ans.append(si)

        return ans
