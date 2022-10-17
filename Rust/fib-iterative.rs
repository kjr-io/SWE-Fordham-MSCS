use std::time::{Instant};

fn iterative_fib(n: i32) -> i32 {
    if n < 2 {
        return n
    }

    let mut a = 0;
    let mut b = 1;
    let mut i = 0;
    
    while i < n {
        let temp = a;
        a = b;
        b = temp + b;
        i = i + 1;
    }
    return a;
}

fn main() {
    let start = Instant::now();

    for _ in 0..10000000{
        for i in 0..25 {
            iterative_fib(i);
        }
    }

    let duration = start.elapsed();

    println!("--- {:?} ---", duration);
}

