/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     constructor(val = 0, left = null, right = null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    /**
     * @param {TreeNode} p
     * @param {TreeNode} q
     * @return {boolean}
     */
    isSameTree(p, q){
        let pQueue = [];
        let qQueue = [];
        let pCurr = p
        let qCurr = q

        if(pCurr){pQueue.push(pCurr);}
        if(qCurr){qQueue.push(qCurr);}

        while(qQueue.length > 0 || pQueue.length > 0){
            pCurr = pQueue.shift();
            qCurr = qQueue.shift();

            if(pCurr == null && qCurr == null){
                continue;
            }

            if(pCurr == null || qCurr == null || pCurr.val != qCurr.val){
                return false;
            }

            pQueue.push(pCurr.left);
            pQueue.push(pCurr.right);
            qQueue.push(qCurr.left);
            qQueue.push(qCurr.right);        
        } 

        return true;
    }
}
