class Solution(object):
    def minHeightShelves(self, books, shelfWidth):
        """
        :type books: List[List[int]]
        :type shelfWidth: int
        :rtype: int
        """
        INF = 10**10
        # dp[i][j] = h : i冊の本を並べて一番上の本棚にはj冊の本があるとき、本棚全体の高さはhである。
        dp = [[INF for _ in range(len(books)+1)] for _ in range(len(books)+1)]

        dp[0][0] = 0
        for i in range(1,len(books) + 1):
            restedWidth = shelfWidth
            currentHeight = 0
            for j in range(1,i + 1): # j <= i - 1. 一番上に０冊はありえない。
                # 本棚を追加するケース
                if j == 1: 
                    dp[i][j] = min(dp[i - 1]) + books[i - 1][1]
                    continue


                # 既存の本棚に刺す
                if dp[i - 1][j - 1] == INF:
                    continue
                restedWidth -= books[i - 1 - j + 1][0] 
                currentHeight = max(currentHeight,books[i - 1 - j + 1][1])
                if restedWidth >= books[i - 1][0]:
                    diff = max(0,books[i - 1][1] -currentHeight)
                    dp[i][j] = dp[i - 1][j - 1] + diff

        return min(dp[len(books)])

print(Solution().minHeightShelves([[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]],4))




