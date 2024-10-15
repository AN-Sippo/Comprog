class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        bought = -(10**5)
        sold = -(10**5)
        rest = 0
        for price in prices:
            pre_sold = sold
            sold = bought + price
            bought = max(bought, rest - price)
            rest = max(rest, pre_sold)

        return max(rest, sold)
