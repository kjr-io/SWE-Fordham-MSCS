use std::time::{Instant};

fn recursive_fib(n: i32) -> i32 {
    if n < 2 {
        return n;
    }
    return recursive_fib(n - 1) + recursive_fib(n - 2);
}

fn main() {
    let start = Instant::now();

    for _ in 0..1000{
        for i in 0..25 {
            recursive_fib(i);
        }
    }

    let duration = start.elapsed();

    println!("--- {:?} ---", duration);
}