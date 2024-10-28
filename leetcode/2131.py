from collections import defaultdict as dd


class Solution:
    def longestPalindrome(self, words: list[str]) -> int:
        freq_map = dd(int)
        ans = 0
        self_palind = 0
        for word in words:
            freq_map[word] += 1

        for key in freq_map:
            if key[1] == key[0]:
                if freq_map[key] == 1:
                    self_palind = 1
                else:
                    if freq_map[key] % 2 == 1:
                        self_palind = 1
                    ans += 4 * (freq_map[key] // 2)
                continue

            palind = key[1] + key[0]
            if palind in freq_map and freq_map[palind] > 0:
                matchs = min(freq_map[palind], freq_map[key])
                freq_map[key] -= matchs
                freq_map[palind] -= matchs
                ans += 4 * matchs
                continue

        if self_palind:
            ans += 2
        return ans
