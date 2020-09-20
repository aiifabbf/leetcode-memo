/*
.. default-role:: math

生成 `[l, h]` 范围内类似1234、2345这样逐位递增1的十进制数字。

比如给 `[100, 300]` ，总共有两个这样的数字123、234。

经典回溯。先试试第一个位置能不能填1、第二位能不能填2……再试试第一位能不能直接填2、第二位能不能填3……
*/

struct Solution;

impl Solution {
    pub fn sequential_digits(low: i32, high: i32) -> Vec<i32> {
        let mut path = 0;
        let mut res = vec![];
        Self::backtrack(&mut path, low, high, &mut res);
        res.sort();
        return res;
    }

    // path是已经做出的选择，res是结果集，每一层根据已经做出的选择，判断要不要放到结果集里、接下来做什么选择
    fn backtrack(path: &mut i32, low: i32, high: i32, res: &mut Vec<i32>) {
        if low <= *path && *path <= high {
            // 如果在范围里面，放入结果集
            res.push(*path);
        } // 这边别急着return，因为有可能1234满足条件，12345同样也满足条件

        if *path == 0 {
            // path为空
            for i in 1..10 {
                // 第一个数字放1到9都试一遍
                *path = i;
                Self::backtrack(path, low, high, res);
                *path = 0;
            }
        } else {
            if *path > high {
                // 如果已经比上界还大，那么没必要再继续下去了
                return;
            } else {
                let last = *path % 10; // 取得上一位的数字
                if last == 9 {
                    // 如果上一位已经是9了，那也没办法再加了
                    return;
                } else {
                    *path = *path * 10 + last + 1; // 123后面加个4，234后面加个5
                    Self::backtrack(path, low, high, res); // 继续下去试试
                    *path = *path / 10; // 撤回刚才的选择
                }
            }
        }
    }
}

fn main() {
    dbg!(Solution::sequential_digits(100, 300)); // [123, 234]
    dbg!(Solution::sequential_digits(1000, 13000)); // [1234, 2345, 3456, 4567, 5678, 5678, 6789, 12345]
}
