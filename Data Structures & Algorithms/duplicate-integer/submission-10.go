func hasDuplicate(nums []int) bool {
    seenBefore := make(map[int]bool, 0)
    for _,num := range nums{
        if _,ok := seenBefore[num]; ok{
           return true 
        }
        seenBefore[num] = true
    }
    return false
}
