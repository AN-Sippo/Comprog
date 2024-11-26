class Node:
    def __init__(self, name, children, alive=True):
        self.name = name
        self.alive = alive
        self.children = children

    def death(self):
        self.alive = False

    def append_child(self, child_node):
        self.children.append(child_node)


class ThroneInheritance:

    def __init__(self, kingName: str):
        root = Node(kingName, children=[])
        self.root = root
        self.name_to_node = {kingName: root}

    def birth(self, parentName: str, childName: str) -> None:
        child_node = Node(childName, children=[])
        self.name_to_node[parentName].append_child(child_node)
        self.name_to_node[childName] = child_node

    def death(self, name: str) -> None:
        self.name_to_node[name].death()

    def getInheritanceOrder(self) -> list[str]:

        def dfs(current_node: Node, visited, curOrder):
            name = current_node.name
            if name in visited:
                return
            if current_node.alive:
                curOrder.append(name)
            visited[name] = 1
            for child_node in current_node.children:
                dfs(child_node, visited, curOrder)

        curOrder = []
        visited = {}
        dfs(self.root, visited, curOrder)
        return curOrder


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()
