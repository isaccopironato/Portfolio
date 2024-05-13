class Treenode:

    def __init__(self, data = None, parent = None) -> None:
        self.data = data 
        self.children = []
        self.parent = parent

    def find_node(self, node_data):

        if self.data is node_data: 
            return self
        
        for node in self.children:
            n = node.find_node(node_data)
            if n: return n

        return None

class Tree:
    
    def __init__(self) -> None:
        self.roote = Treenode()

    def find_node(self, parent) -> Treenode:
        return self.roote.find_node(parent)
        
    def add_node(self, data, parent):

        if self.roote.data == None: 
            self.roote = Treenode(data)
            return

        parent_node = self.find_node(parent)
        
        if parent_node == None: 
            raise Exception("No parent")
        
        parent_node.children.append(Treenode(data, parent_node))

    def print_node(self, data):
        print(str(self.find_node(data).data))
        print(str(self.find_node(data).parent))


tree = Tree()

tree.add_node("node1", "parent")
tree.add_node("node2", "node1")
tree.add_node("node3", "node2")
tree.add_node("node4","node3")

tree.print_node("node1")
print()
tree.print_node("node2")
print()
tree.print_node("node4")




