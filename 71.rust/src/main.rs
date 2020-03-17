/*
格式化unix路径

比如给个很怪的路径 ``/a/b/./../..`` 要能够输出最简单的路径 ``/`` 。

题目标了stack，那就用stack做吧……那选择哪个字符作为触发器呢？可能一开始会选 ``.`` 和 ``/`` ，但是选 ``.`` 是有问题的，比如这个test case

::

    /...

惊不惊喜？ ``...`` 是可以作为正常的文件名的，如果你用 ``.`` 作为触发器的话，确实能处理 ``.`` 和 ``..`` ，但是不能处理 ``...`` 。

所以只用 ``/`` 就够了。别忘了最后加一个dummy ``/`` ，这样在处理 ``/a/b/..`` 这种的时候方便一点。

状态转移图大概是这样的

-   遇到不是 ``/`` 的

    直接放到stack里，不用管。

-   遇到 ``/``

    -   如果stack是空的，直接放
    -   如果stack不是空的

        -   看stack最后一个是否是 ``/``
        
            如果是 ``/`` 的话，说明出现了类似 ``/a/b//`` 这种重复的 ``/`` 的情况，直接忽略掉就好了。

        -   看stack是否以 ``/..`` 结尾
        
            如果以 ``/..`` 结尾，要回到上一级目录。可以不停地pop，直到pop到第二个 ``/`` 为止，比如 ``/a/b/..`` 需要pop到第二个 ``/`` 为止，才能到 ``/a`` 。

        -   看stack是否 ``/.`` 结尾

            如果以 ``/.`` 结尾，说明遇到了类似 ``/a/b/.`` 的情况，这也是冗余的情况，直接pop掉最后的 ``.`` 就可以了。

应该能包括所有的情况了。
*/

struct Solution;

impl Solution {
    pub fn simplify_path(path: String) -> String {
        let mut stack = vec![];

        for v in path.chars().chain(vec!['/'].into_iter()) {
            // 遍历的时候假装最后补一个/
            match v {
                '/' => { // 遇到了/
                    if stack.ends_with(&['/', '.', '.']) { // /a/b/c/..
                        let mut counter = 0; // 至今为止遇到了多少个/

                        while !stack.is_empty() {
                            let node = stack.pop().unwrap();
                            if node == '/' {
                                counter += 1;
                            }
                            if counter == 2 { // 遇到第二个/的时候，停止
                                break;
                            }
                        }

                        stack.push('/');
                    } else if stack.ends_with(&['/', '.']) { // /a/b/c/.
                        stack.pop();
                    } else if stack.ends_with(&['/']) { // /a/b/c/
                        continue;
                    } else { // /a/b/c
                        stack.push(v);
                    }
                }
                w => { // 其他
                    stack.push(w);
                }
            }
        }

        if stack.ends_with(&['/']) {
            // 去除末尾的/
            stack.pop();
        }

        if stack.is_empty() {
            stack.push('/');
        }
        return stack.into_iter().collect::<String>();
    }
}

pub fn main() {
    println!("{:?}", Solution::simplify_path("/home/".to_string())); // /home
    println!("{:?}", Solution::simplify_path("/../".to_string())); // /
    println!("{:?}", Solution::simplify_path("/home//foo/".to_string())); // /home/foo
    println!(
        "{:?}",
        Solution::simplify_path("/a/./b/../../c/".to_string())
    ); // /c
    println!(
        "{:?}",
        Solution::simplify_path("/a//b////c/d//././/..".to_string())
    ); // /a/b/c
    println!("{:?}", Solution::simplify_path("/.".to_string())); // /
    println!("{:?}", Solution::simplify_path("/../../..".to_string())); // /
    println!("{:?}", Solution::simplify_path("/...".to_string())); // /... 这是最坑的test case，只有 ``.`` 和 ``..`` 是特殊文件名，而 ``...`` 只是一个正常的文件名
}
