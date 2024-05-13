class Treenode:

    def __init__(self, data = None, parent = None) -> None:
        self.data = data 
        self.children = []
        self.parent = parent

class Tree:
    
    def __init__(self) -> None:
        self.roote = Treenode()

    def find_node(self, parent, node) -> Treenode:

        if node.data == parent:
            return node
        
        if len(self.roote.children) != 0: 
            pass
        else:
            for child in node.children:
                if child.data == parent:
                    return child
                
            for child in node.children:
                return self.find_node(parent, child)
            
    def find_node_2(self, parent, node):
        pass
    
    def add_node(self, data, parent):

        if self.roote.data == None: 
            self.roote = Treenode(data)
            return

        parent_node = self.find_node(parent, self.roote)
        
        if parent_node == None: 
            raise Exception("No parent")
        
        parent_node.children.append(Treenode(data, parent_node))

    def print_node(self, data):
        print(str(self.find_node(data, self.roote).data))
        print(str(self.find_node(data, self.roote).parent))


tree = Tree()

tree.add_node("node1", "parent")
tree.add_node("node2", "node1")

tree.print_node("node1")
tree.print_node("node2")




