func updateCount(r rune, freqMap map[rune]int){
    if _,ok := freqMap[r]; !ok{
	   freqMap[r] = 0	
	}
	freqMap[r] += 1
}

func isAnagram(s string, t string) bool {
    //return early if both string are diff lengths
	if len(s) != len(t){
		return false
	}

	//build map of letter counts
	sRunes := []rune(s)
	tRunes := []rune(t)
    sMap := make(map[rune]int)
	tMap := make(map[rune]int)
	for i := 0; i < len(s); i++{
        updateCount(sRunes[i],sMap)
		updateCount(tRunes[i],tMap)
	}

	//compare maps
    for sRune,sCnt := range sMap{
        tCnt,ok := tMap[sRune]
		if !ok || tCnt != sCnt{
			return false
		}
	}
	return true
}
