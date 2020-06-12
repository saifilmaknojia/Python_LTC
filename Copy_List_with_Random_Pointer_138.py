# Definition for a Node.


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        mapper = {}

        head_tracker = head
        # create nodes with similar values and store it in dict
        while head_tracker:
            mapper[head_tracker] = Node(head_tracker.val)
            head_tracker = head_tracker.next

        # now lets make connections
        for key, value in mapper.items():
            # attaching next pointer
            value.next = mapper.get(key.next)
            # attaching random pointer
            value.random = mapper.get(key.random)

        return mapper.get(head)
