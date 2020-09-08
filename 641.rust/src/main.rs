/*
.. default-role:: math

实现底层是circular ring buffer的双端队列，需要能从两端都能pop和push。

.. 622只要实现单端队列。

所谓circular ring buffer是个非常巧妙的数据结构，只会在初始化的时候申请一次内存，之后不会像array list那样扩容。底层是一个固定长度的array。在队列尾部添加元素，如果已经占用了array的最后一个空位，之后会“拐弯”拐回array的最前面，利用前面的空闲空间。

具体是怎么拐弯的？一开始的时候是这样的

::
                 n-1
    | | | | | ... | |
    0 1 2 3 4       n

空的。现在在队列尾部追加元素1

::
                 n-1
    |1| | | | ... | |
    0 1 2 3 4       n

再追加一个2

::
                 n-1
    |1|2| | | ... | |
    0 1 2 3 4       n

现在pop front

::
                 n-1
    | |2| | | ... | |
    0 1 2 3 4       n

继续追加

::
                 n-1
    | |2|3|4| ... |n|
    0 1 2 3 4       n

继续追加……啊哦，array满了，但是最前面还有空位，那就把下一个放到最前面吧

::
                 n-1
    |x|2|3|4| ... |n|
    0 1 2 3 4       n

再次pop front

::
                 n-1
    |x| |3|4| ... |n|
    0 1 2 3 4       n

大概就是这样。

如果应用场景是个非常平衡的单端队列，一端进入一个元素、另一端出去一个元素，那么circular ring buffer非常高效。

我的做法是初始化的时候就分配一个长度固定的array，然后用head和tail指针来表示数据部分的边界。

比如

::
                 n-1
    | | | | | ... | |
    0 1 2 3 4       n
    ^       ^
    h       t

这时候队列的长度是 `t - h = 4` 。假设不停在尾部添加元素，直到

::
                 n-1
    | | | | | ... | |
    0 1 2 3 4       n
    ^             ^
    h             t

tail指针到了 `n - 1` ，如果此时再加一个元素，tail会瞬移到0，和head重合。

::

                 n-1
    | | | | | ... | |
    0 1 2 3 4       n
    ^
    h
    t

可是队列一开始没东西的时候，head和tail也是重合的，和现在的情况完全一样，我们无法区分全空和全满了，怎么办呢？另外用length记一下队列的长度就好了。

另外head和tail的范围都是 `[0, n)` ，这就涉及到模除的问题。怎样把head和tail限制在 `[0, n)` 里面呢？用维基百科里的trick <https://en.wikipedia.org/wiki/Circular_buffer> 很方便

-   当需要增加1的时候，比如现在在 `n - 1` 应该直接跳到0，用 ``(t + 1) % capacity`` ，其中 ``capacity`` 就是一开始分配的固定长度的array的长度
-   当需要减少1的时候，比如现在在0，应该直接跳到 `n - 1` ，用 ``(t + capacity - 1) % capacity``

.. 面美团被问了这个问题。

.. 今天读到一篇文章 <https://zhuanlan.zhihu.com/p/225120404> 讲美团在内的外卖平台对送餐员的强力剥削，触目惊心。
*/

struct MyCircularDeque {
    head: usize,      // 左边界，下一个pop front的元素是buffer[head]
    tail: usize,      // 右边界，下一个push back的元素放入buffer[tail]
    buffer: Vec<i32>, // 初始化的时候就建一个长度固定的array
    length: usize,    // 如果不记录length，那么当head和tail重合的时候，你不知道buffer是空的还是满的
}

/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl MyCircularDeque {
    /** Initialize your data structure here. Set the size of the deque to be k. */
    fn new(k: i32) -> Self {
        Self {
            head: 0,
            tail: 0,
            buffer: vec![0; k as usize], // 建一个长度固定的array
            length: 0,
        }
    }

    /** Adds an item at the front of Deque. Return true if the operation is successful. */
    fn insert_front(&mut self, value: i32) -> bool {
        let capacity = self.buffer.len();

        if self.length == capacity {
            // buffer满了，没法放入新元素了
            return false;
        } else {
            self.head = (self.head + capacity - 1) % capacity; // 先把左边界head往左边移动一个单位。这个trick从维基百科上学来的 <https://en.wikipedia.org/wiki/Circular_buffer>
            self.buffer[self.head] = value; // 然后在这里放入元素
            self.length += 1; // 不要忘记更新长度
            return true;
        }
    }

    /** Adds an item at the rear of Deque. Return true if the operation is successful. */
    fn insert_last(&mut self, value: i32) -> bool {
        let capacity = self.buffer.len();

        if self.length == capacity {
            return false;
        } else {
            // push back也差不多，只是push front是先移动head、再放入元素，push back是先放入元素、再移动tail
            self.buffer[self.tail] = value;
            self.tail = (self.tail + 1) % capacity; // 也是从维基上学来的。tail的范围是[0, n)，如果这时候tail是n - 1，右移一个单位应该到0而不是到n
            self.length += 1;
            return true;
        }
    }

    /** Deletes an item from the front of Deque. Return true if the operation is successful. */
    fn delete_front(&mut self) -> bool {
        let capacity = self.buffer.len();

        if self.length == 0 {
            // 本来就是空的，无法pop
            return false;
        } else {
            // pop front根本都不用真的删掉元素，直接动指针就可以了
            self.head = (self.head + 1) % capacity; // 一样的道理。想想head如果现在是n - 1，右移一个单位之后应该是0
            self.length -= 1;
            return true;
        }
    }

    /** Deletes an item from the rear of Deque. Return true if the operation is successful. */
    fn delete_last(&mut self) -> bool {
        let capacity = self.buffer.len();

        if self.length == 0 {
            return false;
        } else {
            self.tail = (self.tail + capacity - 1) % capacity;
            self.length -= 1;
            return true;
        }
    }

    /** Get the front item from the deque. */
    fn get_front(&self) -> i32 {
        if self.length == 0 {
            return -1;
        } else {
            return self.buffer[self.head];
        }
    }

    /** Get the last item from the deque. */
    fn get_rear(&self) -> i32 {
        let capacity = self.buffer.len();

        if self.length == 0 {
            return -1;
        } else {
            let index = (self.tail + capacity - 1) % capacity;
            return self.buffer[index];
        }
    }

    /** Checks whether the circular deque is empty or not. */
    fn is_empty(&self) -> bool {
        return self.length == 0;
    }

    /** Checks whether the circular deque is full or not. */
    fn is_full(&self) -> bool {
        return self.length == self.buffer.len();
    }
}

/**
 * Your MyCircularDeque object will be instantiated and called as such:
 * let obj = MyCircularDeque::new(k);
 * let ret_1: bool = obj.insert_front(value);
 * let ret_2: bool = obj.insert_last(value);
 * let ret_3: bool = obj.delete_front();
 * let ret_4: bool = obj.delete_last();
 * let ret_5: i32 = obj.get_front();
 * let ret_6: i32 = obj.get_rear();
 * let ret_7: bool = obj.is_empty();
 * let ret_8: bool = obj.is_full();
 */
fn main() {
    let mut deque = MyCircularDeque::new(3);
    dbg!(deque.insert_last(1)); // true
    dbg!(deque.insert_last(2)); // true
    dbg!(deque.insert_front(3)); // true
    dbg!(deque.insert_front(4)); // false
    dbg!(deque.get_rear()); // 2
    dbg!(deque.is_full()); // true
    dbg!(deque.delete_last()); // true
    dbg!(deque.insert_front(4)); // true
    dbg!(deque.get_front()); // 4
}
