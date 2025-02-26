class Node(object):
    def __init__(self, v):
        self.val = v
        self.next = None
    
def delete_node(head, val):
    d = Node("temp") # 1
    d.next = head
    p = d
    c = head
    while c:
        if c.val == val:
            p.next = c.next # 2
            return d.next   # 3
        p = c
        c = c.next
    return d.next # 4 