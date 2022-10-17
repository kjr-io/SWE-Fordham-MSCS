fn iterative_fib(n: i32) -> i32 {
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
    let result = iterative_fib(10);
    println!("{}", result);
}