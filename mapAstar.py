#!/usr/bin/env python3

from queue import PriorityQueue


class Node():
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position


def astar(map, start, end):

    openList = []
    closeList = []
    startNode = Node(None,start)
    startNode.g = startNode.h = startNode.f = 0
    endNode = Node(None, end)
    endNode.g = endNode.h = endNode.f = 0

    openList.append(startNode)

    while len(openList) > 0:
        currentNode = openList[0]
        currentIndex = 0
        for index, item in enumerate(openList):
            if item.f < currentNode.f:
                currentNode = item
                currentIndex = index

        openList.pop(currentIndex)
        closeList.append(currentNode)

        if currentNode == endNode:
            path = []
            current = currentNode
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1]

        children = []
        neigbors = [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]

        for neigbor in neigbors:
            nodePosition = (currentNode.position[0]+neigbor[0],currentNode.position[1]+neigbor[1])

            if nodePosition[0] > (len(map)-1) or nodePosition[0] < 0 or nodePosition[1] > (len(map[len(map)-1]) -1) or nodePosition[1] < 0:
                continue
            if map[nodePosition[0]][nodePosition[1]] != 0:
                continue

            newNode=Node(currentNode,nodePosition)
            children.append(newNode)


        for child in children:
            if child in closeList:
                continue
            child.g = currentNode.g+1
            child.h = ((child.position[0] - endNode.position[0]) ** 2) + ((child.position[1] - endNode.position[1]) ** 2)
            child.f = child.g+child.h
            
            for openNode in openList:
                if child == openNode and child.g > openNode.g:
                    continue

            openList.append(child)



def main():

    maze = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    start = (1, 0)
    end = (9, 6)

    path = astar(maze, start, end)
    print(path)


if __name__ == '__main__':
    main()

















    
    



