/*
.. default-role:: math

把array最后一个元素移动到最前面，做 `k` 次。

比如 ``1, 2, 3, 4, 5, 6, 7`` ，移动3次

1.  第一次变成 ``7, 1, 2, 3, 4, 5, 6``
2.  第二次变成 ``6, 7, 1, 2, 3, 4, 5``
3.  第三次变成 ``5, 6, 7, 1, 2, 3, 4``

所以最后结果是 ``5, 6, 7, 1, 2, 3, 4`` 。

如果不限制空间，很简单。关键题目要求用 `O(1)` 空间，就有点难。

那找一找规律吧。基本操作是把 ``a[i]`` 移动到 ``a[(i + offset) % len]`` ，移动之前要记下 ``a[(i + offset) % len]`` 本来的值，再把 ``a[(i + offset) % len]`` 移动到 ``a[(i + 2 * offset) % len]`` ……最后总会覆盖到每个元素的吧？

看上去挺简单的，但是考虑 ``1, 2, 3, 4, 5, 6`` 移动4次，就有问题了

::

    1 2 3 4 5 6
    |_______|

            |__
    ____|

        |______
    |

发现1移动到了5，5移动到了3，3移动到了1，出现了循环，然而2没有移动到6。

猜测一下和gcd有关，因为6和4的gcd是2，所以移动 `6 / 2 = 3` 次之后会出现一次循环，并且需要以开头的2个数字作为起点，做一轮循环移动，不然会出现有些数字没有移动的情况。

结果猜对了……

那么每一轮循环怎么写呢？可以想一下现实中人会怎么做。我把上面的array想象成6张卡片，要把面值是1的卡片移动到面值是5的卡片的位置上，5移动到3，3移动到1，怎么移动呢？

1.  可以先把1摘下来拿在手里
2.  把手里的1放到5的位置，把5摘下来拿在手里
3.  把手里的5放到3的位置，把3摘下来拿在手里
4.  把手里的3放到1的位置
*/

struct Solution;

impl Solution {
    pub fn rotate(nums: &mut Vec<i32>, k: i32) {
        let offset = (k as usize) % nums.len(); // 如果array长度是8，移动8次等于没移动，所以移动15次等于净移动了7次

        if offset == 0 {
            return;
        } else {
            // 以[1, 2, 3, 4, 5, 6]移动4为例子
            let gcd = Self::gcd(offset, nums.len()); // 算出6和4的gcd是2

            for start in 0..gcd {
                // 以开头2个数字为起点，开始一轮循环移动
                let mut i = start; // 手里拿的是卡片i
                let mut swap = nums[i]; // 手里现在拿着卡片i上面的数字

                for _ in 0..nums.len() / gcd {
                    // 每一轮移动3张卡片
                    let j = (i + offset) % nums.len(); // 要把卡片i放到j位置
                    std::mem::swap(&mut nums[j], &mut swap); // 把卡片i放到j的位置，再把j位置上的卡片摘下来放在手里，所以简而言之就是交换手里的卡片和j位置的卡片
                    i = j;
                }
            }
        }
    }

    fn gcd(a: usize, b: usize) -> usize {
        match b {
            0 => a,
            b => Self::gcd(b, a % b),
        }
    }
}

fn main() {
    let mut array = vec![1, 2, 3, 4, 5, 6, 7];
    Solution::rotate(&mut array, 3);
    dbg!(&array); // [5, 6, 7, 1, 2, 3, 4]

    let mut array = vec![-1, -100, 3, 99];
    Solution::rotate(&mut array, 2);
    dbg!(&array); // [3, 99, -1, -100]

    let mut array = vec![1];
    Solution::rotate(&mut array, 0);
    dbg!(&array); // [1]

    let mut array = vec![1, 2, 3, 4, 5, 6];
    Solution::rotate(&mut array, 4);
    dbg!(&array); // [3, 4, 5, 6, 1, 2]
}
