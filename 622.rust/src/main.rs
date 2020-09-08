/*
.. default-role:: math

实现circular ring buffer。

.. 和641一模一样，只不过这里只要单端进入、弹出，而641要双端进入、弹出。

直接看641的解释吧，写的非常详细。
*/

struct MyCircularQueue {
    head: usize,
    tail: usize,
    buffer: Vec<i32>,
    length: usize, // 如果不记录length，那么当head和tail重合的时候，你不知道buffer是空的还是满的
}

/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl MyCircularQueue {
    /** Initialize your data structure here. Set the size of the queue to be k. */
    fn new(k: i32) -> Self {
        Self {
            head: 0,
            tail: 0,
            buffer: vec![0; k as usize], // 直接分配一个大小是k的array
            length: 0,
        }
    }

    /** Insert an element into the circular queue. Return true if the operation is successful. */
    fn en_queue(&mut self, value: i32) -> bool {
        if self.length == self.buffer.len() {
            return false;
        } else {
            self.buffer[self.tail] = value;
            self.tail = (self.tail + 1) % self.buffer.len();
            self.length += 1;
            return true;
        }
    }

    /** Delete an element from the circular queue. Return true if the operation is successful. */
    fn de_queue(&mut self) -> bool {
        if self.length == 0 {
            return false;
        } else {
            self.head = (self.head + 1) % self.buffer.len();
            self.length -= 1;
            return true;
        }
    }

    /** Get the front item from the queue. */
    fn front(&self) -> i32 {
        if self.length == 0 {
            return -1;
        } else {
            return self.buffer[self.head];
        }
    }

    /** Get the last item from the queue. */
    fn rear(&self) -> i32 {
        if self.length == 0 {
            return -1;
        } else {
            if self.tail == 0 {
                return self.buffer[self.buffer.len() - 1];
            } else {
                return self.buffer[self.tail - 1];
            }
        }
    }

    /** Checks whether the circular queue is empty or not. */
    fn is_empty(&self) -> bool {
        return self.length == 0;
    }

    /** Checks whether the circular queue is full or not. */
    fn is_full(&self) -> bool {
        return self.length == self.buffer.len();
    }
}

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * let obj = MyCircularQueue::new(k);
 * let ret_1: bool = obj.en_queue(value);
 * let ret_2: bool = obj.de_queue();
 * let ret_3: i32 = obj.front();
 * let ret_4: i32 = obj.rear();
 * let ret_5: bool = obj.is_empty();
 * let ret_6: bool = obj.is_full();
 */
fn main() {
    let mut queue = MyCircularQueue::new(3);
    dbg!(queue.en_queue(1)); // true
    dbg!(queue.en_queue(2)); // true
    dbg!(queue.en_queue(3)); // true
    dbg!(queue.en_queue(4)); // false
    dbg!(queue.rear()); // 3
    dbg!(queue.is_full()); // true
    dbg!(queue.de_queue()); // true
    dbg!(queue.en_queue(4)); // true
    dbg!(queue.rear()); // 4
}
