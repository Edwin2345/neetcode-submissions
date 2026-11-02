class Solution:
    # time for car i to reach = (target - position[i])/speed[i]
    # car cannot pass, so i-1th car can't pass ith car ordered by position ascending
    #create tuples of (pos, timeToFinish) and put into list to sort
    #garenteed to sort uniquely  as all position valeus are unqiue 
    # if timeToFinish if i-1th car is <= that of ith, they are same fleet, else increment

    # TC: O(nlogn), SC: O(n) extra
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #create list of tuples
        cars = []
        for i in range(len(position)):
            timeToFinish = (target - position[i]) / speed[i]
            cars.append( (position[i], timeToFinish) )
        
        #sort by positions (good enoguh as unqiue)
        #if they werent sort by time to finsih decreasing to 
        #preveent them from being treated as one fleet
        cars.sort(key=lambda t : (t[0], t[1] * -1) )

        #work backwards starting from car at furthest position
        # sotre inishign tiems in stack
        stack = [cars[-1][1]]
        for i in range(len(cars)-2 , -1, -1):
            #new car fleet (i-1th finsihed after ith car)
            #if so, append its finsihign tiem to top of stack
            if cars[i][1] > stack[-1]:
               stack.append( cars[i][1] ) 

        return len(stack)