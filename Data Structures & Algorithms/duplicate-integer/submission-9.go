func hasDuplicate(nums []int) bool {
    seenBefore := make(map[int]struct{})

    for _,val := range nums{
        //check if nums exist
        _, ok := seenBefore[val]
        if ok{
           return true 
        }
        //add to map if not seen
        seenBefore[val] = struct{}{}
    } 

    return false
}
