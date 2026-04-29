func hasDuplicate(nums []int) bool {
    seenBefore := make(map[int]struct{})

    for i := 0; i < len(nums); i++{
        //check if nums exist
        _, ok := seenBefore[nums[i]]
        if ok{
           return true 
        }
        //add to map if not seen
        seenBefore[nums[i]] = struct{}{}
    } 

    return false
}
