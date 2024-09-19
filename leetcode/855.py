from heapq import heappop, heapify, heappush


class SeatRange:
    def __init__(self, left, right, n):
        self.n = n
        self.valid = True
        self.left = left
        self.right = right
        self.next = self.calc_next(left, right)
        self.length = self.calc_length()

    def calc_next(self, left, right):
        if left == -1:
            return 0
        elif right == self.n:
            return self.n - 1
        else:
            return left + (right - left) // 2

    def calc_length(self):
        if self.left == -1:
            return abs(self.next - self.right)

        elif self.right == self.n:
            return abs(self.next - self.left)
        else:
            return min(abs(self.left - self.next), abs(self.right - self.next))

    def disable(self):
        self.valid = False

    def merge(self, other):
        self.disable()
        other.disable()
        return SeatRange(
            min(self.left, other.left), max(self.right, other.right), self.n
        )

    def seat(self):
        self.disable()
        return (
            self.next,
            SeatRange(self.left, self.next, self.n),
            SeatRange(self.next, self.right, self.n),
        )

    def __lt__(self, other):
        return (
            self.length > other.length
            or self.length == other.length
            and self.next < other.next
        )

    def __str__(self):
        return f"< left:{self.left} right:{self.right} length:{self.length} next:{self.next} >"

    def __repr__(self):
        return f"< left:{self.left} right:{self.right} length:{self.length} next:{self.next} valid:{self.valid}>\n"


class RangeSet:
    def __init__(self, l, r):
        self.l = l
        self.r = r


class ExamRoom:

    def __init__(self, n: int):
        self.heap = [SeatRange(-1, n, n)]
        self.n = n
        self.breakpoints = {}

    def seat(self) -> int:
        # print("====seat======")
        r = heappop(self.heap)
        while not r.valid:
            r = heappop(self.heap)
        seat, r1, r2 = r.seat()
        if r1.left in self.breakpoints:
            self.breakpoints[r1.left].r = r1
        if r2.right in self.breakpoints:
            self.breakpoints[r2.right].l = r2
        self.breakpoints[seat] = RangeSet(r1, r2)
        heappush(self.heap, r1)
        heappush(self.heap, r2)
        # print(self.heap)
        # print(f"{seat=}")
        return seat

    def leave(self, p: int) -> None:
        # print(f"====leave:{p}=====")
        r1 = self.breakpoints[p].l
        r2 = self.breakpoints[p].r
        self.breakpoints.pop(p)
        r = r1.merge(r2)
        if r1.left in self.breakpoints:
            self.breakpoints[r1.left].r = r
        if r2.right in self.breakpoints:
            self.breakpoints[r2.right].l = r
        heappush(self.heap, r)
        # print(self.heap)


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)
