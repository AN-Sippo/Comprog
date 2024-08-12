class Solution(object):
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """
        tmp = 0
        s = set()
        for idx ,value in enumerate(arr):
            if value in s:
                continue
            s.add(value)
            if value in arr[idx+1:]:
                continue
            tmp += 1
            if tmp == k:
                return value 
        
        return ""