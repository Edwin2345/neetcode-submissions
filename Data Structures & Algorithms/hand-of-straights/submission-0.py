class Solution:
    #q: are the values of hands fixed -> yes
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        #edge case -> number of cards is not divisible
        if len(hand) % groupSize != 0:
           return False 
        
        #sort the desk
        hand.sort()


        #build freq map of card
        cardMap = {}
        for card in hand:
            if card not in cardMap:
               cardMap[card] = 1
            else:
               cardMap[card] += 1        
                 
        #greedy approach: take smallest value card remaining as starting point 
        for card in hand:
            if cardMap[card] == 0:
                continue
            #try to see if a consecutive group possilbe
            for target in range(card, card + groupSize):
                if target not in cardMap or cardMap[target] <= 0:
                   return False
                cardMap[target] -= 1             

        #was able to split up into consecutive sub sequences
        return True



