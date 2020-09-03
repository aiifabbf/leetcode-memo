/*
.. default-role:: math

给一个string，把这个string拆成全是回文substring的拆法有哪些？

比如给 ``aab`` ，有两种

-   拆成 ``aa, b``
-   拆成 ``a, a, b``

用回溯和动态规划都可以。

如果用动态规划，那么就是用 ``dp[j]`` 表示 ``s[0..j]`` 里所有的切法。要更新 ``dp[j]`` 的时候，去 `j` 的前面找所有能使 ``s[i..j]`` 正好是回文的 `i` ， ``dp[j]`` 就是所有这些 ``dp[i]`` 里每种切法后面追加 ``s[i..j]`` 。还有不要忘了把每个字符都切出来也是一种切法。

比如现在要知道 ``aab`` 的所有切法，已经知道了

-   ``a`` 的切法只有 ``[a]``
-   ``aa`` 的切法有 ``[aa], [a, a]`` 两种

那么加入 ``b`` 之后，切法有

-   ``ab`` 不是回文，忽略
-   ``aab`` 也不会回文，忽略
-   把每个字符单独切出来， ``[a, a, b]``

缺点就是太费内存了。所以下面用了回溯。

动态规划是从后往前想，如何利用前面的项算出 ``dp[j]`` ；回溯是从前面往后想，我现在已经决定在 `0, i_1, i_2, ..., i_n` 这些地方切了，下一个切点在哪里呢？

很容易，假设下一个切点是 `j` ，那么只要保证 `j > i_n` 并且 ``s[i_n..j]`` 是回文就可以了。在每个能使 ``s[i_n..j]`` 的 `j` 都切一下试试看，然后用回溯模板递归地往下走。
*/

struct Solution;

impl Solution {
    pub fn partition(s: String) -> Vec<Vec<String>> {
        // 因为回溯里频繁查询某个substring是否是回文，先传统艺能一下，干脆用O(n^2)的DP把每个substring是不是回文都给算出来
        let s: Vec<char> = s.chars().collect();
        let mut dp = vec![vec![false; s.len() + 1]; s.len() + 1]; // dp[i][j] == true表示s[i..j]是回文

        // 初始条件
        for i in 0..s.len() + 1 {
            dp[i][i] = true; // 空字符串是回文
        }

        // 初始条件
        for i in 0..s.len() {
            dp[i][i + 1] = true; // 单字符也是回文
        }

        // 这边的刷新顺序很有讲究，因为dp[i][j]依赖dp[i - 1][j + 1]，需要从表格的右上角、更新到左下角（如果表格的原点在左上角），是比较奇怪的顺序
        // 我这边就直接先更新所有长度是2的substring s[i..i + 2]、再更新所有长度是3的substring s[i..i + 3]……这样也不会出错
        for gap in 2..s.len() + 1 {
            for i in 0..s.len() - gap + 1 {
                let j = i + gap;
                // s[i..j]是不是回文、即dp[i][j]是否为true，完全取决于s[i]是不是等于s[j - 1]、并且s[i + 1..j - 1]是不是回文、即dp[i + 1][j - 1]是不是true
                if s[i] == s[j - 1] && dp[i + 1][j - 1] == true {
                    dp[i][j] = true;
                }
            }
        }

        let mut path = vec![];
        let mut res = vec![];
        Self::backtrack(&mut path, &dp, &s, &mut res);
        return res;
    }

    fn backtrack(
        path: &mut Vec<usize>, // 现在已经放了哪些分割点，包括0和n
        dp: &Vec<Vec<bool>>,
        s: &[char],
        res: &mut Vec<Vec<String>>,
    ) {
        if path.is_empty() {
            path.push(0);
            Self::backtrack(path, dp, s, res);
            path.pop();
        } else {
            let length = s.len(); // 字符串的长度
            if *path.last().unwrap() == length {
                // 如果最后一个分割点已经是n了，说明到头了。下面从分割点里提取出所有的substring
                let mut substrings: Vec<String> = vec![];

                for v in path.windows(2) {
                    // Rust的windows方法真好用啊
                    let i = v[0]; // substring的左边界
                    let j = v[1]; // 右边界
                    substrings.push(s[i..j].iter().collect()); // substring是s[i..j]
                }

                res.push(substrings);
            } else {
                // 如果还没到最后
                let i = *path.last().unwrap(); // 上一个分割点是哪里

                for j in i + 1..length + 1 {
                    // 试着从上一个分割点开始往后切1个、2个、3个……
                    if dp[i][j] == true {
                        // 如果在这里切正好能切出回文substring
                        path.push(j); // 那就试着在j这里切一下
                        Self::backtrack(path, dp, s, res); // 试着继续往下切
                        path.pop(); // 撤销在j这里切的操作
                    }
                }
            }
        }
    }
}

fn main() {
    dbg!(Solution::partition("aab".into())); // [["aa", "b"], ["a", "a", "b"]]
    dbg!(Solution::partition("abbab".into()));
}
