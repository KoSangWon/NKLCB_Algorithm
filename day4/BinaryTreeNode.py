# node
class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self, array):
        node_list = [Node(value, None, None) for value in array]
        for ind, node in enumerate(node_list):
            left = 2 * ind + 1
            right = 2 * ind + 2
            if left < len(node_list):
                node.left = node_list[left]
            if right < len(node_list):
                node.right = node_list[right]

        self.root = node_list[0]

    def preorder(self):
        def recursive(node):
            if node is None:
                return 
            print(node.value, end=' ')
            recursive(node.left)
            recursive(node.right)
        recursive(self.root)
        print()
            
    def inorder(self):
        def recursive(node):
            if node is None:
                return 
            recursive(node.left)
            print(node.value, end=' ')
            recursive(node.right)
        recursive(self.root)
        print()
    
    def postorder(self):
        def recursive(node):
            if node is None:
                return 
            recursive(node.left)
            recursive(node.right)
            print(node.value, end=' ')
        recursive(self.root)
        print()

    def bfs(self, value):
        q = [self.root]
        while q:
            v = q.pop(0)
            if v.value == value:
                return True
            for i in (v.left, v.right):
                if i is not None:
                    q.append(i)
        return False
    
    def dfs(self, value):
        isFound = False
        def recursive(node):
            nonlocal isFound

            if isFound is True:
                return

            if node.value == value:
                isFound = True

            for i in (node.left, node.right):
                if i is not None:
                    recursive(i)
           
        recursive(self.root)
        return isFound

if __name__=="__main__":
    binaryTree = BinaryTree([i for i in range(1, 8)])
    binaryTree.preorder()
    binaryTree.inorder()
    binaryTree.postorder()
    print(binaryTree.bfs(1))
    print(binaryTree.dfs(8))