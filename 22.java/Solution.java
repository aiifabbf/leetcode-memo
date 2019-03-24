/* 

*/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<String> generateParenthesis(int n) {
        return this.preorderTraversal(n, n);
    }

    public List<String> preorderTraversal(int left, int right) {
        if (left == 0 && right > 0) {
            String str = String.join("", Collections.nCopies(right, ")"));
            List<String> res = new ArrayList<>();
            res.add(str);
            return res;
        } else if (left >= 0 && left <= right) {
            List<String> res = new ArrayList<>();

            for (String v: this.preorderTraversal(left - 1, right)) {
                res.add("(" + v);
            }

            for (String v: this.preorderTraversal(left, right - 1)) {
                res.add(")" + v);
            }
            return res;
        } else {
            return new ArrayList<>();
        }
    }
}