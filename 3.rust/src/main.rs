/*
.. default-role:: math

给一个string，问其中最长的、不含重复字符的substring的长度是多少。

上次看到这个题已经是一年前了，前两天面头条又被问了这道题，觉得有点印象，先写了一个 `O(n^2)` 的DP，然后也想到了 `O(n)` 双指针，但是又不确定对不对、会不会漏掉。面试官说是对的，我说我不确定，但是也找不出反例。于是写了双指针的版本，过了。

还是用DP比较稳妥。设 ``dp[i]`` 是以第 `i - 1` 个字符为结尾的（也就是以 ``s[i - 1]`` 结尾的）、最长的、不含重复字符的substring的长度 [#py]_ 。思考一下怎么从前面的项计算出 ``dp[i]`` 。

因为是substring，中间是不能断的，所以 ``dp[i]`` 只要看 ``dp[i - 1]`` 就可以了。先试着能不能把 ``s[i - 1]`` 追加到前面那个substring后面，这有两种情况

-   一种情况是类似 ``abcd`` 后面接 ``e`` ，完全没问题， ``abcde`` 符合条件，所以 ``dp[i] = dp[i - 1] + 1`` 就好了；
-   另一种情况是 ``abcd`` 后面接 ``b`` ，有点小问题，因为 ``b`` 在前一个substring里面出现过了。

解决第二种情况最简单的方法是从后往前扫描前一个substring，看前一个substring里面是否存在 ``s[i - 1]`` ，如果存在，假设绝对下标是 `h` ，那么 `[h, i)` 这段substring是以第 `i - 1` 个字符结尾的最长substring。

这样复杂度从原来的 `O(n^3)` 降低到 `O(n^2)` 了。

再想想能不能进一步优化，可以的。每次我们都要从后往前扫描前一个substring，看存不存在 ``s[i - 1]`` ，挺恶心的，能不能不要扫描，立刻就知道呢？可以啊，用hash set。但是只用set，只能知道存不存在，并不能知道那个绝对下标 `h` 是多少。

所以要用hash map，key是字符，value是这个字符 **最近一次** 出现的绝对下标 [#]_ 。检查 ``s[i - 1]`` 在不在前面一个substring里面，需要两个步骤

1.  先检查 ``s[i - 1]`` 在不在hash map里面

    如果不在，说明 ``s[i - 1]`` 在整个string里面都是第一次出现，放心大胆地追加到前一个substring后面吧。

    如果在，也不要慌张，有可能出现过，但是出现在前一个substring的范围之外。继续看下一步。

2.  检查 ``s[i - 1]`` 在不在前一个substring的范围之内

    现在你有 ``s[i - 1]`` 最近一次出现的绝对下标 `h` 了，但是 ``dp[i - 1]`` 告诉你说前一个substring的长度只有 `l` ，意味着前一个substring包含的下标范围是 `[i - 1 - l, i - 1)` 。

    所以只要比较一下 `h` 和 `i - 1 - l` 的大小关系不就好了嘛！如果 `h \geq i - 1 - l` ，说明 ``s[i - 1]`` 确实在前一个substring里面出现过了，只能从 `h + 1` 开始截断，这样，以 ``s[i - 1]`` 结尾的substring覆盖的范围就是 `[h + 1, i)` 了。所以此时 ``dp[i]`` 就是 `i - (h + 1)` 。

.. [#py] 在之前python的版本里，我把 ``dp[i]`` 定义成了以第 `i` 个字符结尾的最长不重复substring的长度，我现在觉得这是不对的，任何时候都应该遵循左闭右开的原则，可以减少巨多边界检查、越界之类的麻烦。但是这样也有不自然的地方，算 ``dp[i]`` 的时候反而看的是 ``s[i - 1]`` 。

.. [#] 这个我也是想了很久很久才想出来的。一开始怎么也想不出。

面头条的时候被问了这题，我写了双指针的版本，但是回来一想，发现根本没法证明正确性。这两天又连续做了类似的双指针的题（比如424、1004）。我觉得还是把双指针当成是DP的一种加速手段比较好理解。

用DP的角度来理解，就是计算出以 ``s[j - 1]`` 结尾的、最长的不含重复字符的substring。
*/

