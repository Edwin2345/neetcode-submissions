/**
 * Pair class to store key-value pairs
 */
// class Pair {
//     /**
//      * @param {number} key The key to be stored in the pair
//      * @param {string} value The value to be stored in the pair
//      */
//     constructor(key, value) {
//         this.key = key;
//         this.value = value;
//     }
// }
class Solution {
    /**
     * @param {Pair[]} pairs
     * @returns {Pair[][]}
     */
    insertionSort(pairs) {
        let ans = []

        for(let i=0; i<pairs.length; ++i){
          
            //swap down from i index once necessary
            for(let j=i; j>0 && pairs[j-1].key > pairs[j].key; --j){
                let temp = pairs[j-1];
                pairs[j-1] = pairs[j];
                pairs[j] = temp;
            }

            ans.push([...pairs]);
        }

        return ans;
    }
}
