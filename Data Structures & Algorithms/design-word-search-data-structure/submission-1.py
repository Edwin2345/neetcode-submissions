class WordDictionary:
    class LetterNode:
        def __init__(self):
            self.isEndWord = False
            self.nextLetter = [None]*26

    def __init__(self):
        self.base = self.LetterNode()

    def addWord(self, word: str) -> None:
        node = self.base
        for i,letter in enumerate(word):
            #calc letter index
            letterIndex = ord(letter) - ord('a')            
            #insert letter if not there
            if node.nextLetter[letterIndex] is None:
               node.nextLetter[letterIndex] = self.LetterNode()            
            #set it to isEndWord if applicaple
            if i == len(word) - 1:
               node.nextLetter[letterIndex].isEndWord = True
            #go to next node
            node = node.nextLetter[letterIndex]
        
    def search(self, word: str) -> bool:
        
        def searchHelper(node,index):
            #reached end of word
            if index >= len(word):
               return node.isEndWord

            #current letter not is a dot 
            if word[index] != ".":
               letterIndex = ord(word[index]) - ord("a")
               if node.nextLetter[letterIndex] is None:
                  return False
               return searchHelper(node.nextLetter[letterIndex], index + 1)

            #if current letter is a dot, see if any match
            for i in range(26):
                if node.nextLetter[i] and searchHelper(node.nextLetter[i], index + 1):
                   return True
            return False  
        
        return searchHelper(self.base, 0)
        