struct Solution;

use std::cmp::max;
use std::collections::HashMap;
use std::collections::HashSet;

impl Solution {
    // 用双指针和hash map加速的DP。比普通的DP简洁许多，我觉得目前见到的最好的方法
    #[cfg(feature = "fast-dp")]
    pub fn length_of_longest_substring(s: String) -> i32 {
        let string: Vec<char> = s.chars().collect();
        let mut i = 0;
        let mut seen: HashSet<char> = HashSet::new();
        let mut res = 0;

        for j in 1..string.len() + 1 {
            // 计算出以s[j - 1]结尾的、最长的不含重复字符的substring

            while seen.contains(&string[j - 1]) {
                // 不停地右移左指针i，直到集合里面不含s[j - 1]为止，这样才能保证唯一
                seen.remove(&string[i]);
                i += 1;
            }

            // 到这里，s[i..j]就是以s[j - 1]结尾的、最长的不含重复字符的substring了
            seen.insert(string[j - 1]);
            res = res.max(j - i); // 记录一下长度
        }

        return res as i32;
    }

    // 普通的DP
    #[cfg(feature = "dp")]
    pub fn length_of_longest_substring(s: String) -> i32 {
        let mut seen = HashMap::new();
        let s: Vec<char> = s.chars().collect();
        // let mut dp = vec![0]; // 设dp[i]是以第i - 1个字符结尾的、最长不含重复字符的substring的长度
        let mut lastDp = 0;
        let mut res = 0;

        for i in 1..s.len() + 1 {
            let mut thisDp = 0;
            if !seen.contains_key(&s[i - 1]) {
                // s[i - 1]在整个string里都是第一次出现
                thisDp = lastDp + 1; // 放心大胆地追加在前一个substring后面
            } else {
                // 放心用seen[v]，不会panic，因为到这里seen一定包含v
                if seen[&s[i - 1]] >= i - 1 - lastDp {
                    // 在前一个substring里面出现过s[i - 1]
                    thisDp = i - (seen[&s[i - 1]] + 1); // 从h + 1处截断
                } else {
                    thisDp = lastDp + 1;
                }
            }
            seen.insert(s[i - 1], i - 1); // 更新一下s[i - 1]最近一次出现的位置
            res = max(res, thisDp);
            lastDp = thisDp;
        }

        return res as i32;
    }

    // 又发现了一种双指针的做法，但是我没法证明这个是对的，而且边界条件很难写对。我还是推荐上面的DP+双指针加速的方法，又好理解、又好写
    #[cfg(feature = "two-pointers")]
    pub fn length_of_longest_substring(s: String) -> i32 {
        let s: Vec<char> = s.chars().collect();
        let mut left = 0;
        let mut right = 0;
        let mut seen = HashSet::new();
        let mut res = 0;

        while right < s.len() {

            while left < right {
                if seen.contains(&s[right]) {
                    seen.remove(&s[left]);
                    left += 1;
                } else {
                    break;
                }
            }

            seen.insert(s[right]);
            right += 1;
            res = max(res, right - left);
        }

        return res as i32;
    }
}

pub fn main() {
    println!(
        "{}",
        Solution::length_of_longest_substring("abcabcbb".to_string())
    ); // 3
    println!(
        "{}",
        Solution::length_of_longest_substring("bbbbb".to_string())
    ); // 1
    println!(
        "{}",
        Solution::length_of_longest_substring("pwwkew".to_string())
    ); // 3
    println!("{}", Solution::length_of_longest_substring("a".to_string())); // 1
    println!(
        "{}",
        Solution::length_of_longest_substring("au".to_string())
    ); // 2
    println!(
        "{}",
        Solution::length_of_longest_substring("aab".to_string())
    ); // 2
}
