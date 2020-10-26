/*
.. default-role:: math

婚礼上的香槟塔，每个杯子最多只能盛1单位的香槟，从顶端倒下 `x` 单位的香槟，最终香槟塔的某一层的某个杯子里有多少单位的香槟呢？

香槟塔长这样

::

        1
       1 1
      1 1 1
     1 1 1 1
    1 1 1 1 1

不是二叉树的样子，是第一层上有一个杯子、第二层上有两个杯子……

如果从顶层倒下1单位的香槟

::

     1
    0 0

如果倒下2单位的香槟，因为顶层的杯子已经满了，多出的香槟只能溢出来

::

       1
    0.5 0.5

如果倒下3单位的香槟

::

     1
    1 1

想了好久能不能总结出通项公式，duang一下马上就算出来，发现想不出。所以就模拟一下吧。
*/

struct Solution;

impl Solution {
    pub fn champagne_tower(poured: i32, query_row: i32, query_glass: i32) -> f64 {
        let query_row = query_row as usize;
        let query_glass = query_glass as usize;
        let mut res = vec![];

        for i in 0..query_row + 2 {
            // 因为要得到第query_row层的香槟，所以res的长度至少是query_row + 1
            // 但是这里把res的长度弄成了query_row + 2，这是因为我们是根据当前层的杯子里有多少香槟来判断当前这个杯子有没有溢出的香槟的，如果有溢出，就把溢出的量均分，加到下一层对应的两个杯子里。所以第query_row层是需要更新的，而第query_row + 1层就不管了
            res.push(vec![0.0; i + 1]);
        }

        res[0][0] = poured as f64; // 在顶端倒下这么多香槟

        // 然后模拟
        for i in 0..query_row + 1 {
            for j in 0..i + 1 {
                if res[i][j] > 1.0 {
                    // 溢出了
                    let delta = res[i][j] - 1.0; // 多出的部分
                    res[i + 1][j] += delta / 2.0; // 均分到下层的两个杯子里
                    res[i + 1][j + 1] += delta / 2.0;
                    res[i][j] = 1.0; // 不知道为什么不加这个不对
                }
            }
        }

        return res[query_row][query_glass];
    }
}

fn main() {
    dbg!(Solution::champagne_tower(1, 1, 1)); // 0
    dbg!(Solution::champagne_tower(2, 1, 1)); // 0.5
    dbg!(Solution::champagne_tower(100_000_009, 33, 17)); // 1
}
