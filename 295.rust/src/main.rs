/*
从一个流里面读数字，计算至今为止见过的所有数的中位数。

想一想中位数的定义

-   如果array是偶数长度，中位数是从小到大排好序之后，最中间两个数的平均
-   如果array是奇数长度，中位数就是最中间那个数

需要快速得到最中间那两个数。

看了 `评论区 <https://leetcode.com/problems/find-median-from-data-stream/discuss/74062/Short-simple-JavaC%2B%2BPython-O(log-n)-%2B-O(1)>`_ ，想了一下想出来了。搞两个heap

-   第一个heap是一个最大heap，存至今为止见过的所有数字从小到大排好序之后的前半部分，也就是小的那半部分。或者说这第一个heap里面的数是至今为止见过的所有数字里，最小的那 `n / 2` 个数字。
-   第二个heap是一个最小heap，存至今为止见过的所有数字从小到达排好序之后的后半部分，也就是大的那半部分。或者说这第二个heap里面存的数字是至今为止见过的所有数字里，最大的那 `n / 2` 个数字。

如果至今为止见过的数字有偶数个，那么两个heap大小相同；如果至今为止见过的数字是奇数个，那么第一个heap比第二个heap多一个元素，也就是多那个中位数。

比如假设现在已经读了 ``5, 2, 1, 4, 3`` ，第一个heap里会有

::

    1, 2, 3

第二个heap里会有

::

    4, 5

第一个heap的顶端元素是 ``3`` ，正好就是中位数。

假设现在已经读了 ``2, 3, 1, 4`` ，第一个heap里有

::

    1, 2

第二个heap里有

::

    3, 4

中位数此时是两个heap顶端的元素的平均。

这样的话，无论什么时候要求计算中位数，都能在 `O(1)` 完成，为啥呢？

-   如果至今已经读了奇数个数字

    最好办，中位数直接就是前半部分的最后一个数字，也就是第一个heap的最顶端的那个数。

-   如果至今已经读了偶数个数字

    也很简单，最中间两个数字的左边那个数字，在第一个heap的最顶端，右边那个数字，在第二个heap的最顶端。直接平均一下就好了。

读取新的数字的时候稍微难搞一点，需要维护两个heap的性质

-   第一个heap要么和第二个heap长度相等，要么第一个heap比第二个heap多一个元素
-   第一个heap里的所有数字都必须小于等于第二个heap里的任意一个数字

那么根据第一个性质，有两种情况

-   第一个heap和第二个heap长度相等

    说明之前读了偶数个数字，现在这个数字读进来之后，就算读了奇数个数字了，所以第一个heap这回处理完之后会比第二个heap多一个元素。

    那现在进来的这个数字怎么办呢？肯定不能无脑插到第一个heap里面吧，比如现在已经读了 ``1, 2, 3, 4`` ，第一个heap是 ``1, 2`` ，第二个heap是 ``3, 4`` 。现在来了个 ``5`` ，直接把这个 ``5`` 插到第一个heap里面肯定不对啊，我们希望来了 ``5`` 之后，第一个heap里面是 ``1, 2, 3`` ，第二个heap里是 ``4, 5`` 才对。

    所以显然要决定一下要不要先调整当前两个heap里的元素，再把新来的数加到正确的heap里。那怎么决定呢？也是有两种情况

    -   新来的数可以放到第一个heap

        如果新来的数小于等于第二个heap里面最小的数（也就是heap顶端的数），那么新来的数就可以放心地放到第一个heap里，不会破坏之前提到的两个约束。你想想是不是这样，新来的数放到第一个heap里之后，第一个heap里任意一个数仍然小于等于第二个heap里任意一个数。

    -   新来的数不能放到第一个heap，只能放到第二个heap里

        如果新来的数大于第二个heap里面最小的数，那么新来的数只能放到第二个heap，但是如果就这样放到第二个heap里，会破坏第一条约束，第二个heap里面的元素个数反而比第一个heap大了。

        所以要先从第二个heap里面剔除一个数，放到第一个heap里之后，再把新来的数放到第二个heap里。剔除哪个数呢？肯定是最小的那个数啊。

-   第一个heap比第二个heap大1

    说明之前读了奇数个数字，现在这个数字读进来之后，就读了偶数个数字了，所以第一个heap和第二个heap在这一轮处理过后元素数量变得相等了。

    还是和上面的case一样的处理方法，看新来的数能不能放到第二个heap里。如果新来的数大于等于第一个heap里最大的数（也就是heap顶端的数），那么放心地把新来的数放到第二个heap里面，不会破坏约束。

    如果不能，和上面的case一样处理，先从第一个heap里剔除一个数，剔除哪个？当然是剔除第一个heap里最大的数（也就是顶端的数），放到第二个heap里，再把新来的数放到第一个heap里。
*/

