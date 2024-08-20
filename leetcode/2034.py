import heapq
from collections import defaultdict


class StockPrice:

    def __init__(self):
        self.dic = {}
        self.priceCnt = defaultdict(int)
        self.heapMin = []
        self.heapMax = []
        self.currentPrice = (0, 0)
        heapq.heapify(self.heapMin)
        heapq.heapify(self.heapMax)

    def update(self, timestamp: int, price: int) -> None:
        if timestamp in self.dic:
            self.priceCnt[self.dic[timestamp]] -= 1
        self.dic[timestamp] = price
        self.priceCnt[price] += 1
        if self.currentPrice[0] <= timestamp:
            self.currentPrice = (timestamp, price)
        heapq.heappush(self.heapMin, price)
        heapq.heappush(self.heapMax, -price)

    def current(self) -> int:
        return self.currentPrice[1]

    def maximum(self) -> int:
        res = -heapq.heappop(self.heapMax)
        while self.priceCnt[res] == 0:
            res = -heapq.heappop(self.heapMax)
        heapq.heappush(self.heapMax, -res)
        return res

    def minimum(self) -> int:
        res = heapq.heappop(self.heapMin)
        while self.priceCnt[res] == 0:
            res = heapq.heappop(self.heapMin)
        heapq.heappush(self.heapMin, res)
        return res
