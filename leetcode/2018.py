class Solution:
    def placeWordInCrossword(self, board: list[list[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        wl = len(word)
        rows = board
        columns = [[] for _ in range(n)]
        for row in rows:
            for i in range(n):
                columns[i].append(row[i])
        for lines in [rows, columns]:
            for line in lines:
                a = "".join(line).split("#")
                b = "".join(reversed(line)).split("#")
                for c in (a, b):
                    for ci in c:
                        ok = True
                        if len(ci) != wl:
                            continue
                        for i in range(wl):
                            if word[i] != ci[i] and ci[i] != " ":
                                ok = False
                                break
                        if ok:
                            return True

        return False
