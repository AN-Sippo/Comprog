from collections import defaultdict as dd


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        if len(s) <= 10:
            return []

        dic = {"A": 0, "T": 1, "C": 2, "G": 3}
        s_list = list(map(lambda x: dic[x], s))
        freq_map = dd(int)
        ans_end_idx = []

        hash = 0
        for i in range(10):
            hash += s_list[i] * pow(4, 10 - i)
        freq_map[hash] += 1

        for next_idx in range(10, len(s_list)):
            hash -= s_list[next_idx - 10] * pow(4, 10)
            hash += s_list[next_idx]
            hash *= 4
            freq_map[hash] += 1
            if freq_map[hash] == 2:
                ans_end_idx.append(next_idx)

        ans = []
        for end_idx in ans_end_idx:
            ans.append(s[end_idx - 9 : end_idx + 1])
        return ans


Solution().findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")
