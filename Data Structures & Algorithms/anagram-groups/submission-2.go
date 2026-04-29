func groupAnagrams(strs []string) [][]string {
    //make a dict that is key: [26]int (freq count of letters), value: []string
    dict := make(map[[26]int]([]string))
    
    //iterate through each string
    for _,str := range strs{
        //build freq count of letters in string
        letterCnt := [26]int{}
        for _,char := range str{
            letterCnt[int(char) - int('a')] += 1
        }

        //add string to map
        dict[letterCnt] = append(dict[letterCnt],str)
    }

    //return lsit of groups
    groups := make([][]string,0)
    for _,strList := range dict{
        groups = append(groups, strList)
    }
    return groups
}
