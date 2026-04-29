func groupAnagrams(strs []string) [][]string {
	//key is bitmap of chars and value is array of strings
    anagramMap := make(map[[26]int][]string)

	for _,str := range strs{
        //create bitmap of each word
        bitMap := [26]int{}
		for _,char := range str{
			bitMap[int(char)-int('a')] += 1
		}
		
		//add to map 
		anagramMap[bitMap] = append(anagramMap[bitMap],str)
	}

    //create finalized list of groups
	groups := make([][]string,0)
	for _ , group := range anagramMap{
        groups = append(groups, group)
	}

	return groups
}