use std::cmp::Reverse;
use std::collections::BinaryHeap;

struct MedianFinder {
    lowerHalf: BinaryHeap<i32>, // 至今见过的所有数从小到大排好序之后的前半部分，也就是小的那部分
    upperHalf: BinaryHeap<Reverse<i32>>, // 至今见过的所有数从小到大排好序之后的后半部分，也就是大的那部分
}

/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl MedianFinder {
    /** initialize your data structure here. */
    fn new() -> Self {
        Self {
            lowerHalf: BinaryHeap::new(),
            upperHalf: BinaryHeap::new(),
        }
    }

    fn add_num(&mut self, num: i32) {
        // 复杂度O(ln n)，n是至今为止见过的数的数量
        if self.lowerHalf.len() == self.upperHalf.len() {
            // 小半部分和大半部分大小相同，说明刚才见过了奇数个数
            if self.lowerHalf.len() == 0 {
                // 有可能是还没有读任何一个数哦
                self.lowerHalf.push(num); // 既然允许小半部分的元素数量最多比大半部分的元素数量多1个，那么就插在小半部分里面了
            } else {
                // 读了偶数个数字了，此时中位数是最中间那两个数的平均
                let Reverse(upperFirst) = self.upperHalf.peek().unwrap().clone();
                if num <= upperFirst {
                    // num比大半部分heap里所有的数都小或者相等
                    self.lowerHalf.push(num); // 直接放到小半部分里，不会破坏约束
                } else {
                    // num至少大于大半部分里最小的数
                    self.upperHalf.pop(); // 剔除大半部分里最小的数
                    self.lowerHalf.push(upperFirst); // 放到小半部分里
                    self.upperHalf.push(Reverse(num)); // 再把新来的数字放到大半部分里
                }
            }
        } else {
            // 小半部分和大半部分大小相同，说明刚才见过了偶数个数
            let lowerLast = self.lowerHalf.peek().unwrap().clone(); // 小半部分的最大的那个数
            if num >= lowerLast {
                // 如果新来的数大于等于小半部分最大的数，说明新来的数可以直接被放到大半部分，不会破坏约束
                self.upperHalf.push(Reverse(num));
            } else {
                // 不然，新来的数只能放到小半部分
                self.lowerHalf.pop(); // 踢掉小半部分最大的那个数，给新来的数腾出空间
                self.upperHalf.push(Reverse(lowerLast)); // 被踢掉的数只能放到大半部分里了
                self.lowerHalf.push(num); // 再把新来的数放到小半部分里
            }
        }
    }

    fn find_median(&self) -> f64 {
        // 复杂度O(1)
        // println!("{:?}", self.lowerHalf);
        // println!("{:?}", self.upperHalf);
        if self.lowerHalf.len() == self.upperHalf.len() {
            let a = self.lowerHalf.peek().unwrap().clone();
            let Reverse(b) = self.upperHalf.peek().unwrap().clone();
            return (a + b) as f64 / 2.0;
        } else {
            return self.lowerHalf.peek().unwrap().clone() as f64;
        }
    }
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * let obj = MedianFinder::new();
 * obj.add_num(num);
 * let ret_2: f64 = obj.find_median();
 */

fn main() {
    let mut obj = MedianFinder::new();
    obj.add_num(1);
    obj.add_num(2);
    println!("{:?}", obj.find_median()); // 1.5
    obj.add_num(3);
    println!("{:?}", obj.find_median()); // 2

    let mut obj = MedianFinder::new();
    obj.add_num(-1);
    println!("{:?}", obj.find_median()); // -1
    obj.add_num(-2);
    println!("{:?}", obj.find_median()); // -1.5
    obj.add_num(-3);
    println!("{:?}", obj.find_median()); // -2
    obj.add_num(-4);
    println!("{:?}", obj.find_median()); // -2.5
    obj.add_num(-5);
    println!("{:?}", obj.find_median()); // -3
}
