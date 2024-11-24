class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        n = len(graph)
        colors = [-1 for _ in range(n)]

        def toggle(color):
            if color == 1:
                return 0
            else:
                return 1

        def dfs(node_idx, before_color):
            current_color = toggle(before_color)
            if colors[node_idx] != -1:
                if colors[node_idx] == current_color:
                    return 0
                else:
                    return -1
            else:
                colors[node_idx] = current_color
                for next_node in graph[node_idx]:
                    res = dfs(next_node, current_color)
                    if res == -1:
                        return -1
                return 0

        for i in range(n):
            if colors[i] == -1:
                if dfs(i, 0) == -1:
                    return False

        return True
