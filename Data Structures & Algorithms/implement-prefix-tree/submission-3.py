class PrefixTree:
    #N: only lowercase inglish characters
    class LetterNode:
        def __init__(self):
            self.isEndWord = False
            self.letters = [None]*26

    def __init__(self):
        self.base = self.LetterNode()
        
    def insert(self, word: str) -> None:
        curNode = self.base

        for i,letter in enumerate(word):
            #calc letter index
            letterIndex = ord(letter) - ord("a")
            #add node if not exist
            if curNode.letters[letterIndex] is None:
               curNode.letters[letterIndex] = self.LetterNode()
            #mark as end if last
            if i == len(word) - 1:
               curNode.letters[letterIndex].isEndWord = True
            #go to next node
            curNode = curNode.letters[letterIndex]
        

    def search(self, word: str) -> bool:
        curNode = self.base

        for i,letter in enumerate(word):
            #calc letter index
            letterIndex = ord(letter) - ord("a")
            #letter not present, return false
            if curNode.letters[letterIndex] is None:
               return False
            #end of word -> check if isEndWord
            if i == len(word) - 1:
               return curNode.letters[letterIndex].isEndWord
            #go to next node
            curNode = curNode.letters[letterIndex]     
                 

    def startsWith(self, prefix: str) -> bool:
        curNode = self.base

        for i,letter in enumerate(prefix):
            #calc letter index
            letterIndex = ord(letter) - ord("a")
            #letter not present, return false
            if curNode.letters[letterIndex] is None:
               return False
            #end of word, return True
            if i == len(prefix) - 1:
               return True
            #go to next node
            curNode = curNode.letters[letterIndex]
      
                    

        