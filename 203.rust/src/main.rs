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
    // 拆散重组的做法
    // 稍微慢一点，因为需要重新在heap上申请内存
    #[cfg(feature = "move")]
    pub fn remove_elements(head: Option<Box<ListNode>>, val: i32) -> Option<Box<ListNode>> {
        let mut origin = head;
        let mut sentinel = Some(Box::new(ListNode::new(0)));
        let mut head = &mut sentinel;

        while let Some(mut node) = origin {
            origin = node.next;
            node.next = None;

            if node.val != val {
                head.as_mut().unwrap().next = Some(node); // 这里应该重新分配内存了
                head = &mut head.as_mut().unwrap().next;
            }
        }

        return sentinel.unwrap().next;
    }

    // 直接修改节点、把当前节点的内容直接变成后一个节点的内容的做法
    // 这种做法在没有指针概念的语言里（比如python）里无法做到
    // 稍微快一点，只会释放heap内存，不会malloc
    #[cfg(feature = "edit")]
    pub fn remove_elements(head: Option<Box<ListNode>>, val: i32) -> Option<Box<ListNode>> {
        let mut origin = head;
        let mut head = &mut origin;

        while let Some(node) = head.as_mut() {
            if node.val == val {
                // take之前从来都没有用过，是把一个Option的内容的所有权返回，原地留下None
                // 所以这里我的理解是大概把后一个节点的内容复制到当前节点的内容位置，同时把后一个节点的内容清零
                // 但是这个方法很奇怪，只需要&mut self，却能把内容的所有权返回给你，很神秘
                *head = node.next.take();
            // 有可能下一个节点也是val，所以这里不要head = head.next
            } else {
                if head.is_some() {
                    head = &mut head.as_mut().unwrap().next;
                } else {
                    break;
                }
            }
        }

        return origin;
    }

    // 其实我觉得两种做法都不优雅……但是一时间也想不到更好的、又能过编译的做法了
}

fn main() {
    dbg!(Solution::remove_elements(
        Some(Box::new(ListNode {
            val: 1,
            next: Some(Box::new(ListNode { val: 1, next: None }))
        })),
        1
    )); // []
}
