use std::io;

fn main() {
    let mut input = String::new();
    println!("Enter a number: ");
    io::stdin().read_line(&mut input).expect("Failed to read line");
    let n: usize = input.trim().parse().expect("Please enter a number");

    for i in 0..n {
        println!("{}{}", " ".repeat(n - i - 1), "*".repeat(2 * i +
