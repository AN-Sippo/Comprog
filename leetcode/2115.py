from collections import deque, defaultdict as dd


class Solution:
    def findAllRecipes(
        self, recipes: list[str], ingredients: list[list[str]], supplies: list[str]
    ) -> list[str]:
        edges = dd(lambda: [])
        n = len(recipes)

        ins = {}
        for key in recipes:
            ins[key] = 0

        for i in range(n):
            recipe_name = recipes[i]
            ingredient = ingredients[i]
            ins[recipe_name] = len(ingredient)
            for ig in ingredient:
                edges[ig].append(recipe_name)

        queue = deque()
        for supply in supplies:
            queue.append(supply)
        ans = []
        while queue:
            cooking = queue.popleft()
            for edge in edges[cooking]:
                ins[edge] -= 1
                if ins[edge] == 0:
                    queue.append(edge)
                    ans.append(edge)

        return ans


Solution().findAllRecipes(["bread"], [["yeast", "flour"]], ["yeast", "flour", "corn"])
