/*
.. default-role:: math

给 `n` 对括号，生成所有合法的组合

这里用回溯写了，python版本里是一年前写的前根遍历的做法。一年之后的现在我觉得回溯更好理解。
*/

struct Solution;

impl Solution {
    #[cfg(feature = "preorder-traversal")]
    pub fn generate_parenthesis(n: i32) -> Vec<String> {
        return Self::preorderTraversal(n, n);
    }

    fn preorderTraversal(left: i32, right: i32) -> Vec<String> {
        if (left == 0 && right > 0) {
            let str: String = String::from(")").repeat(right as usize); // ")" * right
            let mut res: Vec<String> = Vec::new();
            res.push(str);
            return res;
        } else if left >= 0 && left <= right {
            let mut res: Vec<String> = Vec::new();

            for v in Self::preorderTraversal(left - 1, right) {
                res.push(String::from("(") + &v);
            }

            for v in Self::preorderTraversal(left, right - 1) {
                res.push(String::from(")") + &v);
            }

            return res;
        } else {
            let res: Vec<String> = Vec::new();
            return res;
        }
    }

    #[cfg(feature = "backtrack")]
    pub fn generate_parenthesis(n: i32) -> Vec<String> {
        let mut path = vec![];
        let mut stack = vec![];
        let mut res = vec![];

        Self::backtrack(&mut path, &mut stack, n as usize, n as usize, &mut res);

        return res.into_iter().map(|v| v.into_iter().collect()).collect();
    }

    fn backtrack(
        path: &mut Vec<char>,
        stack: &mut Vec<char>, // 用来加速，这样就不用每次都扫一遍path才能确定能不能放右括号了
        left: usize,           // 可用的左括号的数量
        right: usize,          // 可用的右括号的数量
        res: &mut Vec<Vec<char>>,
    ) {
        if left == 0 && right == 0 && stack.is_empty() {
            // 这个判断条件有点冗余
            res.push(path.clone());
            return;
        } else {
            if left != 0 {
                path.push('(');
                stack.push('(');
                Self::backtrack(path, stack, left - 1, right, res);
                stack.pop();
                path.pop();
            }
            if right != 0 {
                if let Some(last) = stack.last() {
                    if *last == '(' {
                        // 如果stack的最后是个左括号，那么可以加一个右括号和它配对
                        path.push(')');
                        stack.pop();
                        Self::backtrack(path, stack, left, right - 1, res);
                        stack.push('('); // 恢复加入右括号之前的stack
                        path.pop();
                    }
                }
            }
        }
    }
}

fn main() {
    dbg!(Solution::generate_parenthesis(3));
}
