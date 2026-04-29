class Solution {
    public boolean isValid(String s) {
        HashMap<Character,Character> parenMap = new HashMap<>();
        parenMap.put('(', ')');
        parenMap.put('[', ']');
        parenMap.put('{', '}');

        Stack<Character> parenStack = new Stack<>();

        //iterate through characters
        for(int i=0; i<s.length(); ++i){
            char c = s.charAt(i);

            //if opening char, add to stack
            if(parenMap.get(c) != null){
                parenStack.push(c);
            }
            //if closing char and not match top of stack --> return false
            else if(parenStack.empty() || parenMap.get(parenStack.peek()) != c){
                return false;
            }
            //if closing char and match --> pop the stack
            else if(parenMap.get(parenStack.peek()) == c){
                parenStack.pop();
            }
        }

        //ensure that all characters are matched -> stack empty
        return parenStack.empty();
    }
}
