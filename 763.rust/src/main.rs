/*
.. default-role:: math

给个字符串，把它切成尽可能多的非空substring（要连续），使得任意一种字符只出现在一个substring里、不会出现在别的substring里面

比如给 ``ababcbacadefegdehijhklij`` ，可以切成 ``ababcbaca, defegde, hijhklij`` ，有没有发现第一个substring里出现过的字符只有 ``a, b, c`` ，第二个substring里面出现过的字符是 ``d, e, f, g`` ，第三个substring里面出现过的字符是 ``h, i, j, k`` ，这三个substring里面出现过的字符种类没有交集。

当然切成 ``ababcbacadefegde, hijhklij`` 也满足无交集的约束，但是只能切成两个substring，而刚才的做法可以切成三个substring。

可以这么想：为了满足无交集的约束，首先要知道每种字符在整个字符串里，第一次出现的下标和最后一次出现的下标，比如在 ``ababcbacadefegdehijhklij`` 里面

-   ``a`` 第一次出现的位置是0，最后一次出现的位置是8
-   ``b`` 第一次出现的位置是1，最后一次出现的位置是5
-   ...

为了满足无交集的约束，不管怎么切， ``a`` 所在的那个substring的下标范围不能小于 `[0, 9)` ， 同理 ``b`` 所在的那个substring的下标范围不能小于 `[1, 5)` 。否则会出现 ``a`` 同时出现在两个不同substring里面的情况。

还有另一个问题， ``a`` 的范围 `[0, 9)` 里面不一定只有 ``a`` 这一种字符，还有可能有别的字符，比如 ``b`` ，为了同时满足 ``a`` 和 ``b`` 的约束，要把 ``a`` 的范围 `[0, 9)` 和 ``b`` 的范围 `[1, 5)` 合并起来，取它们的并集，才能使得 ``a`` 和 ``b`` 的约束同时满足。

::

    包含a的substring的最小范围
    |       |
    v       v
    ababcbacadefegdehijhklij
     ^   ^
     |   |
     包含b的substring的最小范围

所以直接转化成了56合并区间的问题了。把每种字符的最小合法substring区间给合并起来。

::

    ababcbacadefegdehijhklij
    ---------               a
     -----                  b
        ----                c
    ababcbacadefegdehijhklij
             ------         d
              ------        e
               -            f
                 -          g
    ababcbacadefegdehijhklij
                    ----    h
                     ------ i
                      ------j
                        -   k
                         -  l
*/

struct Solution;

use std::collections::HashMap;

impl Solution {
    pub fn partition_labels(s: String) -> Vec<i32> {
        let mut seen: HashMap<char, Vec<usize>> = HashMap::new(); // seen[v] = [i, j]表示字符v出现在了下标i、下标j处

        for (i, v) in s.chars().enumerate() {
            match seen.get_mut(&v) {
                Some(indexes) => {
                    indexes.push(i);
                }
                None => {
                    seen.insert(v, vec![i]);
                }
            }
        }

        // 如果字符v最早出现的下标是i、最后一次出现的下标是j，那么包含字符v的那个substring的范围至少是[i, j + 1)，否则会出现其他substring里也有字符v的情况，就不满足题目的约束了
        let mut intervals: Vec<(usize, usize)> = seen
            .into_iter()
            .map(|(k, v)| (*v.first().unwrap(), *v.last().unwrap() + 1))
            .collect(); // 把每个字符的最小substring区间记下来，比如a在1、2、3处出现了，那么第一次出现的下标是1，最后一次出现的下标是3，记为[1, 4)

        // 然后就是56题合并区间的套路了
        intervals.sort();

        let mut stack = vec![];

        for v in intervals.into_iter() {
            if stack.is_empty() {
                stack.push(v);
            } else {
                if stack.last().unwrap().1 <= v.0 {
                    // 这里是和56不同的地方，56题里面合并的是左开右开区间，所以相等的时候不算有交集。这里因为要尽可能多分组，所以我们的原则是能不合并的都不合并，所以相等的时候就不要合并了
                    stack.push(v);
                } else {
                    let mut merged = stack.pop().unwrap();
                    merged.0 = merged.0.min(v.0);
                    merged.1 = merged.1.max(v.1);
                    stack.push(merged);
                }
            }
        }

        return stack.into_iter().map(|v| (v.1 - v.0) as i32).collect();
    }
}

fn main() {
    dbg!(Solution::partition_labels(
        "ababcbacadefegdehijhklij".into()
    )); // [9, 7, 8]
}
