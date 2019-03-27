impl Solution {
    pub fn generate_parenthesis(n: i32) -> Vec<String> {
        return Solution::preorderTraversal(n, n);
    }

    pub fn preorderTraversal(left: i32, right: i32) -> Vec<String> {
        if (left == 0 && right > 0) {
            let str: String = String::from(")").repeat(right as usize); // ")" * right
            let mut res: Vec<String> = Vec::new();
            res.push(str);
            return res;
        } else if (left >= 0 && left <= right) {
            let mut res: Vec<String> = Vec::new();

            for v in Solution::preorderTraversal(left - 1, right) {
                res.push(String::from("(") + &v);
            }

            for v in Solution::preorderTraversal(left, right - 1) {
                res.push(String::from(")") + &v);
            }

            return res;
        } else {
            let res: Vec<String> = Vec::new();
            return res;
        }
    }
}