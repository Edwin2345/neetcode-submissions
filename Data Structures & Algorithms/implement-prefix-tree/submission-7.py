class PrefixTree:
    # 26 possible characters -> so we nee an array of 26 pointers
    # need to indicate if leeter node is end of word with flag
    class LetterNode:
        def __init__(self):
            self.isEndOfWord = False
            self.letters = [None]*26

    def __init__(self):
        self.base = self.LetterNode()

    def insert(self, word: str) -> None:
        #traverse letter by letter
        curNode = self.base

        for letter in word:
            letterIndex = ord(letter) - ord("a")
            #create letter nodes if they dont exist for word
            if curNode.letters[letterIndex] is None:
               curNode.letters[letterIndex] = self.LetterNode()
            curNode = curNode.letters[letterIndex] 

        #set last node as end of word
        curNode.isEndOfWord = True

    def search(self, word: str) -> bool:
        #search letter by letter
        curNode = self.base

        for letter in word:
            letterIndex = ord(letter) - ord("a")
            if curNode.letters[letterIndex] is None:
               return False
            curNode = curNode.letters[letterIndex]
        
        #return true only if last letter is explciitly end of a word
        return curNode.isEndOfWord
          

    def startsWith(self, prefix: str) -> bool:
        #search letter by letter
        curNode = self.base

        for letter in prefix:
            letterIndex = ord(letter) - ord("a")
            if curNode.letters[letterIndex] is None:
               return False
            curNode = curNode.letters[letterIndex]
        
        #return true as all letters found
        return True
        