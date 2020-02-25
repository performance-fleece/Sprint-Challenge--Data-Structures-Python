class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        #compare root now
        # #if lesser go left child

        if value < self.value:
            if not self.left:
                self.left = BinarySearchTree(value)
            else: 
                #something is already there, recurse
                self.left.insert(value)
        
        else:
            #if greater go right child
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)
 

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        if target < self.value:
            if not self.left:
                return False
            else:
                return self.left.contains(target)
        else:
            if not self.right:
                return False
            else:
                return self.right.contains(target)

        