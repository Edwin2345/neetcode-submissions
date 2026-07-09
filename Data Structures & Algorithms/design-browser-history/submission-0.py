class ListNode:
    def __init__(self, val, next=None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev

class BrowserHistory:

    def __init__(self, homepage: str):
        self.node = ListNode(homepage)

    def visit(self, url: str) -> None:
        self.node.next = ListNode(url, None, self.node)
        self.node = self.node.next

    def back(self, steps: int) -> str:
        while self.node.prev and steps > 0:
            self.node = self.node.prev
            steps -= 1
        
        return self.node.val

    def forward(self, steps: int) -> str:
        while self.node.next and steps > 0:
            self.node = self.node.next
            steps -= 1
        
        return self.node.val



# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)