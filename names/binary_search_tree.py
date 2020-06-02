class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        current = self
        while current:
            if current.value > value:
                if current.left is None:
                    current.left = BSTNode(value)
                    return
                current = current.left
            elif current.value <= value:
                if current.right is None:
                    current.right = BSTNode(value)
                    return
                current = current.right

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        current = self

        while current:
            if current.value == target:
                return True
            elif current.value > target:
                if current.left is None:
                    return False
                current = current.left
            elif current.value < target:
                if current.right is None:
                    return False
                current = current.right
