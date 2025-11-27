fn factorial(n: u128) -> u128 {
    let mut total = 1;
    for ite in 1..(n+1) {
        total *= ite;
    }
    return total;
}

fn main() {
    let num: u128 = 25;
    let result = factorial(num);
    println!("The factorial of {} is {}", num, result);
}