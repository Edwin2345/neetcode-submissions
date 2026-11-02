class WordDictionary:
    class LetterNodes:
        def __init__(self):
            self.isEndOfWord = False
            self.letters = [None]*26

    def __init__(self):
        self.base = self.LetterNodes()

    def addWord(self, word: str) -> None:
        curNode = self.base

        for letter in word:
            letterIndex = ord(letter) - ord("a")
            if curNode.letters[letterIndex] is None:
               curNode.letters[letterIndex] = self.LetterNodes()
            curNode = curNode.letters[letterIndex]

        curNode.isEndOfWord = True
               
    def search(self, word: str) -> bool:

        def helper(curNode, index):
            #empty node
            if curNode is None:
               return False 
            #finished checking entire word
            if index == len(word):
               return curNode.isEndOfWord

            #if dot, search throguh all existing letters
            if word[index] == ".":
               for i in range(26):
                   if curNode.letters[i] and helper(curNode.letters[i], index + 1):
                      return True
            #otherwise check if exact letter exists
            else:
                letterIndex = ord(word[index]) - ord("a")
                if curNode.letters[letterIndex] is None:
                   return False 
                return helper(curNode.letters[letterIndex], index + 1)

            #word not found
            return False
        
        return helper(self.base, 0)


        
