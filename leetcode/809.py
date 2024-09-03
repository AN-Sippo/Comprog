from itertools import groupby


class Solution:
    def expressiveWords(self, s: str, words: list[str]) -> int:
        ans = 0
        sg = [(k, len(list(v))) for k, v in groupby(s)]
        for word in words:
            wg = [(k, len(list(v))) for k, v in groupby(word)]
            if len(sg) != len(wg):
                continue
            for sgi, wgi in zip(sg, wg):
                if sgi[0] != wgi[0] or not (
                    sgi[1] == wgi[1] or (sgi[1] >= 3 and sgi[1] > wgi[1])
                ):
                    break
            else:
                ans += 1

        return ans
