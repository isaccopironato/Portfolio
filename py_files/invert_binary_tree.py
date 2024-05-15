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

        while True:
            if itr == None:
                break

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

        while True: 

            if itr == None:
                break

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
        
    def reverseorder(self, node):
                
        if node == None:
            return []
        else:
            return self.reverseorder(node.right) + [node.val] + self.reverseorder(node.left)
        
tree = Binarytree()
my_l = [17,3,13,10,19,22,33,2,4,7,8,14]

tree.add_list_of_nodes(my_l)

print(tree.is_val_in_tree(14))
print(tree.inorder(tree.root))
print(tree.reverseorder(tree.root))