from collections import defaultdict as dd


class TimeMap:

    def __init__(self):
        self.dic = {}
        self.key_to_timestamps = dd(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key_to_timestamps[key].append(timestamp)

        if key in self.dic:
            self.dic[key][timestamp] = value
        else:
            self.dic[key] = {timestamp: value}

    def binary_search(self, now, arr):
        if not arr or (now < arr[0]):
            return -1

        # def solve(mid):
        #     return arr[mid] <= now

        ok = 0
        ng = len(arr)
        while abs(ng - ok) > 1:
            mid = (ok + ng) // 2
            if arr[mid] <= now:
                ok = mid
            else:
                ng = mid
        return arr[ok]

    def get(self, key: str, timestamp: int) -> str:
        res_timestamp = self.binary_search(timestamp, self.key_to_timestamps[key])
        if res_timestamp == -1:
            return ""

        return self.dic[key][res_timestamp]
