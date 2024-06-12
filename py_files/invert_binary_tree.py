class Binarynone:
    def __init__(self, val = None, left = None, right = None) -> None:
        self.val = val 
        self.left = left
        self.right = right

class Binarytree:
    def __init__(self) -> None:
        self.root = Binarynone()
        
    def add_node(self, val) -> None:

        itr = self.root

        if itr.val == None:
            itr.val = val
            return
        
        while itr:
            if itr.val > val:
                if itr.left == None:
                    itr.left = Binarynone(val)
                    break
                else: 
                    itr = itr.left
            else:
                if itr.right == None:
                    itr.right = Binarynone(val)
                    break
                else:
                    itr = itr.right

    def add_list_of_nodes(self, list_val) -> None:
        for i in list_val:
            self.add_node(i)

    def is_val_in_tree(self, val) -> bool:
        itr = self.root

        while itr: 
            if itr.val == val:
                return True
            if itr.val > val:
                itr = itr.left
            else: 
                itr = itr.right
        return False
    
    def decide_order(self, order):
        pass

    def inorder(self, node) -> list:
        if node == None:
            return []
        else:
            return self.inorder(node.left) + [node.val] + self.inorder(node.right)
        
    def reverse_order(self, node):
        if node == None:
            return []
        else:
            return self.reverse_order(node.right) + [node.val] + self.reverse_order(node.left)
        
    def is_val_in_tree_new(self, node, val) -> bool:
            if node is None:
                return False
            if node.val == val:
                return True
            if node.val > val:
                return self.is_val_in_tree_new(node.left,val)
            else:
                return self.is_val_in_tree_new(node.right,val)
    
        
tree = Binarytree()
my_l = [17,3,13,10,19,22,33,2,4,7,8,14]

tree.add_list_of_nodes(my_l)

print(tree.is_val_in_tree_new(tree.root, 18))
print(tree.is_val_in_tree(14))
print(tree.inorder(tree.root))
print(tree.reverse_order(tree.root))