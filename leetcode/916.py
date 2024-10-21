from collections import defaultdict as dd


class Solution:
    def wordSubsets(self, words1: list[str], words2: list[str]) -> list[str]:
        word2_union_freq_map = {}
        for word in words2:
            for key, value in self.count(word).items():
                if key in word2_union_freq_map:
                    word2_union_freq_map[key] = max(word2_union_freq_map[key], value)
                else:
                    word2_union_freq_map[key] = value
        ans = []
        for word in words1:
            freq_map = dd(int, self.count(word))
            for key in word2_union_freq_map:
                if freq_map[key] < word2_union_freq_map[key]:
                    break
            else:
                ans.append(word)

        return ans

    def count(sellf, word: str):
        freq_map = {}
        for wi in word:
            if wi in freq_map:
                freq_map[wi] += 1
            else:
                freq_map[wi] = 1
        return freq_map
