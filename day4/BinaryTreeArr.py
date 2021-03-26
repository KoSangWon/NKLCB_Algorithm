# array
import array

class BinaryTree:
    def __init__(self, arr):
        self.array = array.array('l', arr)    
        
    def preorder(self):
        s = ''
        def recursive(idx):
            nonlocal s
            if idx >= len(self.array):
                return

            s += str(self.array[idx]) + ' '
            recursive(2*idx + 1)
            recursive(2*idx + 2)

        recursive(0)
        print(s)

    def inorder(self):
        s = ''
        def recursive(idx):
            nonlocal s
            if idx >= len(self.array):
                return

            recursive(2*idx + 1)
            s += str(self.array[idx]) + ' '
            recursive(2*idx + 2)

        recursive(0)
        print(s)

    def postorder(self):
        s = ''
        def recursive(idx):
            nonlocal s
            if idx >= len(self.array):
                return

            recursive(2*idx + 1)
            recursive(2*idx + 2)
            s += str(self.array[idx]) + ' '

        recursive(0)
        print(s)
    
    def bfs(self, value):
        for i in range(len(self.array)):
            if self.array[i] == value:
                return True
        return False

    def dfs(self, value):
        isFound = False

        def recursive(idx):
            nonlocal isFound
            if idx >= len(self.array):
                return
            
            if isFound is True:
                return

            if self.array[idx] == value:
                isFound = True

            recursive(2*idx + 1)
            recursive(2*idx + 2)
        recursive(0)
        return isFound
        

if __name__=="__main__":
    binaryTree = BinaryTree([1,2,3,4,5,6])
    binaryTree.preorder()
    binaryTree.inorder()
    binaryTree.postorder()
    print(binaryTree.bfs(3))
    print(binaryTree.dfs(3))