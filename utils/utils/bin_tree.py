from typing import List


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.iter_stack = [self]
    
    def __repr__(self):
        return f'TreeNode<{self.val}>'
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.iter_stack:
            popped = self.iter_stack.pop(0)
            if popped:
                if popped.left:
                    self.iter_stack.append(popped.left)
                if popped.right:
                    self.iter_stack.append(popped.right)
                return popped.val
        else:
            raise StopIteration


class BinaryTree:
    def __init__(self, vals: List[int]):
        self.vals = vals
        self.root = None
        self._create()
    
    def _create(self):
        nodes = []
        for val in self.vals:
            nodes.append(TreeNode(val))
        
        for idx, node in enumerate(nodes):
            try:
                node.left = nodes[2*idx + 1]
                node.right = nodes[2*idx + 2]
            except IndexError:
                pass
        self.root = nodes[0]


def create_btree(values):
    return BinaryTree(values).root


if __name__ == "__main__":
    bt = create_btree([1, 2, 3, None, None, 4, 5])
    for i in bt:
        print(i)