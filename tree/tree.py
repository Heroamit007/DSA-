class Tree:
    def __init__(self, items=None, left=None, right=None):
        self.items = items
        self.left = left
        self.right = right
class BinarySearchTree:
    def __init__(self, root=None):
        self.root = root
    def is_empty(self):
        return self.root == None
    # def insert(self, data):
    #     new_node = Tree(data)
    #     if self.root is None:
    #         self.root = new_node
    #         return
    #     else:
    #         current = self.root
    #         while True:
    #             if data < current.items:
    #                 if current.left is None:
    #                     current.left = new_node
    #                     return
    #                 current = current.left

    #             elif data > current.items:
    #                 if current.right is None:
    #                     current.right = new_node
    #                     return
    #                 current = current.right
    #             else:
    #                 return
    def insert(self, data):
        if self.root is None:
            self.root = Tree(data)
        else:
            self.rinsert(self.root, data)
    def rinsert(self, root, data):
        if root is None:
            return Tree(data)
        if data < root.items:
            root.left = self.rinsert(root.left, data)
        elif data > root.items:
            root.right = self.rinsert(root.right, data) 
        return root
    def search(self,data):
        return self.rsearch(self.root, data)
    def rsearch(self, root, data):
        if root is None or root.items == data:
            return root
        if data<root.items:
            return self.rsearch(root.left, data)
        else:
            return self.rsearch(root.right, data)
    def inorder(self):
        result = []
        self.rinorder(self.root, result)
        return result
    def rinorder(self, root, result):
        if root:
            self.rinorder(root.left, result)
            result.append(root.items)
            self.rinorder(root.right, result)
    def preorder(self):
        result = []
        self.rpreorder(self.root, result)
        return result
    def rpreorder(self, root, result):
        if root:
            result.append(root.items)
            self.rpreorder(root.left, result)
            self.rpreorder(root.right, result)
    def postorder(self):
        result = []
        self.rinorder(self.root, result)
        return result
    def rpostorder(self, root, result):
        if root:
            self.rpostorder(root.left, result)
            self.rpostorder(root.right, result)
            result.append(root.items)
    def minimumValue(self,temp):
        current = temp
        while current.left is not None:
            current = current.left
        return current.items
    
    def maximumValue(self, temp):
        current = temp
        while current.right is not None:
            current = current.right
        return current.items
    def delete(self, data):
        self.root = self.rdelete(self.root, data)
    def rdelete(self, root, data):
        if root is None:
            return root
        elif data < root.items:
            self.root = self.rdelete(root.left, data)
        elif data > root.items:
            self.root = self.rdelete(root.right, data)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            root.items = self.minimumValue(root.right, data)
            self.rdelete(root.right,root.items)
        return root
    
    def size(self):
        return len(self.inorder())

   
    




#deriver code
bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
bst.insert(15) 
bst.insert(3)
print(bst.root.items)  # Output: 10
print(bst.root.left.items)  # Output: 5
print(bst.root.right.items)  # Output: 15
print(bst.root.left.left.items)  # Output: 3