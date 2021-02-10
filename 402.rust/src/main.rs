/*
.. default-role:: math

给最多 `k` 次机会，每次删掉一个数字，使得剩下的数字组成的十进制数最小。

.. 头条二面被问了这道……没想到这么难。

比如给 ``1432219`` ，给最多3次机会，怎么删呢？

1.  第一次肯定是删4，这样剩下的数字是 ``132219`` ，是最小的
2.  第二次删掉3，剩下 ``12219``
3.  第三次删掉2，剩下 ``1219``，似乎已经最小了

所以猜测是不是用greedy（虽然我也不知道怎么证明greedy是正确的）。

再看个例子 ``10200`` ，给一次机会，肯定是删掉1，这样1剩下 ``0200`` ，再去掉leading zeros，剩下200，是最小的。

感觉似乎是从左往右看，删掉满足“右边的数字小于自己”的数字，这样的步骤重复 `k` 次。但是假如字符串本身就是单调递增的，例如 ``12345`` ，找不到满足“右边的数字小于自己”的数字，这时候如果非要删除一个数字的话，删掉最右边的数字能使得剩下的数字最小。

这样做复杂度是 `O(n^2)` 。

聪明的你一定发现了，这不就是以前见过的单调递增stack吗？把原来字符串里边的数字从左到右一个一个放进stack里，同时要一直维持stack单调递增的性质。

具体方法是，每次要放入一个数字时候，和stack顶端的数字比较，如果小于等于顶端的数字，那没事了，直接放入就好了；如果大于顶端的数字，pop掉顶端的数字，继续比较，直到stack空、或者stack顶端的数字小于等于将要放入的数字。

每pop一次就相当于删掉一个数字，这道题里删除次数最大是 `k` ，所以pop之前还要加个条件，判断次数有没有用完。
*/

struct Solution;

impl Solution {
    #[cfg(feature = "stack")]
    pub fn remove_kdigits(num: String, k: i32) -> String {
        let mut stack = vec![];
        let mut k = k as usize; // 还能删多少次

        for v in num.chars() {
            // 从高位往低位看
            while k > 0 && !stack.is_empty() && *stack.last().unwrap() > v {
                // 与普通的单调递增stack相比，多加一个判断剩余删除次数
                stack.pop(); // pop一次相当于删除一次
                k -= 1; // 剩余次数减一
            } // 出while的时候，要么stack空了，要么stack顶端的数字小于等于v

            stack.push(v);
        }

        // 如果出现12345、但是仍然有剩余删除机会的情况，那么就pop掉最后的k个数字
        while k > 0 {
            stack.pop();
            k -= 1;
        }

        let res: String = stack.into_iter().skip_while(|v| *v == '0').collect(); // 用skip while删除leading zeros，方便又优雅
        if res.is_empty() {
            // corner case
            "0".to_owned()
        } else {
            res
        }
    }

    // 从左往右看，删掉满足“右边紧邻的数字小于自己”的数字，这样的步骤重复k次
    // 不太高效，不过直观
    #[cfg(feature = "array")]
    pub fn remove_kdigits(num: String, k: i32) -> String {
        let k = k as usize;
        if k >= num.len() {
            return "0".to_string();
        }
        let mut array: Vec<_> = num.chars().map(|v| v.to_digit(10).unwrap()).collect();

        for _ in 0..k {
            let mut removed = false;

            for i in 1..array.len() {
                if array[i - 1] > array[i] {
                    array.remove(i - 1);
                    removed = true;
                    break;
                }
            }

            if !removed {
                // 如果啥也没删掉，比如出现了12345这种情况，就删掉最后一位的5，留下1234，这样最小
                array.pop();
            }
        }

        // 去掉最前面的连续0
        let mut firstNonZeroIndex = array.len(); // 第一个非0出现的位置

        for i in 0..array.len() {
            if array[i] != 0 {
                firstNonZeroIndex = i;
                break;
            }
        }

        array.splice(..firstNonZeroIndex, std::iter::empty()); // splice可以一次性删掉。如果一个一个pop就太慢了

        // 这里写的真的太丑了，完全可以用drop while

        if array.is_empty() {
            return "0".to_string();
        } else {
            return array
                .into_iter()
                .map(|v| std::char::from_digit(v, 10).unwrap())
                .collect();
        }
    }
}

fn main() {
    println!("{:?}", Solution::remove_kdigits("1432219".to_string(), 3)); // 1219
    println!("{:?}", Solution::remove_kdigits("10200".to_string(), 1)); // 200
    println!("{:?}", Solution::remove_kdigits("10".to_string(), 2)); // 0
    println!("{:?}", Solution::remove_kdigits("100".to_string(), 1)); // 0
    println!("{:?}", Solution::remove_kdigits("112".to_string(), 1)); // 11
    println!("{:?}", Solution::remove_kdigits("9".to_string(), 1)); // 0
}
