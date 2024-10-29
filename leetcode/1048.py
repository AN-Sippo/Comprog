class Solution:
    def longestStrChain(self, words: list[str]) -> int:
        words.sort(key=lambda x: len(x))

        def get(word, idx):
            if len(word) > idx:
                return word[idx]
            else:
                return ""

        n = len(words)
        edges = [[] for _ in range(n)]
        for start in range(n):
            for end in range(start, n):
                start_word = words[start]
                end_word = words[end]
                if len(start_word) == len(end_word):
                    continue
                elif len(start_word) + 1 < len(end_word):
                    break
                inserted = False
                start_idx = 0
                end_idx = 0
                while end_idx < len(end_word):
                    if get(start_word, start_idx) == end_word[end_idx]:
                        start_idx += 1
                        end_idx += 1
                        continue
                    else:
                        if inserted:
                            break
                        inserted = True
                        end_idx += 1
                else:
                    edges[start].append(end)

        memo = [10000 for _ in range(n)]

        def dfs(idx):
            if memo[idx] != 10000:
                return memo[idx]
            _max = 1
            for next in edges[idx]:
                _max = max(dfs(next) + 1, _max)
            memo[idx] = _max
            return _max

        ans = 0
        for i in range(n):
            ans = max(ans, dfs(i))
        return ans
