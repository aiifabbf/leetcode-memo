/*
.. default-role:: math

实现hash set

因为输入范围是 `[0, 10^6]` ，所以最暴力的办法就是直接搞一个长度是 `10^6 + 1` 的array， ``array[i] = true`` 表示在集合里， ``array[i] = false`` 表示不在集合里。这样最快，但是有点浪费空间。

稍微进阶一点的是搞成电话本、或者像桶排序的桶一样。不要搞那么大的array，搞个小一点的，做成电话本的首字母目录，用来定位在哪个桶。把hash函数设计成 `h(x) = x \mod c` 其中 `c` 是array的长度。所有hash相同的数字放在同一个桶里。要判断key在不在集合里面的时候，先计算hash，定位到它应该在哪个桶里，再遍历那个桶。

.. 听说初代JVM里就是这样做的，桶是用的链表。

再进阶玩法就很多了，如果hash碰撞很频繁，链表就很慢，可以进化成二分搜索树。

.. 去年这时候我还觉得hash set是超级理想的数据结构，居然能做到常数查询。现在发现好像也并不是那么理想……可能是因为hash set的高效在python的低速下显得很快吧……
*/

struct MyHashSet {
    buckets: Vec<Vec<i32>>,
}

/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl MyHashSet {
    /** Initialize your data structure here. */
    fn new() -> Self {
        Self {
            buckets: vec![vec![]; 1000],
        }
    }
    fn add(&mut self, key: i32) {
        let bucket = self.buckets.get_mut(key as usize % 1000).unwrap();
        if let Some(_) = bucket.iter().position(|v| v == &key) {
            return;
        } else {
            bucket.push(key);
        }
    }

    fn remove(&mut self, key: i32) {
        let bucket = self.buckets.get_mut(key as usize % 1000).unwrap();
        if let Some(index) = bucket.iter().position(|v| v == &key) {
            bucket.remove(index);
        }
    }

    /** Returns true if this set contains the specified element */
    fn contains(&self, key: i32) -> bool {
        let bucket = self.buckets.get(key as usize % 1000).unwrap();
        if let Some(_) = bucket.iter().position(|v| v == &key) {
            return true;
        } else {
            return false;
        }
    }
}

/**
 * Your MyHashSet object will be instantiated and called as such:
 * let obj = MyHashSet::new();
 * obj.add(key);
 * obj.remove(key);
 * let ret_3: bool = obj.contains(key);
 */
fn main() {
    let mut obj = MyHashSet::new();
    obj.add(1);
    obj.add(2);
    // dbg!(&obj.buckets);
    dbg!(obj.contains(1)); // true
    dbg!(obj.contains(3)); // false
    obj.add(2);
    // dbg!(&obj.buckets);
    dbg!(obj.contains(2)); // true
    obj.remove(2);
    // dbg!(&obj.buckets);
    dbg!(obj.contains(2)); // false
}
