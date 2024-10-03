class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.max_size = maxSize
        self.diff = [0 for _ in range(maxSize)]

    def push(self, x: int) -> None:
        if len(self.stack) == self.max_size:
            return
        self.stack.append(x)

    def pop(self) -> int:
        if not self.stack:
            return -1
        k = len(self.stack) - 1
        diff = self.diff[k]
        self.diff[k] = 0
        if k != 0:
            self.diff[k - 1] += diff
        return self.stack.pop() + diff

    def increment(self, k: int, val: int) -> None:
        if not self.stack:
            return
        k = min(k, len(self.stack))
        self.diff[k - 1] += val
