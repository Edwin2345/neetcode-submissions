func groupAnagrams(strs []string) [][]string {
    /*
       CLAIRIFCATIONS

	   1. are strings only lowercase cahaters
	   2. do we need to return the string groups in any order?
	   3. are empty strings/ empty strs possible

	   build a map[int[26]]([]string)

	   iterate through all string

	       build int26 array

		   add it to map
		
		iterate through values of map and append to [][]string
	*/

    anagramMap := make(map[[26]int]([]string), 0)  

	for _,str := range strs{
		//build char freq for current string
		var charFreq [26]int
		for _,ch := range str{
			charFreq[int(ch - 'a')] += 1
		}

		anagramMap[charFreq] = append(anagramMap[charFreq], str)
	}


	//turn map into list of lists
	var anagramGroups [][]string
	for _,anagramList :=  range anagramMap{
        anagramGroups = append(anagramGroups, anagramList)
	}
   
   return anagramGroups
}
