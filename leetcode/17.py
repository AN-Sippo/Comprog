class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if digits == "":
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
        ans = [""]
        for digit in digits:
            next = []
            for ai in ans:
                for letter in key_map[digit]:
                    next.append(ai + letter)
            ans = next

        return ans
