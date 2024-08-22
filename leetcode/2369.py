class Solution:
    def isValid(self, l) -> bool:
        if len(l) == 3:
            if l[0] == l[1] == l[2]:
                return True
            if l[0] + 2 == l[1] + 1 == l[2]:
                return True
        if len(l) == 2 and l[0] == l[1]:
            return True
        return False

    def validPartition(self, nums: list[int]) -> bool:
        N = len(nums)
        l = [(nums[0],)]
        for n in nums[1:]:
            if len(l) == 0:
                return False
            nl = set()
            for li in l:
                if len(li) == 3:
                    nl.add((n,))
                elif len(li) == 2:
                    if li[0] == li[1] == n or li[0] + 2 == li[1] + 1 == n:
                        nl.add((li[0], li[1], n))
                    if li[0] == li[1]:
                        nl.add((n,))
                elif len(li) == 1:
                    if li[0] == n or li[0] + 1 == n:
                        nl.add((li[0], n))
            l = nl

        for li in l:
            if self.isValid(li):
                return True
        return False
