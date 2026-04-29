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
        if(pairs.length == 0){
            return [];
        }

        let ans = [];
        ans.push([...pairs])
       
        for(let i=1; i<pairs.length; ++i){
            let current = pairs[i];
            let j = i-1;

            for(j; j>=0 && pairs[j].key > current.key; --j){
                pairs[j+1] = pairs[j];
            }
            pairs[j+1]=current;

            ans.push([...pairs]);
        }

        return ans;

    }
}
