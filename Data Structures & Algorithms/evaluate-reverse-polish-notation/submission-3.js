class Solution {
    /**
     * @param {string[]} tokens
     * @return {number}
     */
    evalRPN(tokens){
        const opSet = new Set(['+', '-', '*', '/']);
        const stack = [];
        for(let t of tokens){
           if(opSet.has(t)){
              let p2 = stack.pop();
              let p1 = stack.pop();
              switch(t){
                case '+':
                   stack.push(p1 + p2);
                   break;
                case '-':
                   stack.push(p1 - p2);
                   break;
                case '*':
                   stack.push(p1 * p2);
                   break;
                case '/':
                   stack.push(Math.trunc(p1 / p2));
                   break;
              }
           }
           else{
             stack.push(parseInt(t,10));
           }
        }

        return stack.pop();
    }
}
