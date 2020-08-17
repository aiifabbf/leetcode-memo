/*
.. default-role:: math

手上有 `n` 颗糖，有 `m` 个人，给第0个人发1颗糖，第1个人发2颗糖，……第 `n - 1` 个人发 `n` 颗糖，再回来，给第0个人发 `n + 1` 颗糖。如果中间糖不够了，发完即止。

虽然糖有 `10^9` 颗，但是因为每次都会多发一颗，所以实际上复杂度是 `O(n^0.5)` 。放心暴力。
*/

struct Solution;

impl Solution {
    pub fn distribute_candies(candies: i32, num_people: i32) -> Vec<i32> {
        let mut total = candies; // 现在手上有多少糖
        let mut res = vec![0; num_people as usize];
        let mut give = 1; // 这一次发多少颗糖

        for i in (0..res.len()).cycle() {
            if total <= give {
                // 如果手上的糖正好这次发完，或者不够
                res[i] += total; // 那就全给这个人
                break; // 然后就结束了
            } else {
                res[i] += give;
                total -= give;
                give += 1;
            }
        }

        return res;
    }
}

fn main() {
    dbg!(Solution::distribute_candies(7, 4)); // [1, 2, 3, 1]
    dbg!(Solution::distribute_candies(10, 3)); // [5, 2, 3]
}
