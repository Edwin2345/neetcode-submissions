func maxArea(heights []int) int {
    left := 0
	right := len(heights)-1

	//start at opposite ends, work inward
	maxArea := 0
	for left < right{
        //find curr area
		curArea := 0
		if heights[left] < heights[right]{
		   curArea = (right-left)*heights[left]
		   left += 1	
		}else{
		   curArea = (right-left)*heights[right]
		   right -= 1
		}

		//update max
		maxArea = max(maxArea, curArea)
	}

    return maxArea
}
