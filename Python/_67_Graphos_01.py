from __future__ import annotations
from typing import List, Set
from collections import deque

class DirectNode:
    
    def __init__(self, info):
        self.Info = info
        self.Adjacents = list()

    def addAdjacent(self, adjacent: DirectNode) -> None:
        self.Adjacents.append(adjacent)

    def transverseDSF_Recursion(self) -> List[DirectNode]:
        path = list()
        self.__transverseDSF_Recursion(self, path, set())
        return path

    def __transverseDSF_Recursion(self, node: DirectNode, path: List[DirectNode], visited: Set[DirectNode]) -> None:
        if node is None or node in visited:
            return
        path.append(node)
        visited.add(node)
        for adjacent in node.Adjacents:
            self.__transverseDSF_Recursion(adjacent, path, visited)

    def transverseDPS_NoRecursion(self) -> List[DirectNode]:
        stack = deque()
        stack.append(self)
        visited = set()
        path = list()
        while len(stack) > 0:
            current = stack.pop()
            if current not in visited:
                path.append(current)
                visited.add(current)
                for adj in current.Adjacents:
                    stack.append(adj)
        return path

    def transverseBFS (self) -> List[DirectNode]:
        queue = deque()
        queue.appendleft(self)
        path = list()
        visited = set()
        while len(queue) > 0:
            current = queue.pop()
            if current not in visited:
                path.append(current)
                visited.add(current)
                for adj in current.Adjacents:
                    queue.appendleft(adj)
        return path

    def hasCycle(self) -> bool:
        stack = deque()
        stack.append(self)
        visited = set()
        visiting = set()
        self.__hasCycle = False
        self.__hasCycleDFS(self, visited, visiting)
        return self.__hasCycle


    def __hasCycleDFS(self, node: DirectNode, visited: Set[DirectNode], visiting: Set[DirectNode]) -> None:
        if node in visiting:
            self.__hasCycle = True
        if node in visited:
            return
        visited.add(node)
        visiting.add(node)
        for adj in node.Adjacents:
            self.__hasCycleDFS(adj, visited, visiting)
        visiting.remove(node)

    def __repr__(self) -> str:
        adjacents = list()
        for adj in self.Adjacents:
            adjacents.append(adj.Info)
        return f'Info: {self.Info}; Adjacents:{adjacents}'

graph = dict()


graph['a'] = DirectNode('a')
graph['b'] = DirectNode('b')
graph['c'] = DirectNode('c')
graph['d'] = DirectNode('d')
graph['e'] = DirectNode('e')
graph['f'] = DirectNode('f')
graph['g'] = DirectNode('g')
graph['h'] = DirectNode('h')

graph['a'].addAdjacent(graph['b'])
graph['a'].addAdjacent(graph['c'])
graph['b'].addAdjacent(graph['g'])
graph['c'].addAdjacent(graph['d'])
graph['c'].addAdjacent(graph['g'])
graph['d'].addAdjacent(graph['e'])
graph['e'].addAdjacent(graph['f'])
graph['f'].addAdjacent(graph['g'])
graph['g'].addAdjacent(graph['h'])

for node in graph.values():
    print(node)

for node in graph['a'].transverseDSF_Recursion():
    print(node.Info, end=' ')
print()

for node in graph['e'].transverseDSF_Recursion():
    print(node.Info, end=' ')
print()

for node in graph['a'].transverseDPS_NoRecursion():
    print(node.Info, end=' ')
print()

for node in graph['e'].transverseDPS_NoRecursion():
    print(node.Info, end=' ')
print()

for node in graph['a'].transverseBFS():
    print(node.Info, end=' ')
print()

for node in graph['e'].transverseBFS():
    print(node.Info, end=' ')
print()

print(graph['a'].hasCycle())

graph['g'].addAdjacent(graph['c'])
print(graph['a'].hasCycle())