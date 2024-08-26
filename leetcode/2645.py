class Solution:
    def addMinimum(self, word: str) -> int:
        N = len(word)
        word += "xx"
        ans = 0
        i = 0
        while i < N:
            print(word[i])
            if word[i] == "a":
                if word[i + 1] == "b" and word[i + 2] == "c":
                    i += 3
                elif word[i + 1] == "b" or word[i + 1] == "c":
                    ans += 1
                    i += 2
                else:
                    ans += 2
                    i += 1
            elif word[i] == "b":
                if word[i + 1] == "c":
                    ans += 1
                    i += 2
                else:
                    ans += 2
                    i += 1
            elif word[i] == "c":
                ans += 2
                i += 1

        return ans


print(Solution().addMinimum("aaa"))
