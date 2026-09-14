class PrefixTree:
    #N: only lowercase inglish characters
    class LetterNode:
        def __init__(self):
            self.isEndWord = False
            self.letters = [None]*26

    def __init__(self):
        self.base = self.LetterNode()
        
    def insert(self, word: str) -> None:
        def insertByLetter(node, index):
            #compute letter index
            letterIndex = ord(word[index]) - ord("a") 

            #insert letter node for the current letter we are on
            if node.letters[letterIndex] is None:
               node.letters[letterIndex] = self.LetterNode()

            #if at end of word -> mark it and return
            if index == len(word) - 1:
               node.letters[letterIndex].isEndWord = True 
               return
            
            #otherwise. go insert next letter node
            return insertByLetter(node.letters[letterIndex], index + 1)
        
        return insertByLetter(self.base, 0)

    def search(self, word: str) -> bool:
        def searchByLetter(node, index):
            #compute letter index
            letterIndex = ord(word[index]) - ord("a") 

            #letter is not present
            if node.letters[letterIndex] is None:
               return False

            #check if end of word
            if index == len(word)-1:
               return node.letters[letterIndex].isEndWord
            
            #otherwise search for next letter
            return searchByLetter(node.letters[letterIndex], index + 1)
        
        return searchByLetter(self.base, 0)
                 

    def startsWith(self, prefix: str) -> bool:
        def startsByLetter(node, index):
            #compute letter index
            letterIndex = ord(prefix[index]) - ord("a") 

            #letter not there
            if node.letters[letterIndex] is None:
               return False 

            #reached end of prefix
            if index == len(prefix)-1:
               return True
            
            #othewise search for next letter in prefix
            return startsByLetter(node.letters[letterIndex], index + 1)
                    
        return startsByLetter(self.base, 0)
        
        