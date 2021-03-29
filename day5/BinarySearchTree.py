import random

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        # Ref: https://stackoverflow.com/questions/34012886/print-binary-tree-level-by-level-in-python/40885162
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.value
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.value
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.value
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.value
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2




class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    
    def __search(self, value): # __를 붙이면 private method가 된다.
        node = self.root
        parent = None
        direction = None
        
        while node:
            if node.value == value:
                break
            elif value < node.value:
                parent = node
                node = node.left
                direction = 'left'
            else:
                parent = node
                node = node.right
                direction = 'right'

        return node, parent, direction

    def insert(self, value):
        node, parent, direction = self.__search(value)

        if parent is None:
            self.root = Node(value)
            return True

        if node:
            return False
        elif direction == 'left':
            parent.left = Node(value, None, None)
        else:
            parent.right = Node(value, None, None)
        return True
        

    def insert2(self, value):
        new_node = Node(value, None, None)
        parent = self.root
        node = self.root

        if self.root is None:
            self.root = node
            return
        
        while node:
            parent = node
            if node.value > value:
                node = node.left
            else:
                node = node.right

        if parent.value < value:
            parent.right = new_node
        else:
            parent.left = new_node

    def search(self, value):
        node, _, _ = self.__search(value)
        return node

    def search2(self, value):
        node = self.root
        while node:
            if node.value == value:
                return True
            elif node.value > value:
                node = node.left
            else:
                node = node.right
        return False

    def remove(self, value):
        node, parent, direction = self.__search(value)

        # 찾는 값이 없는 경우
        if node is None:
            return False

        # 자식 노드가 없는 경우
        if node.left is None and node.right is None:
            if direction == 'left':
                parent.left = None
            elif direction == 'right':
                parent.right = None
            else:
                self.root = None # root node

        # 자식 노드가 하나(left)인 경우
        elif node.right is None:
            if direction == 'left':
                parent.left = node.left
            elif direction == 'right':
                parent.right = node.left
            else:
                self.root = node.left # root node

        # 자식 노드가 하나(right)인 경우
        elif node.left is None:
            if direction == 'left':
                parent.left = node.right
            elif direction == 'right':
                parent.right = node.right
            else:
                self.root = node.right # root node

        # 자식 노드가 둘인 경우
        else:
            right_node_parent = node
            right_node = node.left
            while right_node.right:
                right_node_parent = right_node
                right_node = right_node.right 

            if right_node.left:
                right_node_parent.right = right_node.left        

            if node == right_node_parent:
                parent.right = right_node
                


            right_node.left = node.left
            right_node.right = node.right
            if direction == 'left':
                parent.left = right_node
            elif direction == 'right':
                parent.right = right_node
            else:
                self.root = right_node

        return True
                
                
bst = BinarySearchTree()

x = list(range(20))
random.shuffle(x)
for el in x:
    bst.insert(el)
bst.root.display()

bst.remove(6)
bst.root.display()

bst.remove(10)
bst.root.display()