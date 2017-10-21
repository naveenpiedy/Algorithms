from collections import deque
class Graph:
    def __init__(self, Nodes = dict()):
        self.Nodes = Nodes

    def add_node(self, name, neighbours = None):
        if neighbours is None:
            neighbours = []
        self.Nodes[name] = neighbours

    def add_neighbours(self, name, neighbour):
        #print(name, self.Nodes[name], self.Nodes)
        temp = self.Nodes[name]
        #print(temp)
        temp.extend(neighbour)
        self.Nodes[name] = temp
        #print(name, self.Nodes[name], self.Nodes)

    def breadth_first_search(self, start_node):
        queue = deque()
        #print(start_node)
        visted = []
        queue.append(start_node)
        while queue:
            node_to_be_checked = queue.popleft()
            if node_to_be_checked not in visted:
                visted.append(node_to_be_checked)
                queue.extend([i for i in self.Nodes[visted[-1]] if i not in visted])
        return visted

    def depth_first_search(self, start_node):
        stack =[start_node]
        visited =[]
        while stack:
            node_to_be_checked = stack.pop()
            if node_to_be_checked not in visited:
                visited.append(node_to_be_checked)
                stack.extend([i for i in self.Nodes[visited[-1]] if i not in visited])
        return visited



# def main():
#     G = Graph()
#     G.add_node('A')
#     G.add_node('B')
#     G.add_node('C')
#     G.add_node('D')
#     G.add_node('E')
#     G.add_node('F')
#     G.add_neighbours('A', ['B','C'])
#     G.add_neighbours('B', ['D','E'])
#     G.add_neighbours('C', ['F'])
#     G.add_neighbours('E', ['F'])
#     print(G.Nodes)
#     x = G.breadth_first_search('A')
#     print(x)
#     y = G.depth_first_search('A')
#     print(y)
#
# if __name__ == '__main__':
#     main()
