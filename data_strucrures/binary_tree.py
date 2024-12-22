
class node():
    def __init__(self):
        self.val = None
        self.prew = None
        self.left = None
        self.right = None

class tree():
    def __init__(self):
        self.roote = node()
    
    def add_node(self, val):

        itr = self.roote

        if itr.val == None:
            itr.val = val

        
        while itr.val != None: 
            if itr.val > val:
                if itr.right.val == None: 
                    itr.right == node()
                    itr.right.val = val
                    break
                itr = itr.right

            elif itr.val < val:
                if itr.left == None:
                    itr.left == node()
                    itr.left.val = val
                    break
                itr = itr.left

            else: 
                print("val all ready in tree")


    def remuve_node(self):
        pass
    
    def find_node_plece(self):
        pass

    def check_for_val(self, val):
        if self.roote.val == None:
            return None
        elif self.roote.val == val: 
            return None # return path  
            
