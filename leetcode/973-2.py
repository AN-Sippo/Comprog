class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        n = len(points)

        left = 0
        right = n - 1
        pivot_index = 0
        while pivot_index != k:
            pivot_index = self.partition(left, right, points)
            if pivot_index > k:
                right = pivot_index - 1
            else:
                left = pivot_index

        return points[:pivot_index]

    def choose_pivot(self, a, b):
        return a + (b - a) // 2

    def partition(self, left, right, points: list[list[int]]):
        pivot_index = self.choose_pivot(left, right)
        pivot_distance = self.calc_distance(points[pivot_index])
        while right > left:
            if self.calc_distance(points[left]) >= pivot_distance:
                points[left], points[right] = points[right], points[left]
                right -= 1
            else:
                left += 1

        if self.calc_distance(points[left]) <= pivot_distance:
            left += 1

        return left

    def calc_distance(self, point: list[int]):
        x, y = point
        return x**2 + y**2
