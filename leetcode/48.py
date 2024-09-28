from collections import deque


class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        n = len(matrix)
        round = 0
        top = 0
        bottom = n - 1
        left = 0
        right = n - 1
        while top < bottom:
            queue = deque()
            jump = n - 2 * round - 1
            current_y = top
            current_x = left
            for _ in range(jump * 5):
                queue.append(matrix[current_y][current_x])
                if len(queue) >= jump + 1:
                    matrix[current_y][current_x] = queue.popleft()
                current_y, current_x = self.next(
                    current_y, current_x, top, bottom, left, right
                )
            top += 1
            bottom -= 1
            left += 1
            right -= 1
            round += 1

    def next(self, current_y, current_x, top, bottom, left, right):
        if current_y == top and current_x == right:
            current_y += 1
        elif current_y == top and current_x == left:
            current_x += 1
        elif current_y == bottom and current_x == right:
            current_x -= 1
        elif current_y == bottom and current_x == left:
            current_y -= 1
        elif current_y == top:
            current_x += 1
        elif current_x == right:
            current_y += 1
        elif current_y == bottom:
            current_x -= 1
        elif current_x == left:
            current_y -= 1
        else:
            raise Exception("unexpedted rotation")

        return (current_y, current_x)


Solution().rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
