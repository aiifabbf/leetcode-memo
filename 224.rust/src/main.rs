/*
.. default-role:: math

实现简单的计算器，只要实现正整数（不会出现 ``-2 + 1`` 这种）、加减、括号。

按照传统编译原理的点到为止……先把字符串变成token序列，然后再变成AST，再计算AST。这题没有乘除法，所以好像不需要用AST，我用了个stack就搞定了。

变成token的过程是把 ``23 + (1 + 2)`` 这样的字符串，变成一串有意义的符号，比如

::

    Number(23), Operator(Add), Parenthesis(Left), Number(1), Operator(Add), Number(2), Parenthesis(Right)

我用enum来表示token了。

变成token list之后，就想办法解析。用stack就可以了。大概有三种情况

-   遇到数字，看一下stack的顶端是不是加减号，如果是加减号，那么加减号前面肯定是个数字，这时候把加减号、数字全都pop出来，运算好了之后，再放回 **token list** 的最前面
-   遇到右括号，不用怀疑，stack的顶端肯定是个数字，再往里面是个左括号，所以直接把数字提取出来，放回token list的最前面
-   遇到其他情况，直接放进stack

这么做的好处是表达式是立即计算的，就像消消乐一样。假设字符串是 ``2 + (6 + 2)`` 整个过程是这样的

::

    stack              tokens
                    <- 2, +, (, 6, +, 2, )
    2               <- +, (, 6, +, 2, )
    2, +            <- (, 6, +, 2, )
    2, +, (         <- 6, +, 2, )
    2, +, (, 6      <- +, 2, )
    2, +, (, 6, +   <- 2, )
    2, +, (, 8      <- )
    2, +            <- 8
                    <- 10
    10

.. 做完发现去年做过……
*/

struct Solution;

use std::collections::VecDeque;

// 用enum来表示token
#[derive(Debug, Eq, PartialEq, Clone)]
enum Token {
    Operator(Operator),       // 加、减运算符
    Parenthesis(Parenthesis), // 括号
    Number(u64), // 数字。这题里面没有负数，所以不用考虑负数的情况，但是即使要考虑，我觉得也没法在tokenize阶段考虑
}

#[derive(Debug, Eq, PartialEq, Clone)]
enum Operator {
    Add,
    Sub,
}

#[derive(Debug, Eq, PartialEq, Clone)]
enum Parenthesis {
    Left,
    Right,
}

impl Solution {
    // 从algorithms书学来的，Dijkstra发明的2 stack做法
    // pub fn calculate(s: String) -> i32 {
    //     let mut tokens = Self::tokens(&s[..]);

    //     let mut operators = vec![];
    //     let mut operands = vec![];

    //     while let Some(token) = tokens.pop_front() {
    //         match &token[..] {
    //             "+" | "-" => {
    //                 operators.push(token);
    //             }
    //             "(" => {}
    //             ")" => {
    //                 let operator = operators.pop().unwrap();
    //                 let b = operands.pop().unwrap();
    //                 let a = operands.pop().unwrap();
    //                 let value = match &operator[..] {
    //                     "+" => a + b,
    //                     "-" => a - b,
    //                     _ => 0,
    //                 };
    //                 operands.push(value);
    //             }
    //             _ => {
    //                 operands.push(token.parse::<i32>().unwrap());
    //             }
    //         }
    //     }

    //     // return operands.pop().unwrap_or(0);
    //     return 0;
    // }
    // 好吧，2 stack对表达式的要求非常非常严格，要求每个二元表达式两边都有括号，所以1 + 1 + 1这种必须要写成((1 + 1) + 1)才能用2 stack

    pub fn calculate(s: String) -> i32 {
        let mut tokens = Self::tokens(&s[..]);
        let mut stack = vec![];

        while let Some(token) = tokens.pop_front() {
            match token {
                Token::Parenthesis(Parenthesis::Right) => {
                    // 遇到右括号，类似(, 2遇到)的情况
                    let token = stack.pop().unwrap(); // stack顶端肯定是个数字
                    stack.pop().unwrap(); // 再往里面是个左括号
                    tokens.push_front(token); // 直接把数字拿出来，放到token list的最前面
                }
                Token::Number(b) => {
                    // 遇到数字
                    if let Some(last) = stack.last().cloned() {
                        // 看下stack顶端是什么
                        match last {
                            Token::Operator(operator) => {
                                // 如果stack顶端是加减号，那么可以确定再往里面一个是数字，类似2, +遇到1的情况
                                stack.pop(); // 把加减号pop出来
                                if let Token::Number(a) = stack.pop().unwrap() {
                                    let token = Token::Number(match operator {
                                        // 看下是加号还是减号
                                        Operator::Add => a + b,
                                        Operator::Sub => a - b,
                                    });
                                    tokens.push_front(token); // 算完后放进token list的最前面
                                }
                            }
                            _ => {
                                // 可能stack顶端是左括号，类似(遇到1的情况
                                stack.push(token);
                            }
                        }
                    } else {
                        // stack是空的，那就直接放进stack里
                        stack.push(token);
                    }
                }
                _ => {
                    // 其他情况都放到stack里
                    stack.push(token);
                }
            }
        }

        return stack
            .pop()
            .map(|v| match v {
                Token::Number(v) => v as i32,
                _ => 0,
            })
            .unwrap_or(0); // 最后stack里唯一的token就是结果啦
    }

    // "23 + (1 + 2)"变成[Number(23), Operator(Add), Parenthesis(Left), Number(1), Operator(Add), Number(2), Parenthesis(Right)]
    fn tokens(s: &str) -> VecDeque<Token> {
        let mut res: VecDeque<Token> = VecDeque::new();
        let tokenize = |c| match c {
            '(' => Token::Parenthesis(Parenthesis::Left),
            ')' => Token::Parenthesis(Parenthesis::Right),
            '+' => Token::Operator(Operator::Add),
            '-' => Token::Operator(Operator::Sub),
            v => Token::Number(v.to_digit(10).unwrap() as u64),
        }; // 把char变成Token

        for v in s.chars() {
            if !v.is_whitespace() {
                if res.is_empty() {
                    let token = tokenize(v);
                    res.push_back(token);
                } else {
                    if v.is_ascii_digit() {
                        // 如果是数字的话，有可能和前一个数字一起组成多位数
                        if let Some(last) = res.back_mut() {
                            // 前面有Token的话
                            match last {
                                Token::Number(w) => {
                                    // 如果前面的Token是数字，当前字符也是数字，那么合并成一个Token
                                    *w = *w * 10 + v.to_digit(10).unwrap() as u64;
                                }
                                _ => {
                                    let token = tokenize(v);
                                    res.push_back(token);
                                }
                            }
                        } else {
                            let token = tokenize(v);
                            res.push_back(token);
                        }
                    } else {
                        let token = tokenize(v);
                        res.push_back(token); // 好多重复的，有时间优化一下
                    }
                }
            } // 忽略空格
        }

        return res;
    }
}

fn main() {
    dbg!(Solution::calculate("1 + 1".into())); // 2
    dbg!(Solution::calculate(" 2-1 + 2 ".into())); // 3
    dbg!(Solution::calculate("(1+(4+5+2)-3)+(6+8)".into())); // 23
    dbg!(Solution::calculate("23 + 87".into())); // 110
}
