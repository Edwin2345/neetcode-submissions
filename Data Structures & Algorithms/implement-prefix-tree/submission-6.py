class PrefixTree:
    #N: only lowercase inglish characters
    class LetterNode:
        def __init__(self):
            self.isEndWord = False
            self.nextLetter = [None]*26

    def __init__(self):
        self.base = self.LetterNode()
        
    def insert(self, word: str) -> None:
        curNode = self.base

        for i,letter in enumerate(word):
            #calc letter index
            letterIndex = ord(letter) - ord("a")
            #add node if not exist
            if curNode.nextLetter[letterIndex] is None:
               curNode.nextLetter[letterIndex] = self.LetterNode()
            #go to next node
            curNode = curNode.nextLetter[letterIndex]
         
        #mark last letter as end of word
        curNode.isEndWord = True
        
    def search(self, word: str) -> bool:
        curNode = self.base

        for i,letter in enumerate(word):
            #calc letter index
            letterIndex = ord(letter) - ord("a")
            #letter not present, return false
            if curNode.nextLetter[letterIndex] is None:
               return False
            #go to next node
            curNode = curNode.nextLetter[letterIndex]     
         
        #at last letter Node, check if end of word
        return curNode.isEndWord
                 

    def startsWith(self, prefix: str) -> bool:
        curNode = self.base

        for i,letter in enumerate(prefix):
            #calc letter index
            letterIndex = ord(letter) - ord("a")
            #letter not present, return false
            if curNode.nextLetter[letterIndex] is None:
               return False
            #go to next node
            curNode = curNode.nextLetter[letterIndex]
        
        #all letters in prefix exist
        return True
                    

        