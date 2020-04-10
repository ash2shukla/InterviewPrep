from typing import List


class ListNode:
    def __init__(self, val, _next=None):
        self.val = val
        self.next = _next
        self.iter_node = self
    
    def __repr__(self):
        return f"Node<{self.val}>"

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.iter_node:
            current_val = self.iter_node.val
            self.iter_node = self.iter_node.next
            return current_val
        else:
            raise StopIteration


class LinkedList:
    def __init__(self, vals: List[any]):
        self.vals = vals
        self.head = None
        self.iter_node = None
        self._create()

    def _create(self) -> None:
        prev = None
        for val in self.vals:
            if prev:
                prev.next = ListNode(val)
                prev = prev.next
            else:
                self.head = ListNode(val)
                prev = self.head


def create_ll(vals):
    return LinkedList(vals).head


if __name__ == "__main__":
    linked_list = create_ll([1, 2, 3, 4])
    print(list(linked_list))