class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if len(digits) == 0:
            return []
        key_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        n = len(digits)

        def backtrack(idx, path: list[str]):
            if idx == n:
                ans.append("".join(path))
                return
            for letter in key_map[digits[idx]]:
                path.append(letter)
                backtrack(idx + 1, path)
                path.pop()

        ans = []
        backtrack(0, [])
        return ans
