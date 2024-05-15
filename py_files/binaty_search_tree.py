class Binarynode:
    def __init__(self, data = None) -> None:
        self.data = data
        self.left = None
        self.right = None

class Binarytree:

    def __init__(self) -> None:
        self.roote = Binarynode()

    def add_node(self, data):

        itr = self.roote

        if itr.data == None: 
            itr.data = data

        while True:
            if itr.data < data: 
                if itr.right == None:
                    itr.right = Binarynode(data)
                    break
                else: 
                    itr = itr.right
            else: 
                if itr.left == None:
                    itr.left = Binarynode(data)
                    break
                else: 
                    itr = itr.left

    def add_list_of_nodes(self, data_list: list)-> None:
        for i in data_list:
            self.add_node(i)

    def if_data_in_tree(self, data):

        itr = self.roote

        while True:
            if itr == None:
                return False
               
            if itr.data == data: 
                return True
            
            elif data > itr.data:
                itr = itr.right
            else: 
                itr = itr.left


    
tree = Binarytree()
my_l = [i for i in range(0, 1000 ,13)]
tree.add_list_of_nodes(my_l)

print(tree.if_data_in_tree(20))
print(tree.if_data_in_tree(8))
print(tree.if_data_in_tree(30))
print(tree.if_data_in_tree(5))
print(tree.if_data_in_tree(3))

print(tree.if_data_in_tree(13))
print(tree.if_data_in_tree(26))