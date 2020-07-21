struct Solution;

impl Solution {
    pub fn winner_square_game(n: i32) -> bool {
        let n = n as usize;
        let mut dp = vec![false; n + 1];
        dp[0] = false;

        for i in 1..n + 1 {
            if (1..).take_while(|j| i >= j * j).any(|j| !dp[i - j * j]) {
                // 这个式子和递推式长得太像了
                dp[i] = true;
            }
        }

        return dp[n];
    }
}

fn main() {
    dbg!(Solution::winner_square_game(1)); // true
    dbg!(Solution::winner_square_game(2)); // false
    dbg!(Solution::winner_square_game(4)); // true
    dbg!(Solution::winner_square_game(7)); // false
}
