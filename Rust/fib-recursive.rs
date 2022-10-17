#[allow(unsued_variables)]
fn recursive_fib(n: i32) -> i32 {
    if n < 2 {
        return n;
    }
    return recursive_fib(n - 1) + recursive_fib(n - 2);
}
