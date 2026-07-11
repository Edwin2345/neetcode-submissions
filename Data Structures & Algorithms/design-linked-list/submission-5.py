class ListNode:
    def __init__(self, val=-1, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class MyLinkedList:

    def __init__(self):
        self.head = self.tail = ListNode()
        self.length = 0

    def get(self, index: int) -> int:
        if index < 0 or index > self.length-1:
            return -1

        self.node = self.head

        while index > 0:
            self.node = self.node.next
            index -= 1
        
        return self.node.val

    def addAtHead(self, val: int) -> None:
        if self.head.val == -1:
            self.head.val = val
        
        else:
            self.head.prev = ListNode(val, self.head)
            self.head = self.head.prev
        
        self.length += 1

    def addAtTail(self, val: int) -> None:
        if self.tail.val == -1:
            self.tail.val = val
        
        else:
            self.tail.next = ListNode(val, None, self.tail)
            self.tail = self.tail.next
        
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.length:
            return None
        
        elif index == self.length:
            self.addAtTail(val)

        elif index == 0:
            self.addAtHead(val)
        
        else:
            self.node = self.head
            
            while index > 1:
                self.node = self.node.next
                index -= 1
            
            self.node.next = temp = ListNode(val, self.node.next, self.node)
            self.node = self.node.next.next
            self.node.prev = temp

            self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index > self.length-1:
            return None
        
        elif index == self.length-1:
            self.tail = self.tail.prev
            self.tail.next = None
        
        elif index == 0:
            self.head = self.head.next
            self.head.prev = None
        
        else:
            self.node = self.head
            while index > 1:
                self.node = self.node.next
                index -= 1
            
            self.node.next = self.node.next.next
            temp = self.node
            self.node = self.node.next
            self.node.prev = temp
        
        self.length -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)