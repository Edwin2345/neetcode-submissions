func twoSum(nums []int, target int) []int {
    arrMap := make(map[int]int)
    for i := 0; i < len(nums); i++{
        //check if pair exists
        smallerIndex, ok := arrMap[target-nums[i]]
        if ok{
            return []int{smallerIndex, i}
        }
        //otherwise, just add it
        arrMap[nums[i]] = i
    }

    return []int{-1,-1}
}
