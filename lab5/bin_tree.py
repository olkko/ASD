class BST_tree:
    def search(self, key, root):
        if root is None or root.key == key:
            return root
        if root.key < key:
            return self.search(key, root.right)
        return self.search(key, root.left)

    def insert(self, root, key, value):
        if root is None:
            return Node(key, value)
        if root.key == key:
            root.value = value
            return root
        elif root.key < key:
            root.right = self.insert(root.right, key, value)
        else:
            root.left = self.insert(root.left, key, value)
        return root

    def delete(self, root, key):
        if root is None:
            return root
        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            else:
                temp = self.find_min(root.right)
                root.key = temp.key
                root.value = temp.value
                root.right = self.delete(root.right, temp.key)
        return root

    def find_min(self, root):
        while root.left is not None:
            root = root.left
        return root

    def print(self, root):
        if root is not None:
            self.print(root.left)
            print(root.key, root.value)
            self.print(root.right)

    def height(self, root):
        if root is None:
            return 0
        leftCount = self.height(root.left)
        rightCount = self.height(root.right)
        return max(leftCount, rightCount)+1
    
    def print_tree(self, root):
        print("==============")
        self.__print_tree(root, 0)
        print("==============")

    def __print_tree(self, node, lvl):
        if node!=None:
            self.__print_tree(node.right, lvl+5)

            print()
            print(lvl*" ", node.key, node.value)
     
            self.__print_tree(node.left, lvl+5)

class Node:
    def  __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

def main():
    tree = BST_tree()
    root = None
    root = tree.insert(root, 50, "A")
    root = tree.insert(root, 15, "B")
    root = tree.insert(root, 62, "C")
    root = tree.insert(root, 5, "D")
    root = tree.insert(root, 20, "E")
    root = tree.insert(root, 58, "F")
    root = tree.insert(root, 91, "G")
    root = tree.insert(root, 3, "H")
    root = tree.insert(root, 8, "I")
    root = tree.insert(root, 37, "J")
    root = tree.insert(root, 60, "K")
    root = tree.insert(root,24, "L")
    tree.print_tree(root)

    node = tree.search(24, root)
    print(node.value)

    node.value = "AA"
    tree.print_tree(root)

    root = tree.insert(root, 6, "M")

    root = tree.delete(root, 62)

    root = tree.insert(root, 59, "N")
    root = tree.insert(root, 100, "P")

    root = tree.delete(root, 8)
    root = tree.delete(root, 15)

    root = tree.insert(root, 55, "R")

    root = tree.delete(root, 50)
    root = tree.delete(root, 5)
    root = tree.delete(root, 24)

    height = tree.height(root)
    print(height)
    
    tree.print(root)
    tree.print_tree(root)




if __name__ == '__main__':
    main()