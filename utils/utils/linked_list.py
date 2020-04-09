from typing import List


class ListNode:
    def __init__(self, value, _next=None):
        self.value = value
        self.next = _next
    
    def __repr__(self):
        return f"Node<{self.value}>"


class LinkedList:
    def __init__(self, values: List[any]):
        self.values = values
        self.head = None 
        self._create()
        
    def _create(self) -> None:
        prev = None
        for value in self.values:
            if prev:
                prev.next = ListNode(value)
                prev = prev.next
            else:
                self.head = ListNode(value)
                prev = self.head


def create_ll(values: List[any]) -> ListNode:
    return LinkedList(values).head