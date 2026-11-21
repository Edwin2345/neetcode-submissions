class Solution:
    # immediate edge case --. if len(hand) % groupSize != 0 --> false
    # count the freq of card valeus with a map, also keep track of the smallest hand
    # do a fixed set of interations for number of hands needed, taking smallest avialble hand as starting
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

        # try to make enough straights
        # TC: O(N // K) * (O(N) + O(K)) == O(N^2)
        # SC: O(1)
        for _ in range(len(hand) // groupSize):
            # find the smallestHand value to start the group
            smallestHand = min(cardMap.keys())

            # see if you can form a straight of groupSize, if not, not possible
            curVal = smallestHand
            for _ in range(groupSize):
                if curVal not in cardMap:
                    return False

                cardMap[curVal] -= 1
                if cardMap[curVal] == 0:
                    del cardMap[curVal]

                curVal += 1

        return True
