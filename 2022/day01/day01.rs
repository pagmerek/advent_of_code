use std::fs;

fn main() {
    let input = fs::read_to_string("input").unwrap();
    part1(&input);
    part2(&input);
}


fn part1(input: &String) {
    let contents = input
        .split("\n\n")
        .map(|s| {
            s.split("\n").map(|l| if l != "" {l.parse::<i32>().unwrap()} else {0}).sum()
        })
        .fold(0, |acc, x| if x > acc {x} else {acc});
    println!("part 1: {}", contents);
}

fn part2(input: &String) {
    let mut contents = input
        .split("\n\n")
        .map(|s| {
            s.split("\n").map(|l| if l != "" {l.parse::<i32>().unwrap()} else {0}).sum()
        })
        .collect::<Vec<i32>>();

    contents.sort_by(|a, b| b.cmp(a));

    let result: i32 = contents.iter()
        .take(3)
        .sum();

    println!("part 2: {}", result);
}


