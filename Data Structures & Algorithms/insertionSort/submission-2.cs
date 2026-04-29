// Definition for a pair
// public class Pair {
//     public int Key;
//     public string Value;
//
//     public Pair(int key, string value) {
//         Key = key;
//         Value = value;
//     }
// }
public class Solution {
    public List<List<Pair>> InsertionSort(List<Pair> pairs) {
        List<List<Pair>> ans = new List<List<Pair>>();

        //iterate through list
        for(int i=0; i<pairs.Count; ++i){

            //swap list down
            int j=i;
            while(j>0 && pairs[j-1].Key > pairs[j].Key){
                Pair temp  = pairs[j-1];
                pairs[j-1]  = pairs[j];
                pairs[j] = temp;               
                --j;
            }

            //Save State Afetr Every Subset Sorted
            List<Pair> newList = new List<Pair>(pairs);
            ans.Add(newList);

        }


        return ans;
    }
}
