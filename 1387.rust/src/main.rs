struct Solution;

use std::collections::HashMap;

use std::hash::Hash;

// 强行写了个装饰器
struct Cached<A, R> {
    f: fn(A) -> R,
    cache: HashMap<A, R>,
}

impl<A, R> Cached<A, R>
where
    A: Eq + Hash + Clone,
    R: Clone,
{
    pub fn new(f: fn(A) -> R) -> Self {
        Self {
            f: f,
            cache: HashMap::new(),
        }
    }

    pub fn call(&mut self, args: A) -> R {
        if !self.cache.contains_key(&args) {
            self.cache.insert(args.clone(), (self.f)(args.clone())); // 如果写成self.f(args)，会认为是某个实例方法
        }

        return self.cache.get(&args).cloned().unwrap(); // 好多clone啊我要死了
    }
}

impl Solution {
    #[cfg(feature = "default")]
    pub fn get_kth(lo: i32, hi: i32, k: i32) -> i32 {
        let mut cache = HashMap::new(); // 可惜rust没有functools.lru_cache，也没有装饰器

        for i in 1..1001 {
            if !cache.contains_key(&i) {
                cache.insert(i, Solution::power(i));
            }
        }

        let mut array: Vec<i32> = (lo..hi + 1).collect();
        array.sort_by_key(|v| (cache[v], *v));

        return array[k as usize - 1];
    }

    #[cfg(feature = "decorator")]
    pub fn get_kth(lo: i32, hi: i32, k: i32) -> i32 {
        let mut power = Cached::new(Solution::power);

        for i in 1..1001 {
            power.call(i); // 找了一圈发现rust还没法做到impl Fn for Xxx，所以也没法做到power(i)这么优雅
        }
        // 可以看这里 <https://stackoverflow.com/questions/42859330/how-do-i-make-a-struct-callable>

        let mut array: Vec<i32> = (lo..hi + 1).collect();
        array.sort_by_key(|v| (power.call(*v), *v));

        return array[k as usize - 1];
    }

    fn power(n: i32) -> i32 {
        if n == 1 {
            return 1;
        } else if n % 2 == 0 {
            return 1 + Solution::power(n / 2);
        } else {
            return 1 + Solution::power(3 * n + 1);
        }
    }
}

fn main() {
    println!("{:?}", Solution::get_kth(12, 15, 2)); // 7
    println!("{:?}", Solution::get_kth(1, 1, 1)); // 1
    println!("{:?}", Solution::get_kth(7, 11, 4)); // 7
    println!("{:?}", Solution::get_kth(10, 20, 5)); // 13
    println!("{:?}", Solution::get_kth(1, 1000, 777)); // 570
}
