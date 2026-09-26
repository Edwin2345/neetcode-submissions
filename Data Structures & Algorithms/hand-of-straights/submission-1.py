class Solution:
    #q: are the values of hands fixed -> yes
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        #edge case -> number of cards is not divisible
        if len(hand) % groupSize != 0:
           return False

        #build freq map of card
        cardMap = {}
        for card in hand:
            if card not in cardMap:
               cardMap[card] = 1
            else:
               cardMap[card] += 1        
                 
        #greedy approach: take smallest value card remaining as starting point 
        #sort to get the smallest card values
        hand.sort()
        for cardVal in hand:
            #card value not in set 
            if cardMap[cardVal] == 0:
                continue
            #try make a hand of straight starting with thsi card valu
            for targetVal in range(cardVal, cardVal + groupSize):
                #not able to put card in a straingt group
                if targetVal not in cardMap or cardMap[targetVal] == 0:
                   return False 
                cardMap[targetVal] -= 1        

        #was able to split up into consecutive sub sequences
        return True



