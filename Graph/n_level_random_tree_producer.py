import json
import random

_PROBILITY_FACTOR = 4
_HEIGHT = 20


class Node:
    def __init__(self, index, left=None, right=None):
        self.index = index
        self.left = left
        self.right = right

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


def producer(height=10):
    global _PROBILITY_FACTOR
    _PROBILITY_FACTOR = height
    root = Node(1)
    levelNMaker([root], 1)
    return root


def levelNMaker(nodes, level):

    if(level == _HEIGHT):
        return

    nextLevelNodes = []
    for node in nodes:
        addChildren(node)
        if(node.right is not None):
            nextLevelNodes.append(node.right)
        if(node.left is not None):
            nextLevelNodes.append(node.left)

    levelNMaker(nextLevelNodes, level + 1)


def addChildren(node):

    hasRight = random.randint(1, 10) > _PROBILITY_FACTOR
    hasLeft = random.randint(1, 10) > _PROBILITY_FACTOR

    if(hasRight):
        node.right = Node(node.index + 1)

    if(hasLeft):
        node.left = Node(
            node.index + 2 if hasRight else node.index + 1)

    return


def getHight(root, counter=1):
    if(root.right is not None):
        return getHight(root.right, counter + 1)
    if(root.left):
        return getHight(root.left, counter + 1)
    
    if(root.right is None and root.left is None):
        return counter
