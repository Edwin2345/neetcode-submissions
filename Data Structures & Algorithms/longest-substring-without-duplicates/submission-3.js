class Solution {
    /**
     * @param {string} s
     * @return {number}
     */
    lengthOfLongestSubstring(s) {
        let maxLength=0;
        let L=0;
        let R=0;
        const subStrSet = new Set();

        for(R; R<s.length; ++R){
            //Shrink window until can add new char (if ness)
            while(subStrSet.has(s[R]) && L<R){
                 subStrSet.delete(s[L]);
                 ++L;
            }

            //add the current char to window
            subStrSet.add(s[R]);

            //update maxLength
            maxLength = Math.max(maxLength, subStrSet.size);
        }

        return maxLength;
    }
}
