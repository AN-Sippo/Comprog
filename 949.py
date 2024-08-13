from itertools import permutations


class Solution:
    def largestTimeFromDigits(self, arr):
        def isValid(arr):
            hour = arr[0] * 10 + arr[1]
            minutes = arr[2] * 10 + arr[3]
            return 0 <= hour <= 23 and 0 <= minutes <= 59

        def timeKey(arr):
            return arr[0] * 1000 + arr[1] * 100 + arr[2] * 10 + arr[3]

        validTimes = []
        for l in permutations(arr, 4):
            if not isValid(l):
                continue
            validTimes.append(l)

        if len(validTimes) == 0:
            return ""

        validTimes.sort(key=timeKey)

        return f"{validTimes[-1][0]}{validTimes[-1][1]}:{validTimes[-1][2]}{validTimes[-1][3]}"
