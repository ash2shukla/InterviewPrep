from typing import List, Any, Literal
from dataclasses import dataclass, asdict
from copy import deepcopy


@dataclass
class treenode:
    value: Any
    parent_index: int
    self_index: int = None
    alignment: Literal['left', 'right'] = None


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __repr__(self):
        return f'TreeNode<{self.val}>'
    
    def __iter__(self):
        self.iter_stack = [treenode(value=self, parent_index=None, self_index=0, alignment=None)]
        self.current_idx = 0
        return self
    
    def __next__(self):
        if self.iter_stack:
            popped = self.iter_stack.pop(0)
            if popped.value:
                if popped.value.left:
                    self.current_idx += 1
                    self.iter_stack.append(treenode(value=popped.value.left, parent_index=popped.self_index, self_index=self.current_idx, alignment='left'))
                if popped.value.right:
                    self.current_idx += 1
                    self.iter_stack.append(treenode(value=popped.value.right, parent_index=popped.self_index, self_index=self.current_idx, alignment='right'))
                popped.value = popped.value.val
                return popped
        else:
            raise StopIteration


class BinaryTree:
    def __init__(self, nodes: List[treenode]):
        self.nodes: List[treenode] = deepcopy(nodes)
        self.root: TreeNode = None
        self._create()
    
    def _create(self):
        for i, node in enumerate(self.nodes):
            self.nodes[i].value = TreeNode(node.value)
            if node.alignment is not None:
                setattr(self.nodes[node.parent_index].value, node.alignment, node.value)
        self.root = (self.nodes and self.nodes[0].value) or None


def create_btree(treenodes: List[treenode]):
    return BinaryTree(treenodes).root


if __name__ == "__main__":
    treenodes = [
        treenode(value=1, parent_index=-1, alignment=None),
        treenode(value=2, parent_index=0, alignment='left'),
        treenode(value=3, parent_index=0, alignment='right'),
        treenode(value=4, parent_index=1, alignment='left'),
        treenode(value=5, parent_index=1, alignment='right')
    ]
    bt = create_btree(treenodes)
    print(list(create_btree(list(bt))))