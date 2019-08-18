from n_level_random_tree_producer import producer

root = producer(5)

print(root.toJSON())

def printLevelOrder(root): 
    for i in range(1, 6): 
        printGivenLevel(root, i) 


def printGivenLevel(root , level): 
    if root is None: 
        return
    if level == 1: 
        print (root.index) 
    elif level > 1 : 
        printGivenLevel(root.left , level-1) 
        printGivenLevel(root.right , level-1) 


printLevelOrder(root) 
