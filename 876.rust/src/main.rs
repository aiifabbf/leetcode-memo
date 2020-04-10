/*
.. default-role:: math

返回链表最中间的那个节点。如果链表是偶数长度的，返回中间靠右的那个节点。

先遍历一遍链表，得到链表的长度，假设长度是 `n` 吧。无论是奇数还是偶数长度，都是第 `\lfloor n / 2 \rfloor` 个节点。
*/

struct Solution;

// Definition for singly-linked list.
#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>,
}

impl ListNode {
    #[inline]
    fn new(val: i32) -> Self {
        ListNode { next: None, val }
    }
}

impl Solution {
    pub fn middle_node(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut length = 0;
        let mut origin = head;
        let mut head = &origin;

        while let Some(inner) = head.as_ref() {
            head = &inner.next;
            length += 1;
        }

        // head = &origin;

        // for _ in 0..length / 2 {
        //     head = &head.as_ref().unwrap().next;
        // }

        // return head.clone();
        // 我还在想怎么才能不clone
        // 终于想到了，第二次遍历的时候就不要遍历引用了，直接遍历原始变量就好了。

        let mut head = origin;

        for _ in 0..length / 2 {
            head = head.unwrap().next;
        }

        return head;
    }
}

fn main() {}
