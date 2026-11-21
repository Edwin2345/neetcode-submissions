class Solution:
    # immediate edge case --. if len(hand) % groupSize != 0 --> false
    # count the freq of card valeus with a map, also keep track of the smallest hand
    # do a fixed set of interations for number of hands needed, taking smallest avialble hand as starting
    # TC: O(NlogN for sorting), SC: O(N)
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # edge case, if nto divivible cna form hand of striaghts
        if len(hand) % groupSize != 0:
            return False

        # freq map the values
        # O(N) TC, O(N) SC
        cardMap = defaultdict(int)
        smallestHand = hand[0]
        for card in hand:
            cardMap[card] += 1
            smallestHand = min(smallestHand, card)

        # try to make enough straights, sort to start with the smalels tcard first
        #TC: O(NlogN) for sorting + O(N) for acutal algo =  O(NlogN)
        #SC : O(1)
        hand.sort()
        for card in hand:
            # find the smallest hand still avaliable
            if card not in cardMap:
               continue 

            # see if you can form a straight of groupSize
            curVal = card
            for _ in range(groupSize):
                #couldnt find straight
                if curVal not in cardMap:
                    return False

                #update card count
                cardMap[curVal] -= 1
                if cardMap[curVal] == 0:
                    del cardMap[curVal]

                #findt he next striaght value
                curVal += 1

        return True
